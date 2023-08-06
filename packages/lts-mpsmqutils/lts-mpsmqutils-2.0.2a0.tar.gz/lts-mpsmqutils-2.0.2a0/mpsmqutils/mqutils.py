import os, json, time, datetime, stomp
from contextlib import contextmanager
from tenacity import retry, stop_after_attempt, wait_random_exponential
from traceback import format_exc
# Job tracker module
import mpsjobtracker.trackers.jobtracker as jobtracker

jt = None
def get_jt():
    global jt
    if not jt:
        jt = jobtracker.JobTracker()
    return jt

_user = os.getenv('MQ_USER')
_password = os.getenv('MQ_PASSWORD')
_queue = os.getenv('QUEUE_NAME')
_client_id = f"mqutils_{os.getenv('HOSTNAME')}"

_host = os.getenv('MQ_HOST')
_port = os.getenv('MQ_PORT')
_failback_host = os.getenv('MQ_HOST_FAILBACK', None)
_failback_port = os.getenv('MQ_PORT_FAILBACK', None)
_hosts = [(_host, _port,)]

if _failback_host and _failback_port:
    _hosts.append((_failback_host, _failback_port,))

_max_reconnects = 1000

def create_initial_queue_message(job_ticket_id, parent_job_ticket_id = None):
    '''Creates a queue json message to be picked up by the worker'''
    print("************************ MQUTILS - CREATE_INITIAL_QUEUE_MESSAGE *******************************")
    try:
        message = __create_ingest_message(job_ticket_id, 0, "success", parent_job_ticket_id)
        print("MESSAGE TO QUEUE create_initial_queue_message")
        print(message)
    except Exception as e:
        print(e)
        raise(e)
    return message

def create_next_queue_message(ticket_id, parent_job_ticket_id = None):
    '''Creates a message for the next task in the job'''
    print("************************ MQUTILS - CREATE_NEXT_QUEUE_MESSAGE *******************************")
    message = None
    try:
        message = __create_ingest_message(ticket_id, 1, "success", parent_job_ticket_id)
        print("MESSAGE TO QUEUE create_next_queue_message")
        print(message)
    except Exception as e:
        print(e)
        raise(e)
    return message

def create_requeue_message(ticket_id, parent_job_ticket_id = None):
    '''Creates a queue json message for the current task to be requeued'''
    print("************************ MQUTILS - CREATE_REQUEUE_MESSAGE *******************************")
    try:
        jt = get_jt()
        job_tracker_file = jt.get_tracker_document(ticket_id)
        job_management = job_tracker_file.get("job_management")
        if (job_management is None):
            raise Exception ('Tracker File is malformed, missing job_management')
        prev_step_status = job_management["previous_step_status"]
        message = __create_ingest_message(ticket_id, 0, prev_step_status, parent_job_ticket_id)
        print("MESSAGE TO QUEUE create_requeue_message")
        print(message)
    except Exception as e:
        print(e)
        raise(e)
    return message

def create_revert_message(ticket_id, parent_job_ticket_id = None):
    print("************************ MQUTILS - CREATE_REVERT_MESSAGE *******************************")
    '''Creates a queue json message to revert the previous task
         Returns None if there is no previous message'''
    message = None
    try:
        message = __create_ingest_message(ticket_id, -1, "failed", parent_job_ticket_id)
        print("MESSAGE TO QUEUE create_revert_message")
        print(message)
    except Exception as e:
        print(e)
        raise(e)
    return message

def create_task_manager_queue_message(job_ticket_id, parent_job_ticket_id = None):
    print("************************ MQUTILS - CREATE_TASK_MANANGER_QUEUE_MESSAGE *******************************")
    json_message = {
        "job_ticket_id": job_ticket_id,
        "task_name": "task_manager_worker_inprocess",
        "previous_step_status" : "success",
        "category": "task_management"
    }
    print(json_message)
    print("parent job ticket id:")
    print(parent_job_ticket_id)
    if parent_job_ticket_id:
        json_message["parent_job_ticket_id"] = parent_job_ticket_id
    message = json.dumps(json_message)
    print(message)
    return message

NOTIFY_QUEUE = os.getenv('MQ_NOTIFY_QUEUE', '/queue/iiif_notify')
def create_notification(sender, recipients, subject, message, method="email", **opts):
    print("************************ MQUTILS - CREATE_NOTIFICATION *******************************")
    jt=get_jt()
    message = json.dumps({
        "from": sender,
        "to": recipients,
        "subject": subject,
        "message": message,
        "options": opts,
        "timestamp": jt.get_timestamp_utc_now(),
        "method": method
    })
    print(message)

    with managed_mq_connect() as conn:
        conn.send(NOTIFY_QUEUE, message, headers = {"persistent": "true"})

CACHE_MANAGER_QUEUE = os.getenv('MQ_CACHE_MANAGER_QUEUE', '/queue/mps-asset-db-cache')
def create_cache_refresh_message(**opts):
    print("************************ MQUTILS - CREATE_CACHE_REFRESH_MESSAGE *******************************")
    jt = get_jt()
    message = json.dumps({
        "category": "cache_management",
        "timestamp": jt.get_timestamp_utc_now(),
        "options": opts
    })
    print(message)
    with managed_mq_connect() as conn:
        conn.send(CACHE_MANAGER_QUEUE, message, headers = {"persistent": "true"})

def create_multi_asset_ingest_queue_message(job_ticket_id):
    print("************************ MQUTILS - CREATE_MULTI_ASSET_INGEST_QUEUE_MESSAGE *******************************")
    json_message = {
        "job_ticket_id": job_ticket_id,
        "task_name": "multi_asset_ingest",
        "previous_step_status" : "success",
        "category": "task_management"
    }
    print(json_message)
    message = json.dumps(json_message)
    return message

def __create_ingest_message(ticket_id, step_number_increment, prev_step_status, parent_job_ticket_id = None):
    print("************************ MQUTILS - CREATE_INGEST_MESSAGE *******************************")
    '''Helper method for the create messages above'''
    jt = get_jt()
    print(ticket_id)
    print(parent_job_ticket_id)
    job_tracker_file = jt.get_tracker_document(ticket_id)

    timestamp = jt.get_timestamp_utc_now()

    job_management = job_tracker_file.get("job_management")
    if (job_management is None):
        print("Malformed Tracker File")
        raise Exception ('Tracker File is malformed, missing job_management.')

    current_step = int(job_management["current_step"])
    print("current step:")
    print(current_step)
    step_number = current_step + step_number_increment
    print("step number:")
    print(step_number)

    steps_list = job_management["steps"]
    # Get step by looking up the step by step number
    event = jt.filter_element_by_property(steps_list, "step_number", step_number)
    if not event:
        return None
    task_name = event[0]["task_name"]
    event_name = event[0]["worker_type"]

    msg_json = {
        "event": event_name,
        "timestamp": timestamp,
        "job_ticket_id": str(ticket_id),
        "task_name": task_name,
        "current_step": step_number,
        "previous_step_status": prev_step_status,
        "category": "ingest"
    }
    if parent_job_ticket_id:
        print("parent job ticket id:")
        print(parent_job_ticket_id)
        msg_json["parent_job_ticket_id"] = parent_job_ticket_id

    print("msg json:")
    print(msg_json)
    message = json.dumps(msg_json)
    return message
