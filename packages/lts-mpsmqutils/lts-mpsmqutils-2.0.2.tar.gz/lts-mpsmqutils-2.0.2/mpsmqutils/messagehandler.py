import datetime, email, json, os, re, smtplib, time, traceback
import celery as celeryapp

from textwrap import dedent

import mpsmqutils.mqutils as mqutils
# Job tracker module
import mpsjobtracker.trackers.jobtracker as jobtracker
job_tracker = jobtracker.JobTracker()

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

retry_strategy = Retry(
    total=3,
    status_forcelist=[429, 500, 502, 503, 504],
    backoff_factor=1
)
adapter = HTTPAdapter(max_retries=retry_strategy)
http_client = requests.Session()
http_client.mount("https://", adapter)
http_client.mount("http://", adapter)

# The queue to notify the task manager that a worker is starting
_tm_queue = os.getenv('TASK_MANAGER_QUEUE_NAME', '/queue/worker-in-process')

_hostname_prefix = os.getenv('HOSTNAME') + ": "

# Notify config for use in the notify application
NOTIFY_QUEUE = os.getenv('MQ_NOTIFY_QUEUE', '/queue/iiif_notify')
DLQ_QUEUE = os.getenv('MQ_DLQ_QUEUE', '/queue/ActiveMQ.DLQ')

# Email SMTP host for use in notify
NOTIFY_MAIL_RELAY=os.getenv('MQ_NOTIFY_MAIL_RELAY', None)
NOTIFY_DEFAULT_EMAIL=os.getenv('MQ_NOTIFY_DEFAULT_EMAIL', None)

def call_worker_api(task_name, job_ticket_id = None, parent_job_ticket_id = None, worker_url_endpoint = 'do_task', worker_url = os.getenv('WORKER_API_URL'), add_params=None):
    print("************************ MQUTILS MQLISTENER - CALL WORKER API *******************************")
    '''Call the worker API and process the response in a standard format'''

    result = {
      'success': False,
      'error': None,
      'message': None
    }
    print("result:")
    print(result)
    job_ticket_id_str = f" job_ticket_id: {job_ticket_id}" if job_ticket_id else ""
    parent_job_ticket_id_str = f" parent_job_ticket_id: {parent_job_ticket_id}" if parent_job_ticket_id else ""
    print(f'mqlistener call_worker_api START{job_ticket_id_str}{parent_job_ticket_id_str} task_name {task_name}')

    """
      Call worker API internally to perform the task
      This API call is calling the worker task in the same container and must use the internal container port
    """
    try:

        if not worker_url:
            error_msg = 'Missing configuration WORKER_API_URL'
            print(error_msg, flush=True)
            raise Exception(error_msg)
        url = worker_url + '/' + worker_url_endpoint
        print('mqlistener call_worker_api url {}'.format(url), flush=True)
        json_params = { 'task_name': task_name }
        if add_params:
            json_params = {**json_params, **add_params}
        if job_ticket_id:
            json_params['job_ticket_id'] = job_ticket_id
        if parent_job_ticket_id:
            json_params['parent_job_ticket_id'] = parent_job_ticket_id
        print("json_params")
        print(json_params)
        # The worker uses a self-signed certificate and it does not need to be verified since the listener makes a request to the worker inside the same container internally
        response = http_client.post(url, json = json_params, verify=False)
        response.raise_for_status()
        print(response)
    except Exception as e:
        print(e)
        if job_ticket_id:
            job_tracker.append_error(job_ticket_id, 'mqlistener call_worker_api API call failed', traceback.format_exc(), True)
        raise Exception(e)

    print(f'mqlistener call_worker_api COMPLETE{job_ticket_id_str}{parent_job_ticket_id_str} task_name {task_name} response.json() {response.json()}', flush=True)

    response_json = response.json()
    print(response_json)

    success = False if not response_json.get('success') else True
    print("success:")
    print(success)
    result['success'] = success
    result['error'] = response_json.get('error', None)
    result['message'] = response_json.get('message', None)

    return result

