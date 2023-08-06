import urllib
import logging
import json

logger = logging.getLogger(__name__)
logging.getLogger().setLevel(logging.DEBUG)

from .ApiCore import ApiCore
from .Submissions import Submission
from .api_helpers import _build_slot_sequence_dict

class LucoApi:
    """
    This class acts as the user gateway to the API.
    Authentication is handled behind the scenes by the ApiCore class so that 
    access tokens can be shared by multiple API calls.
    """
    def __init__(self, base_url, tenant_id=None, client_id=None, client_secret=None, 
                 resource_id=None, identity=None, timeout=20, log=False):

        self.config = {'base_url': base_url,
                       'tenant_id': tenant_id,
                       'client_id': client_id,
                       'client_secret': client_secret,
                       'resource_id': resource_id}

        if log:
            file_handler = logging.FileHandler('log.txt', mode='w')
            formatter = logging.Formatter('%(name)s : %(levelname)s : %(message)s')
            file_handler.setFormatter(formatter)
            logging.getLogger().addHandler(file_handler)
        else:
            logging.getLogger().addHandler(logging.NullHandler())

        self.core = ApiCore(self.config, timeout, identity)

        self.slot_sequence_error = f'Slot sequence not defined correctly.'

    def find_slotId(self, date, slotSequence):
        """
        Deprecated: Please use find_slot_id()
        """
        return self.find_slot_id(date, slotSequence)

    def find_slot_id(self, tag=None, slot_sequence=None):
        """
        Find slot id from a tag/date and slot sequence definition.

        Args:
            tag (str) : Date (YYYY-MM-DD) for scheduled deliveries or Unique tag for unscheduled deliveries
            slot_sequence (dict or list of k:v pairs (dicts)) : list slot sequence definitions in form {'key': 'value'}.
                Order matters - this determines parameter position.

        Returns:
            slot_id (int)
        """
        
        if isinstance(slot_sequence, list):
            # Original list of dicts structure
            # Loop through slot_sequence and generate definition dicts.
            definitions = []
            position = 0
            for param in slot_sequence:
                if len(param) == 1:
                    for k, v in param.items():
                        definitions.append({'position': position,
                                            'key': k,
                                            'value': v})
                else:
                    raise Exception(self.slot_sequence_error)
                position += 1
        else:
            # Simple dictionary structure
            # Loop through slot_sequence and generate definition dicts.
            definitions = []
            position = 0
            for k, v in slot_sequence.items():
                definitions.append({'position': position,
                                    'key': k,
                                    'value': v})
                position += 1

        endpoint = f'/slots/search/'
                
        payload = urllib.parse.urlencode({'Tag': tag,
                                          'SlotSequenceDefinition': definitions}, doseq=True)

        r = self.core.get_request(endpoint, params=payload, allow_status=[404])
        
        if r.status_code == 404:
            slot_id = self.__create_unscheduled_slot(tag, definitions)
        else:
            r.raise_for_status()
            slot_id = r.json()['slotId']

        return slot_id

    def __create_unscheduled_slot(self, tag, slot_sequence):
        """
        If find_slot_id receives a 404 error code, this means a slot with the requested tag does
        not exist. In this case we use the POST /slots/ endpoint to create a new slot on the 
        slot sequence with the requested tag. 

        The slot id of the newly created slot is passed back to the user.
        """
        endpoint = '/slots/'

        payload = {'tag': str(tag),
                   'slotSequenceDefinition': slot_sequence}

        header = {'content-type': 'application/json-patch+json'}
        r = self.core.post_request(endpoint, additionalHeaders=header, data=json.dumps(payload))

        r.raise_for_status()

        return r.json()['slotId']

    def get_submission(self, slot_id, submission_id):
        """
        Returns a submission object representing an existing submission.
        
        Args:
            slot_id (int)
            submission_id (int)

        Returns:
            submission (Submission)
        """
        return Submission(slot_id, submission_id, self.core)

    def create_submission(self, slot_id, stage=None, run_environments=None):
        """
        Create a submission against a slot and return a Submission object representing it.
        
        Args:
            slot_id (int)
            stage (string) : None
            run_environment (dict or list of dicts) : None
        Returns:
            submission (Submission)
        """
        # Create new submission
        endpoint = f'/slots/{slot_id}/submissions'
        r = self.core.post_request(endpoint)
        r.raise_for_status()

        submission_id = r.json()['slotSubmissionId']

        # Get Submission object of newly created submission
        new_submission = self.get_submission(slot_id, submission_id)
        
        if stage and run_environments:
            new_submission.submit_run_environment(stage, run_environments)

        return new_submission

    def find_submission_in_slot_sequence(self, slot_id, submission_id, OnlyCompletedSubmissions=False, TimeDifference=None, FindClosest='historic'):
        """
        Returns a Slot and Submission ID and whether it is an exact match 
        based on the search criteria, and what the relative difference is 
        in terms of time and number of slots.

        endpoint: GET /slots/{slotId}/submissions/{submissionId}/search

        Args:
            slot_id (int)
            submission_id (int)
            OnlyCompletedSubmissions (bool)
            TimeDifference (str) : d:HH:MM:SS
            FindClosest (str) : historic, future, either or exact
            
        Returns:
            Response JSON (dict)
        """
        endpoint = f'/slots/{slot_id}/submissions/{submission_id}/search'

        payload = {'OnlyCompletedSubmissions': OnlyCompletedSubmissions,
                   'FindClosest': FindClosest}

        if TimeDifference:
            payload['TimeDifference'] = TimeDifference

        r = self.core.get_request(endpoint, params=payload)
        r.raise_for_status()

        return r.json()

    def find_submissions_by_slot_sequence(self, slotSequence, onlyLatestSlot=True, onlyDeliveredSlots=True, onlyCompletedSubmissions=True,
                                  onlyLatestSubmission=True, expectedAfterUtc=None, expectedBeforeUtc=None):
        """
        Returns submissions and their slots for a slot sequence

        endpoint: GET /slotsequences/submissions

        Args:
            slotSequence (list of k:v pairs (dicts))
            onlyLatestSlot (bool)
            onlyDeliveredSlots (bool)
            onlyCompletedSubmissions (bool)
            onlyLatestSubmission (bool)
            expectedAfterUtc (str) : YYYY-MM-DD or YYYY-MM-DDThh:mm:ss
            expectedBeforeUtc (str) : YYYY-MM-DD or YYYY-MM-DDThh:mm:ss
        """
        endpoint = f'/slotsequences/submissions'

        if isinstance(slotSequence, list):
            # Loop through slot_sequence and generate definition dicts.
            definitions = []
            position = 0
            for param in slotSequence:
                if len(param) == 1:
                    for k, v in param.items():
                        definitions.append({'position': position,
                                            'key': k,
                                            'value': v})
                else:
                    raise Exception(self.slot_sequence_error)
                position += 1
        else:
           # Loop through slot_sequence and generate definition dicts.
            definitions = []
            position = 0
            for k, v in slotSequence.items():
                definitions.append({'position': position,
                                    'key': k,
                                    'value': v})
                position += 1
        
        payload_dict = {'SlotSequenceDefinition': definitions,
                        'OnlyLatestSlot': onlyLatestSlot,
                        'OnlyDeliveredSlots': onlyDeliveredSlots,
                        'OnlyCompletedSubmissions': onlyCompletedSubmissions,
                        'OnlyLatestSubmission': onlyLatestSubmission}

        if expectedAfterUtc:
            payload_dict['ExpectedAfterUtc'] = expectedAfterUtc
        if expectedBeforeUtc:
            payload_dict['ExpectedBeforeUtc'] = expectedBeforeUtc

        payload = urllib.parse.urlencode(payload_dict, doseq=True)

        r = self.core.get_request(endpoint, params=payload)
        r.raise_for_status()

        return r.json()

    def find_latest_submission_by_slot_sequence(self, slotSequence, expectedAfterUtc=None, expectedBeforeUtc=None):
        """
        Accessory method to LucoApi.find_submissions_by_slot_sequence(). Returns the slot id and submission id of 
        the most recently completed submission on the slot sequence.

        Equivalent to: 
        
        find_submissions_by_slot_sequence(slotSequence, expectedAfterUtc=expectedAfterUtc, expectedBeforeUtc=expectedBeforeUtc)

        Where the response JSON is interpreted to only return the slot id and submission id.
        """
        r = self.find_submissions_by_slot_sequence(slotSequence, 
                expectedAfterUtc=expectedAfterUtc, expectedBeforeUtc=expectedBeforeUtc)

        slot_id = r['slots'][0]['slotId']
        submission_id = r['slots'][0]['submissions'][0]['slotSubmissionId']

        return slot_id, submission_id

    def submit_slot_sequences(self, slot_sequences, allow_overwrites=False, allow_archiving=False, ignore_delivery_config=False):
        """
        Submit slot sequence definitions to create a new slot sequence or update an existing slot sequence
        """

        # ensure slot_sequences is a list
        slot_sequences = [slot_sequences] if isinstance(slot_sequences, dict) else slot_sequences

        endpoint = f'/v2/slotsequences/import'

        payload = {
            'allowOverwrites': allow_overwrites,
            'allowArchiving': allow_archiving,
            'ignoreDeliveryConfig': ignore_delivery_config,
            'slotSequences': slot_sequences
        }

        header = {'content-type': 'application/json-patch+json'}
        r = self.core.post_request(endpoint, additionalHeaders=header, json=payload)

        response = r.json()

        counts = {'created': response['createdCount'],
                  'exists': response['existsCount'],
                  'notProcessed': response['notProcessedCount'],
                  'updated': response['updatedCount'],
                  'notUpdated': response['notUpdatedCount'],
                  'archived': response['archivedCount']}

        imports = response['slotSequenceImports']

        for ss_import in imports:
            ss_import['slotSequenceDefinition'] = _build_slot_sequence_dict(ss_import['slotSequenceDefinition'])

        results = {}
        results['counts'] = counts
        results['imports'] = imports

        return results