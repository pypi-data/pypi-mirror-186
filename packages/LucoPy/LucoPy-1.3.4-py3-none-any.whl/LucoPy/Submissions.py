import json
import logging
from .api_helpers import _build_slot_sequence_dict
from .data_quality import CheckResult, CollectionResult

log = logging.getLogger(__name__)

def _build_param_dict(paramGroupsJSON):
    """
    Utility method to collate slot parameters and slot parameter
    groups into a dictionary.
    """
    groups = {}
    for group in paramGroupsJSON:
        name = group['slotParameterGroupName']
        
        params = {}
        for param in group['slotParameters']:
            params[param['key']] = param['value']

        groups[name] = params

    return groups

class Submission:
    """
    This Submission class is associated with the v2 submission structure.

    Submission level functionality is handled through this class. Instances of this
    class are created using the LucoApi.get_submission() or LucoApi.create_submission() methods.
    """

    def __init__(self, slot_id, submission_id, core):
        self.slot_id = slot_id
        self.id = submission_id
        self.core = core
        self.__definitionJSON = None

    # Check if GET /slots/{slot_id}/submissions/{submission_id} has been called to 
    # get the submission JSON object.
    def __check_definition_exists(self):
        if not self.__definitionJSON:
            self.__update_definition()

    # Update JSON definition
    def __update_definition(self):
        endpoint = f'/v2/slots/{self.slot_id}/submissions/{self.id}'
        r = self.core.get_request(endpoint, params={'includeDelivery': True})
        r.raise_for_status()
        self.__definitionJSON = r.json()

    # The following @property decorated methods prevent the class from calling the api 
    # to get the submission JSON unless the call hasn't been made already.
    @property
    def type(self):
        self.__check_definition_exists()
        return self.__definitionJSON['slotSequence']['definition']['type']['slotSequenceTypeName']

    @property
    def expected_by(self):
        self.__check_definition_exists()
        return self.__definitionJSON['slot']['expectedBy']

    @property
    def name(self):
        self.__check_definition_exists()
        return _build_slot_sequence_dict(self.__definitionJSON['slotSequence']['definition']['name'])

    @property
    def status(self):
        self.__update_definition()
        return self.__definitionJSON['submission']['status']

    @property
    def start_time(self):
        self.__check_definition_exists()
        return self.__definitionJSON['submission']['startedOn']

    @property
    def end_time(self):
        self.__update_definition()
        return self.__definitionJSON['submission']['endedOn']

    @property
    def __param_groups(self):
        self.__check_definition_exists()
        return _build_param_dict(self.__definitionJSON['slotSequence']['parameters']['slotParameterGroups'])

    def params(self, group=None, key=None):
        """
        Search for slot parameters.

        Args:
        - group (str) : Parameter group to return
        - key (str) : Key within group to return the value of

        Returns:
        - result (dict or str)
        """
        if group:
            param_group = self.__param_groups[group]

            if key:
                return param_group[key]
            else:
                return param_group
        else:
            return self.__param_groups

    def get_delivery_schedule(self):
        """
        Return active delivery schedule. Works on assumption that there
        can only be one active schedule at a time.
        """
        self.__check_definition_exists()

        delivery_schedules = self.__definitionJSON['slotSequence']['delivery']

        for schedule in delivery_schedules:
            if schedule['isActive'] == True:
                return schedule

        # If there is no active schedule return None
        return None

    def get_metrics(self, stages=None, metrics=None):
        """
        Retrieve submission metrics
        
        Filter by stage and/or metric by passing strings or lists of strings

        Args:
            stages (string or list of strings)
            metrics (string or list of strings)

        Returns:
            metrics (dict or value)
        """
        endpoint = f'/slots/{self.slot_id}/submissions/{self.id}/metrics'

        payload = {}

        # Define payload
        if stages:
            if isinstance(stages, str):
                stages = [stages]
            payload['stages'] = stages

        if metrics:
            if isinstance(metrics, str):
                metrics = [metrics]
            payload['metrics'] = metrics

        r = self.core.get_request(endpoint, params=payload)
        r.raise_for_status()

        result = r.json()['slotSubmissionMetrics']

        # Restructure return format
        # Create list of all stages if None specified
        if not stages:
            stage_list = []
            for metric in result:
                if metric['stage'] not in stage_list:
                    stage_list.append(metric['stage'])
        else:
            stage_list = stages

        # Group metrics into dict per stage
        new_result = {k: {} for k in stage_list}
        for metric in result:
            if metric['stage'] in stage_list:
                new_result[metric['stage']].update({metric['metric']: metric['value']})

        # Refine to single stage/value if possible
        if stages and len(stages) == 1:
            if metrics and len(metrics) == 1:
                return new_result[stages[0]][metrics[0]]
            else:
                return new_result[stages[0]]
        else:
            return new_result

    def get_quality(self):
        """
        Retrieve quality results
        
        Returns:
            quality (dict)
        """
        endpoint = f'/v2/slots/{self.slot_id}/submissions/{self.id}/quality'

        r = self.core.get_request(endpoint)
        r.raise_for_status()

        response_json = r.json()

        for i, result in enumerate(response_json['qualityResults']):
            quality_results = json.loads(result['results'])
            response_json['qualityResults'][i]['results'] = quality_results

        return response_json

    def submit_run_environment(self, stage=None, run_environments=None):
        """
        Submit run environment details

        Args:
            stage (string) : Optional
            run_environments (dict or list of dicts) : Required

        Returns:
            response status (Bool) : Boolen success or failure       
        """
        endpoint = f'/slots/{self.slot_id}/submissions/{self.id}/runenvironment'

        if isinstance(run_environments, dict):
            run_environments = [run_environments]

        payload = {'stage': stage,
                   'runData': run_environments}

        header = {'content-type': 'application/json-patch+json'}
        r = self.core.post_request(endpoint, additionalHeaders=header, data=json.dumps(payload))
        r.raise_for_status()
        
        self.run_environments = run_environments

        return r.ok

    def submit_metrics(self, stage=None, runId=None, metric=None, value=None, metrics=None):
        """
        Submit metrics

        metrics : takes a dictionary of Metric:Value pairs.

        If only submitting one metric, you can use metric='metric' and value='value'
        """
        endpoint = f'/v2/slots/{self.slot_id}/submissions/{self.id}/metrics'

        if metric !=None and value != None:
            metrics_list = [{"metric": metric,
                             "value": value}]
        elif metrics:
            metrics_list = []
            for k, v in metrics.items():
                metrics_list.append({"metric": k,
                                     "value": v})
        else:
            raise Exception('Metric:Value pairs not provided correctly')

        payload = {'stage': stage,
                   'metrics': metrics_list}

        header = {'content-type': 'application/json-patch+json'}
        r = self.core.post_request(endpoint, additionalHeaders=header, data=json.dumps(payload))

        r.raise_for_status()
        return r.ok

    def __submit_quality_v1(self, stage=None, runId=None, tool=None, results=None, dataset=None, action=None):
        """
        Submit quality
        
        Essential: stage, tool, results and action.
        
        Dataset is optional, runId is no longer stored.
        """
        for param in [tool, results, action]:
            if not param:
                raise Exception('Please provide: tool, results and action')

        if isinstance(results, dict):
            results = json.dumps(results)

        endpoint = f'/slots/{self.slot_id}/submissions/{self.id}/quality'

        payload = {'stage': stage,
                   'runId': '',
                   'tool': tool,
                   'results': results,
                   'dataSet': dataset,
                   'action': action}

        header = {'content-type': 'application/json-patch+json'}
        r = self.core.post_request(endpoint, additionalHeaders=header, data=json.dumps(payload))

        r.raise_for_status()
        return r.ok

    def __submit_quality_v2(self, results, stage=None, action=None):
        """
        Submit quality results using the Luco DQ format.
        """

        endpoint = f'/v2/slots/{self.slot_id}/submissions/{self.id}/quality'

        params = {'stage': stage,
                  'action': action}

        header = {'content-type': 'application/json-patch+json'}

        r = self.core.post_request(endpoint, additionalHeaders=header, params=params, data=json.dumps(results))

        r.raise_for_status()
        return r.ok

    def submit_quality(self, stage=None, runId=None, tool=None, results=None, dataset=None, action=None):
        """
        Submit Data Quality results

        If using great_expectations format: stage, tool, results and action are required. Dataset is optional.

        If using Luco DQ format: results is required, stage and action are optional

        runId is no longer used in either case.
        """

        if isinstance(results, str) or isinstance(results, dict):
            if 'validation_result' in results:
                # Check if great_expectaions format and point to v1 endpoint
                r = self.__submit_quality_v1(stage, runId, tool, results, dataset, action)
            else:
                # If Luco DQ format, use v2 endpoint
                r = self.__submit_quality_v2(results, stage=stage, action=action)
        else:
            r = self.__submit_quality_v2(results.to_json_dict(), stage=stage, action=action)

        return r

    def submit_status(self, status, stage=None, runId=None, type=None, message=None, modified_by=None):
        """
        Submit the status of the Submission

        Args:
            runId       (str)
            status      (str)
            stage       (str)
            type        (str)
            message     (str)
            modified_by (str)

        Returns:
            response status (Bool) : Boolen success or failure
        """
        endpoint = f'/slots/{self.slot_id}/submissions/{self.id}/status'

        data = {'runId': '',
                'status': status,
                'stage' : stage,
                'type': type,
                'message': message,
                'modifiedBy': modified_by}

        header = {'content-type': 'application/json-patch+json'}
        r = self.core.post_request(endpoint, additionalHeaders=header, data=json.dumps(data))

        r.raise_for_status()
        return r.ok

    def submit_completed_status(self):
        """
        Submit a status for a completed submission.

        Equivalent to submit_status('Completed', 'Submission)
        """
        return self.submit_status('Completed', 'Submission')