def call_generic_worker_api(message_data, worker_endpoint):
    print("************************ MQUTILS MQLISTENER - CALL GENERIC WORKER API *******************************", flush=True)
    '''Call the worker API and process the response in a standard format'''

    result = {
      'success': False,
      'error': None,
      'message': None,
      'next_queue': None
    }
    worker_url = os.getenv('WORKER_API_URL') + '/' + worker_endpoint

    """
      Call worker API internally to perform the task
      This API call is calling the worker task in the same container and must use the internal container port
    """
    try:
        if not worker_url:
            error_msg = 'Missing configuration WORKER_API_URL'
            print(error_msg, flush=True)
            raise Exception(error_msg)
        url = worker_url
        print('mqlistener call_generic_worker_api url {}'.format(url), flush=True)
        # The worker uses a self-signed certificate and it does not need to be verified since the listener makes a request to the worker inside the same container internally
        response = http_client.post(url, json = message_data, verify=False)
        print('made request', flush=True)
        response.raise_for_status()
        print('response.raise_for_status', flush=True)
        print(response, flush=True)
    except Exception as e:
        print(e)
        raise Exception(e)

    response_json = response.json()
    print(response_json, flush=True)

    success = False if not response_json.get('success') else True
    print("success:", flush=True)
    print(success, flush=True)
    result['success'] = success
    result['error'] = response_json.get('error', None)
    result['message'] = response_json.get('message', None)
    result['next_queue'] = response_json.get('next_queue', None)

    return result

def handle_worker_response(job_ticket_id, worker_response, parent_job_ticket_id=None):
    print("************************ MQUTILS MQLISTENER - HANDLE_WORKER_RESPONSE *******************************")
    """Handle the response from the worker API
    Capture any error messages returned in the json body
    Examples worker API responses:
    Response was successful: { success: true }
    Response had an error: { success: false, 'error': 'Example error', 'message': 'Example error message' }
    """
    task_success = True if worker_response.get('success') else False
    print("task success")
    print(task_success)
    if not task_success:
        # Set job failed if the job is a child job
        set_job_failed = True if parent_job_ticket_id else False
        job_tracker.append_error(job_ticket_id, worker_response.get('error'), worker_response.get('message'), set_job_failed)
    return task_success

