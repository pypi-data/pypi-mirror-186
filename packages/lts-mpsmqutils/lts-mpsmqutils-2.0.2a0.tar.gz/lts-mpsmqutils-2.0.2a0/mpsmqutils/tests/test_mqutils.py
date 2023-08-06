import sys, os, pytest, logging
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import mqutils as mqutils
import mqlistener as mqlistener

import mpsjobtracker.trackers.jobtracker as jobtracker
job_tracker = jobtracker.JobTracker()
logging.basicConfig(format='%(message)s')

class TestMqUtils():
    """
    To run these tests, run the pytest command:
    python -m pytest

    Test filename must start with "test_"
    Test class name must start with "Test"
    Test method name must start with "test_"
    """
    mq_conn = None

    def test_get_mq_connection(self):
        TestMqUtils.mq_conn = mqutils.get_mq_connection()
        assert TestMqUtils.mq_conn is not None

    def test_call_worker_api_fail(self):
        '''This expects an active MQ instance to be running and the credentials created in the .env
            1. Creates a parent directory with tracker file to represent the multi-asset worker parent directory
            2. Creates a child directory and tracker file with the relevant image context
            3. Attempts to send a fake api call (which will fail)
        The test is successful if:
            1. An inprocess directory is created in the jobs directory with a parent and child directory
                and their corresponding tracker files
            2. The 'call_worker_api' call should throw an exception (handled by the pytest.raises(Exception)
            3. The child tracker file should show a status of 'failed'
        '''
        with pytest.raises(Exception):
            #Create the parent directory which represents the multi-asset worker
            parent_tracker_file = job_tracker.init_tracker_file('assets', context)
            parent_job_ticket_id = parent_tracker_file['job_ticket_id']

            image_context = context["assets"]["image"][0]
            child_tracker_file = job_tracker.init_tracker_file('assets', image_context, parent_job_ticket_id)
            child_job_ticket_id = child_tracker_file['job_ticket_id']
            child_tracker_dir = job_tracker.get_job_directory(child_job_ticket_id, parent_job_ticket_id)

            mqlistener.call_worker_api("task_name", child_job_ticket_id, parent_job_ticket_id, 'do_task', "http://dummy-link.com")
            tracker_file = job_tracker.get_tracker_file(child_job_ticket_id, parent_job_ticket_id)
            assert tracker_file is not None
            assert tracker_file['job_management']['job_status'] == "failed"

context = {
          "globalSettings": {
            "actionDefault": "update"
          },
          "metadata": {},
          "assets": {
            "audio": [],
            "video": [],
            "text": [],
            "image": [
              {
                "action": "create",
                "sourceSystemId": "4827718",
                "storageSrcKey": "sampleimage1.jp2",
                "storageDestKey": "sampleimage1.jp2",
                "storageSrcPath": "iiif-mps-dev",
                "thumbSizes": [
                  150,
                  300
                ],
                "identifier": "URN-3:IIIF_DEMO:10004",
                "space": "testspace",
                "createdByAgent": "testagent",
                "createDate": "2021-02-11 17:56:09",
                "lastModifiedByAgent": "testagent",
                "lastModifiedDate": "2021-02-11 17:56:09",
                "status": "ACTIVE",
                "storageTier": "s3",
                "iiifApiVersion": "2",
                "assetLocation": "DRS",
                "mediaType": "image",
                "policyDefinition": {
                  "policy": {
                    "authenticated": {
                      "height": 2400,
                      "width": 2400
                    },
                    "public": {
                      "height": 1200,
                      "width": 1200
                    }
                  },
                  "thumbnail": {
                    "authenticated": {
                      "height": 250,
                      "width": 250
                    },
                    "public": {
                      "height": 250,
                      "width": 250
                    }
                  }
                },
                "assetMetadata": [
                  {
                    "fieldName": "admin",
                    "jsonValue": {
                      "name": "Hello there!",
                      "description": "A test description",
                      "type": "Standard",
                      "pages": "120",
                      "rating": "10",
                      "shelf": "1A",
                      "case": "Cabinet 1"
                    }
                  }
                ]
              }
            ]
          }
}
