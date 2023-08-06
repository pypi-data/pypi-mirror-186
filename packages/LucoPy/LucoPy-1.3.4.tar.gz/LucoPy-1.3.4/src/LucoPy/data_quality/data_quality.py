import json
import copy

class CheckResult:

    def __init__(self, results):
        self.results = results

        # Set Collection attributes from results
        # Required - will throw exception if not present
        required_args = ['check', 'success']
        for k in required_args:
            if k not in results:
                raise Exception(f'Required arg not present: {k}')

        for k, v in results.items():
            setattr(self, k, v)

    def __str__(self):
        return json.dumps(self.results, indent=2)

    def to_json_dict(self):
        return self.results

    def is_exception_thrown(self):

        try:
            if not self.success and self.results['onFail']['Action'].lower() == 'fail':
                return True
        except KeyError:
            pass

        return False

class CollectionResult:

    def __init__(self, results):
        self.__results_dict = copy.deepcopy(results)
        self.results = results
        self.results['checks'] = self.__build_checks(results['checks'])

        # Set Collection attributes from results
        # Required - will throw exception if not present
        required_args = ['checks']
        for k in required_args:
            if k not in results:
                # TODO: return all missing required args
                raise Exception(f'Required arg not present: {k}')

        for k, v in results.items():
            setattr(self, k, v)

    def __str__(self):
        return json.dumps(self.__results_dict, indent=2)

    def __build_checks(self, checks):

        checks_objs = []

        for check_results in checks:
            checks_objs.append(CheckResult(check_results))

        return checks_objs

    def to_json_dict(self):
        return self.__results_dict

    def is_exception_thrown(self, error_on_fail=True):
        """
        Checks the success of each check. Returns True if any checks fail and have 'Action': 'fail'
        in the onFail field. Always returns False if error_on_fail is False.
        """
        if error_on_fail:
            failed_checks = [check.is_exception_thrown() for check in self.checks]

            if True in failed_checks:
                return True

        return False