completed_statuses = frozenset(['success', 'failed'])
class MqMessageHandler():
    def __init__(self, message):
        self.message = message

    def handle_message(self):
        print("************************ MQUTILS MQLISTENER - HANDLE_MESSAGE *******************************")
        # headers, body = frame.headers, frame.body
        print('handling message "%s"' % self.message)

        category = self.message.get("category", "ingest")
        task_success = False
        job_ticket_id = self.message.get('job_ticket_id')
        print('job_ticket_id {}'.format(job_ticket_id))
        try:
            job_tracker_doc = job_tracker.get_tracker_document(job_ticket_id)
        except Exception as e:
            import traceback
            print("Exception trying to get tracker_document: " + traceback.format_exc())
            job_tracker_doc = None

        print('job_tracker_doc {}'.format(job_tracker_doc))
        status = job_tracker_doc['job_management']['job_status']
        if status in completed_statuses:
            print(f'Status {status} counts as completed, assuming job is complete')
            #Assume if the tracker is completed or not there, that this job is no longer running
            return

        print(f"Dispatching based on category: {category}", flush=True)
        if (category == "ingest"):
            task_success = self.__ingest_message_handler(self.message)
        elif (category == "task_management"):
            task_success = self.__task_management_message_handler(self.message)
        elif (category == "service"):
            task_success = self.__service_message_handler(self.message)
        elif (category == "cache_management"):
            task_success = self.__cache_management_message_handler(self.message)

        #Sometimes the ack/nack might be sent in the handler
        if (task_success != None):
            if not task_success:
                # TODO: ack is sent automatically after task completes
                # TODO: unsure how nack works in the case of celery
                job_tracker.set_job_status('failed', job_ticket_id, "failed")
                print('Task unsuccessful')
                # self.conn.nack(message_id, self._sub_id)

        #TODO- Handle
        print('processed message for job id {}'.format(job_ticket_id))

    def __ingest_message_handler(self, message_data):
        print("************************ MQUTILS MQLISTENER - INGEST_MESSAGE_HANDLER *******************************")
        print('ingest message')
        job_ticket_id = message_data.get('job_ticket_id')
        print('job_ticket_id {}'.format(job_ticket_id))
        parent_job_ticket_id = message_data.get('parent_job_ticket_id', None)
        print('parent_job_ticket_id {}'.format(parent_job_ticket_id))
        task_name = message_data.get('task_name')
        print('task_name {}'.format(task_name))
        previous_step_status = message_data.get('previous_step_status', 'success')
        print('previous_step_status {}'.format(previous_step_status))
        task_success = False
        worker_url_endpoint = "do_task"

        try:
            print('set_job_status to running')
            job_tracker.set_job_status('running', job_ticket_id)
        except Exception as e:
            print(e)
            return False

        #Send a message to the task manager queue as long as this isn't the task manager message
        tm_message = mqutils.create_task_manager_queue_message(job_ticket_id, parent_job_ticket_id)
        print('sending tm message {} to queue {}'.format(tm_message, _tm_queue))
        celeryapp.execute.send_task("tasks.tasks.do_task", args=[tm_message], kwargs={}, queue=_tm_queue)

        # Run the service
        # Check if previous step status was successful
        if previous_step_status and 'fail' not in previous_step_status:
            # Update timestamp file before do task
            print('BEFORE DO TASK UPDATING TIMESTAMP FILE job_ticket_id {}'.format(job_ticket_id))
            print('CALLING DO TASK')
            print('job_ticket_id {} task_name {}'.format(job_ticket_id, task_name))

            worker_url_endpoint = "do_task"

            nextmessage = mqutils.create_next_queue_message(job_ticket_id, parent_job_ticket_id)
            print('create_next_queue_message nextmessage {}'.format(nextmessage))

        else:
            # Update timestamp file before revert task
            print('BEFORE REVERT TASK UPDATING TIMESTAMP FILE job_ticket_id {}'.format(job_ticket_id))
            job_tracker.update_timestamp(job_ticket_id)

            print('CALLING REVERT TASK')
            print('job_ticket_id {} task_name {}'.format(job_ticket_id, task_name))
            worker_url_endpoint = "revert_task"

            # Create next queue message
            nextmessage = mqutils.create_revert_message(job_ticket_id, parent_job_ticket_id)
            print('create_revert_message nextmessage {}'.format(nextmessage))
        try:
            #Update the timestamp
            job_tracker.update_timestamp(job_ticket_id)
            print("SUCCESSFULLY UPDATED TIMESTAMP job_ticket_id {} parent_job_ticket_id {}".format(job_ticket_id, parent_job_ticket_id))
        except Exception as e:
            print(e)
            return False


        # Call task
        try:
            worker_response = call_worker_api(task_name, job_ticket_id, parent_job_ticket_id, worker_url_endpoint)
            task_success = handle_worker_response(job_ticket_id, worker_response, parent_job_ticket_id)
            print("SUCCESS IN WORKER RESPONSE TRY BLOCK")
        except Exception as e:
            print(e)
            task_success = False
            job_tracker.append_error(job_ticket_id, str(e), traceback.format_exc(), True)

        if (task_success):
            # Update timestamp file after task is complete
            print('AFTER TASK UPDATING TIMESTAMP FILE job_ticket_id {}'.format(job_ticket_id))
            job_tracker.update_timestamp(job_ticket_id)
            if nextmessage is None:
                job_tracker.set_job_status(previous_step_status, job_ticket_id)
                #There are no more items to queue so the job is actually finished.
                #TODO: LTSIIIF-499 Call manifest services at the end of the workflow
                print('******** LAST TASK COMPLETED ********')
                print('previous_step_status {} job_ticket_id {} parent_job_ticket_id {}'.format(previous_step_status, job_ticket_id, parent_job_ticket_id))
            else:
                try:
                    json_message = json.loads(nextmessage)
                    print('json_message {}'.format(json_message))
                    print(json_message)
                except ValueError as e:
                    print(e)
                    job_tracker.append_error(job_ticket_id, 'Unable to get parse the next queue message',  traceback.format_exc(), False)
                    raise e

                # Set the queue name to match the worker type
                worker_type = json_message["event"]
                queue = worker_type
                print('worker_type {}'.format(worker_type))
                tracker_doc = job_tracker.get_tracker_document(job_ticket_id)
                # Update the number of tries in the tracker file
                tracker_doc["job_management"]["numberOfTries"] = 0
                tracker_doc["job_management"]["current_step"] = json_message["current_step"]
                tracker_doc["job_management"]["job_status"] = "queued"
                tracker_doc["job_management"]["previous_step_status"] = json_message["previous_step_status"]
                try:
                    print('******** UPDATE TRACKER FILE ********')
                    updated_tracker_doc = job_tracker.replace_tracker_doc(tracker_doc)
                    print('updated_tracker_doc {}'.format(updated_tracker_doc))
                except Exception as e:
                    #TODO what to do here - what does this mean if the tracker retrieval fails?
                    print("TRACKER RETRIEVAL FAILS")
                    print(e, flush=True)
                    raise e
                celeryapp.execute.send_task("tasks.tasks.do_task", args=[nextmessage], kwargs={}, queue=queue)
        print('task_success')
        print(task_success)
        return task_success

    def __task_management_message_handler(self, message_data):
        print("************************ MQUTILS MQLISTENER - TASK MANAGEMENT MESSAGE HANDLER *******************************")
        print('task management message')
        job_ticket_id = message_data.get('job_ticket_id')
        parent_job_ticket_id = message_data.get('parent_job_ticket_id', None)
        task_name = message_data.get('task_name')
        print('TASK NAME:')
        print(task_name)
        task_success = False

        #We want the task manager to watch the multi asset ingest jobs
        if (task_name == "multi_asset_ingest"):
            #Send a message to the task manager queue as long as this isn't the task manager message
            print("MULTI ASSET INGEST TASK")
            tm_message = mqutils.create_task_manager_queue_message(job_ticket_id, parent_job_ticket_id)
            print('sending tm message {} to queue {}'.format(tm_message, _tm_queue))
            # BROKEN
            celeryapp.execute.send_task("tasks.tasks.do_task", args=[tm_message], kwargs={}, queue=_tm_queue)

        try:
            job_tracker.set_job_status('running', job_ticket_id)
            # Run the service
            # Update timestamp file before do task
            print('BEFORE DO TASK UPDATING TIMESTAMP FILE job_ticket_id {}'.format(job_ticket_id))
            job_tracker.update_timestamp(job_ticket_id)
            print('CALLING DO TASK')
            print('job_ticket_id {} task_name {} category task_management'.format(job_ticket_id, task_name))
        except Exception as e:
            print(e)
            task_success = False

        # Call do task
        print("******************* CALLING WORKER API DO TASK __task_management_message_handler *******************")
        try:
            print("call_worker_api task_name {} job_ticket_id {} parent_job_ticket_id {} do_task")
            worker_response = call_worker_api(task_name, job_ticket_id, parent_job_ticket_id, 'do_task')
            print("worker_response")
            print(worker_response)
        except Exception as e:
            print(e)
            print("CALLING WORKER API DO TASK FAILED")
            task_success = False
            job_tracker.append_error(job_ticket_id, str(e), traceback.format_exc(), True)

        print("******************* HANDLE WORKER RESPONSE *******************")
        try:
            task_success = handle_worker_response(job_ticket_id, worker_response, parent_job_ticket_id)
        except Exception as e:
            print(e)
            print("HANDLE WORKER RESPONSE FAILED")
            task_success = False
            job_tracker.append_error(job_ticket_id, str(e), traceback.format_exc(), True)

        print("task_success")
        print(task_success)

        #Ack message was already handled above
        if (task_name == "multi_asset_ingest"):
            try:
                print("MORE MULTI ASSET INGEST STUFF HERE")
                job_status = job_tracker.get_job_status(job_ticket_id)
                if job_status == "failed":
                    print('JOB STATUS: FAILED')
                # Successful parent jobs will be handled by the task_manager's job monitor which periodically checks in-progress
                # jobs for stalled jobs or parent jobs where all children are complete. Upon successful completion of all child
                # jobs, the parent will be marked by that process as successful
            except Exception as e:
                job_tracker.append_error(job_ticket_id, f"Exception {str(e)} in job {job_ticket_id}", traceback.format_exc(), True)

            return None
        return task_success


    def __service_message_handler(self, message_data):
        print('services message')
        return True

    def __cache_management_message_handler(self, message_data, message_id):
        print('cache management message')
        try:
            worker_response = call_worker_api('update_cache')
        except Exception as e:
            import traceback;
            print('Failure in cache management handler')
            print(traceback.format_exc(), flush=True)
            # print('Nack message_id {}'.format(message_id))
            # self.conn.nack(message_id, self._sub_id)
            # TODO: HOW DO WE NACK IN CELERY?
            return False
        return True

# Generalized listener based on MQListener for use with components that do not use jobtracker
# If a next queue is returned from do_task, will place the same message it received on the specified queue
class GenericMessageHandler():
    def __init__(self, message, worker_endpoint='do_task'):
        self.message = message
        self.worker_endpoint = worker_endpoint

    def handle_message(self):
        print('received a message headers "%s"' % self.message)
        task_success = False

        task_success = self.__generic_message_handler(self.message, self.worker_endpoint)

        # #Sometimes the ack/nack might be sent in the handler
        if (task_success != None):
            if not task_success:
                print('Task unsuccessful')
                # TODO: HOW TO NACK A TASK?
        # print('processed message message_id {}'.format(message_id), flush=True)

    def __generic_message_handler(self, message_data, worker_endpoint):
        print("************************ MQUTILS MQLISTENER - GENERIC_MESSAGE_HANDLER *******************************")
        task_success = False

        # Call task
        try:
            worker_response = call_generic_worker_api(message_data, worker_endpoint)
            next_queue = os.getenv('NEXT_QUEUE')
            task_success = True if worker_response.get('success') else False
            print("SUCCESS IN WORKER RESPONSE TRY BLOCK")
        except Exception as e:
            print(e)
            task_success = False

        if (task_success):
            # Update timestamp file after task is complete
            if next_queue is None:
                #There are no more items to queue so the job is actually finished.
                print('******** LAST TASK COMPLETED ********')
            else:
                print('******** TASK COMPLETED - GOING TO NEXT QUEUE ********')
                celeryapp.execute.send_task("tasks.tasks.do_task", args=[self.message], kwargs={}, queue=next_queue)
        print('task_success')
        print(task_success)
        return task_success

# NOTIFY_SUB=2
# DLQ_SUB=3
# recipient_separators = re.compile(r'[,;]')
# class NotificationListener(stomp.ConnectionListener):
#     def __init__(self, conn):
#         self.conn = conn

#     def on_disconnected(self):
#         print('disconnected: reconnecting...')
#         connect_and_subscribe(self.conn, NOTIFY_QUEUE, sub_id=NOTIFY_SUB)
#         connect_and_subscribe(self.conn, DLQ_QUEUE, sub_id=DLQ_SUB)

#     def handle_direct_notification(self, frame):
#         print("Handling message from notification queue")
#         message = json.loads(frame.body)

#         if not 'to' in message:
#             message['to'] = [NOTIFY_DEFAULT_EMAIL]

#         if message['method'] == "email":
#             print("Method is email", flush=True)
#             if isinstance(message['to'], str):
#                 message['to'] = recipient_separators.split(message['to'])
#             msg = dedent(f"""\
#             From: {message['from']}
#             Subject: {message['subject']}

#             """) + message["message"]

#             print(f"Sending mail to {message['to']} via {NOTIFY_MAIL_RELAY}")
#             with smtplib.SMTP(NOTIFY_MAIL_RELAY) as smtp:
#                 try:
#                     result = smtp.sendmail(
#                         from_addr='no-reply@iiif.harvard.edu',
#                         to_addrs=message['to'],
#                         msg = msg
#                     )
#                 except Exception as e:
#                     print(f"Sendmail failed with exception {e}")
#                     import traceback
#                     print(traceback.format_exc())
#                 print(f"Result of sendmail: {result}", flush=True)
#         else:
#             raise RuntimeError('Unknown method for notification')


#     def handle_dlq(self, frame):
#         print('Handling DLQ notification')
#         message = json.loads(frame.body)
#         job_ticket_id = message_data.get('job_ticket_id')
#         parent_job_ticket_id = message_data.get('parent_job_ticket_id', None)
#         tracker_doc = job_tracker.get_tracker_doc(job_ticket_id, parent_job_ticket_id)
#         parent_suffix = f" with Parent Job: {parent_job_ticket_id}" if parent_job_ticket_id else ""
#         msg = dedent(f"""\
#         From: IIIF Notifier <no-reply@iiif.harvard.edu>
#         Subject: Job: {job_ticket_id}{parent_suffix}

#         Job {job_ticket_id}{parent_suffix} has failed.

#         Job tracker file contents follow.

#         """) + json.dumps(tracker_doc)
#         with smtplib.SMTP(NOTIFY_MAIL_RELAY) as smtp:
#             try:
#                 result = smtp.sendmail(
#                     from_addr='no-reply@iiif.harvard.edu',
#                     to_addrs=[NOTIFY_DEFAULT_EMAIL],
#                     msg = msg
#                 )
#             except Exception as e:
#                 print(f"Sendmail failed with exception {e}")
#                 import traceback
#                 print(traceback.format_exc())
#                 raise(e)
#             print(f"Result of sendmail: {result}", flush=True)

#     def on_message(self, frame):
#         headers, body = frame.headers, frame.body
#         message_id = headers.get('message-id')
#         sub_id = int(headers.get('subscription'))
#         print(f'handling message {message_id} from sub {sub_id}')
#         try:
#             if sub_id == NOTIFY_SUB:
#                 print('received direct notification')
#                 self.handle_direct_notification(frame)
#             elif sub_id == DLQ_SUB:
#                 print('received DLQ notification')
#                 self.handle_dlq(frame)
#             else:
#                 raise RuntimeError(f"sub_id {sub_id} is unknown")
#         except Exception as e:
#             self.conn.nack(message_id, sub_id)
#             raise(e)
#         self.conn.ack(message_id, sub_id)

#     def on_error(self, frame):
#         print('received an error "%s"' % frame.body)


# def initialize_mqlistener():
#     if _failback_host and _failback_port:
#         print('failback host and port in use')
#         conn = stomp.Connection([(_host, _port),(_failback_host, _failback_port)], heartbeats=(40000, 40000), keepalive=True)
#     else:
#         print('failback host and port not in use')
#         conn = stomp.Connection([(_host, _port)], heartbeats=(40000, 40000), keepalive=True)
#     conn.set_listener('', MqListener(conn))
#     connect_and_subscribe(conn)
#     # http_clients://github.com/jasonrbriggs/stomp.py/issues/206
#     while True:
#         time.sleep(2)
#         if not conn.is_connected():
#             print('Disconnected in loop, reconnecting')
#             connect_and_subscribe(conn)

# def initialize_generic_listener(worker_endpoint='do_task'):
#     if _failback_host and _failback_port:
#         print('failback host and port in use', flush=True)
#         conn = stomp.Connection([(_host, _port),(_failback_host, _failback_port)], heartbeats=(40000, 40000), keepalive=True)
#     else:
#         print('failback host and port not in use', flush=True)
#         conn = stomp.Connection([(_host, _port)], heartbeats=(40000, 40000), keepalive=True)
#     conn.set_listener('', GenericListener(conn, worker_endpoint))
#     conn_list.append(conn)
#     connect_and_subscribe(conn)
#     # http_clients://github.com/jasonrbriggs/stomp.py/issues/206
#     while True:
#         time.sleep(2)
#         if not conn.is_connected():
#             print('Disconnected in loop, reconnecting', flush=True)
#             connect_and_subscribe(conn)

# def initialize_notify_listener():
#     if _failback_host and _failback_port:
#         print('failback host and port in use')
#         conn = stomp.Connection([(_host, _port),(_failback_host, _failback_port)], heartbeats=(40000, 40000), keepalive=True)
#     else:
#         print('failback host and port not in use')
#         conn = stomp.Connection([(_host, _port)], heartbeats=(40000, 40000), keepalive=True)
#     conn.set_listener('', NotificationListener(conn))
#     connect_and_subscribe(conn, NOTIFY_QUEUE, sub_id=NOTIFY_SUB)
#     connect_and_subscribe(conn, DLQ_QUEUE, sub_id=DLQ_SUB)
#     # http_clients://github.com/jasonrbriggs/stomp.py/issues/206
#     while True:
#         time.sleep(2)
#         if not conn.is_connected():
#             print('Disconnected in loop, reconnecting')
#             connect_and_subscribe(conn, NOTIFY_QUEUE, sub_id=NOTIFY_SUB)
#             connect_and_subscribe(conn, DLQ_QUEUE, sub_id=DLQ_SUB)
