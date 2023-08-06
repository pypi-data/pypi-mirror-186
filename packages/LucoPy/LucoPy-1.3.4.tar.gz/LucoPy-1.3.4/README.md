# LucoPy

Python SDK to interact with the Luco API.

Contact: support@lu.co

---

## How to Use

Install the latest version from PyPI using PIP

```bash
pip install LucoPy
```

Or, specify a version

```bash
pip install LucoPy==x.x.x
```

Import the LucoApi class from the LucoPy library in your script and create an object of this class by passing in the API base url and the appropriate credentials. E.g.

```bash
from LucoPy import LucoApi

api = LucoApi(base_url, tenant_id, client_id, client_secret, resource_id)
```

---

## Authentication

In order to make calls to the API endpoints, LucoPy must be able to generate an authenticated access token. Authentication is managed by the ApiCore class using an identity provided during the instantiation of the LucoApi object.

### Azure Service Principal

If the Luco instance is hosted on Azure, a service principal can be used to authenticate to the API. In order to use a service principal, an App Registration must be created in the same Azure subscription as the Luco instance. The required credentials must then be passed as arguments to the LucoApi class when instantiating it. These credentials are:

- `tenant_id` - Directory (tenant) ID of the App Registration representing LucoPy
- `client_id` - Application (client) ID of the App Registration representing LucoPy
- `client_secret` - Secret value of the App Registration representing LucoPy
- `resource_id` - Application (client) ID of the target App Registration representing the API

### Other Identities

Any custom identity object can be passed into the LucoApi class via the `identity` kwarg when instantiating the LucoApi class. This idenity object must have a method called `generate_token()` which returns an access token validated to the API and the expiry datetime of this token.

---

### LucoApi Class

`LucoApi(base_url, tenant_id=None, client_id=None, client_secret=None, resource_id=None, identity=None, timeout=20, log=False)`

This class acts as the gateway to the Luco platform. An instance of this class should be created at the beginning of each script, API calls are then made through the ApiCore which handles the necessary authentication.

The base URL of the API instance must be passed as a parameter to this object along with the method of authentication.

The `timeout` option defines the maximum time (seconds) to wait for an HTTPS response from the API before causing a failure.

Use the `log` argument to turn logging on or off. Logs are generated and sent to a log.txt file in the base directory alongside where the script is being run.

1) `find_slot_id(tag, slot_sequence)`

    Find slot id from a tag/date and slot sequence definition. If the slot sequence does not have an active delivery schedule and a new tag is provided - a new slot will be created with this tag and the id of this slot will be returned.

    Args:
    - tag (str) : Date (YYYY-MM-DD) for scheduled deliveries or Unique tag for unscheduled deliveries
    - slot_sequence (dict or list of k:v pairs (dicts)) : list slot sequence definitions in form {'key': 'value'}.
            Order matters - this determines parameter position.

    Returns:
    - slot_id (int)

2) `get_submission(slot_id, submission_id)`

    Returns a submission object representing an existing submission.

    Args:
    - slot_id (int)
    - submission_id (int)

    Returns:
    - submission (Submission)

3) `create_submission(slot_id)`

    Create a submission against a slot and returns a Submission object representing it.

    Args:
    - slot_id (int)
    - stage (string) : None
    - run_environment (dict or list of dicts) : None

    Returns:
    - submission (Submission)

4) `find_submission_in_slot_sequence(slotId, submissionId, OnlyCompletedSubmissions=False, TimeDifference=None, FindClosest='historic')`

    Returns a Slot and Submission ID and whether it is an exact match based on the search criteria, and what the relative difference is in terms of time and number of slots.

    Args:
    - slot_id (int)
    - submission_id (int)
    - OnlyCompletedSubmissions (bool)
    - TimeDifference (str) : d:HH:MM:SS
    - FindClosest (str) : historic, future, either or exact

    Returns:
    - Response JSON (dict)

5) `find_submissions_by_slot_sequence(slotSequence, onlyLatestSlot=True, onlyDeliveredSlots=True, onlyCompletedSubmissions=True, onlyLatestSubmission=True, expectedAfterUtc=None, expectedBeforeUtc=None)`

    Returns submissions and their slots for a slot sequence

    Args:
    - slotSequence (dict or list of k:v pairs (dicts))
    - onlyLatestSlot (bool)
    - onlyDeliveredSlots (bool)
    - onlyCompletedSubmissions (bool)
    - onlyLatestSubmission (bool)
    - expectedAfterUtc (str) : YYYY-MM-DD or YYYY-MM-DDThh:mm:ss
    - expectedBeforeUtc (str) : YYYY-MM-DD or YYYY-MM-DDThh:mm:ss

    Returns:
    - Response JSON (dict)

6) `find_latest_submission_by_slot_sequence(slotSequence, expectedAfterUtc=None, expectedBeforeUtc=None)`

    Accessory method to find_submissions_by_slot_sequence(). Returns the slot id and submission id of the most recently completed submission on the slot sequence.

    Equivalent to:

    `find_submissions_by_slot_sequence(slotSequence, expectedAfterUtc=expectedAfterUtc, expectedBeforeUtc=expectedBeforeUtc)`

    Where the response JSON is interpreted to only return the slot id and submission id.

    Args:
    - slotSequence (dict or list of k:v pairs (dicts))
    - expectedAfterUtc (str) : YYYY-MM-DD or YYYY-MM-DDThh:mm:ss
    - expectedBeforeUtc (str) : YYYY-MM-DD or YYYY-MM-DDThh:mm:ss

    Returns:
    - slot_id (int), submission_id (int)

7) `submit_slot_sequences(slot_sequences, allow_overwrites=False, allow_archiving=False, ignore_delivery_config=False)`

    Import new or update existing slot sequences.

    Args:
    - slot_sequences (dict (JSON))
    - allow_overwrites (bool) : False
    - allow_overwrites (bool) : False
    - ignore_delivery_config (bool) : False

    Retuns:
    - results (dict)

### Submission Class

`Submission(slot_id, submission_id, core)`

Much of the functionality is handled at the Submission level. A Submission object is created by the `get_submission` or `create_submission` methods of the LucoApi class. These objects store the definition of the corresponding submission and handle methods relating to it.

1) `params(group=None, key=None)`

    Retrieve slot parameters. The `group` and `key` kwargs can be used to refine the response. Only use `key` in addition to `group`.

    Args:
    - group (str) : Parameter group to return
    - key (str) : Key within group to return the value of

    Returns:
    - result (dict or str)

2) `get_delivery_schedule()`

    Get the currently active delivery schedule. Retuns `None` if there are no active schedules .

    Returns:
    - delivery_schedule (dict)

3) `get_metrics(stages=None, metrics=None)`

    Retrieve metrics. Filter by stage and metric by passing strings or lists of strings.

    Args:
    - stages (string)
    - metrics (string)

    Returns:
    - metrics (dict)

4) `get_quality() --> dict`

    Retrieve quality results

    Returns:
    - quality (dict)

5) `submit_run_environment(stage=None, run_environments=None)`

    Submit run environment details

    Args:
    - stage (string) : Optional
    - run_environments (dict or list of dicts) : Required

    Returns:
    - response status (Bool) : Boolen success or failure

6) `submit_metrics(stage, metric=None, value=None, metrics=None)`

    Submit metrics by passing a dict of metric : value pairs to `metrics`. Option to pass a single metric : value pair using `metric` and `value`. It is recommended to use `metrics`.

    Args:
    - stage (str)
    - metric (str) : Metric key
    - value (str) : Value of metric
    - metrics (dict) : Dictionary of Metric : Value pairs.

    Returns:
    - response status (Bool) : Boolen success or failure

7) `submit_quality(stage, tool=None, results=None, dataset=None, action=None)`

    Submit quality results

    Args:
    - stage (str)
    - tool (str)
    - results (str)
    - dataset (str) : Optional
    - action (str)

    Returns:
    - response status (Bool) : Boolen success or failure

8) `submit_status(status, stage=None, type=None, message=None, modified_by=None)`

    Submit the status of the Submission

    Args:
    - status      (str)
    - stage       (str) : Optional
    - type        (str) : Optional
    - message     (str) : Optional
    - modified_by (str) : Optional

    Returns:
    - response status (Bool) : Boolen success or failure

9) `submit_completed_status()`

    Submit a status for a completed submission. Equivalent to:
    `submit_status('Completed', 'Submission')`

    Returns:
    - response status (Bool) : Boolen success or failure

---

## Data Quality

This data quality module provides functionality to support the handling of data quality results. This module will support the conversion of DQ results from a variety of tools into a consistent format which can be submitted to Luco. This generic format is based around the concepts of **checks** and **collections**.

A **collection** is a dictionary object with the following structure:

```json
{
    "name": "string",
    "tool": "string",
    "toolVersion": "1.2.3",
    "referenceUrl": "<some-url>",
    "checks": [
        {
            "check": "expect $col1 to not be null", // Required
            "checkArgs": {
                "col1": "Id"
            },
            "success": true, // Required
            "onFail": {
                "ignore": true,
                "failedRecordsLink": "<link-to-blob-storage>"
            },
            "observed": {
                "elementCount": 10,
                "failedPercentage": "10.0%"
            },
            "referenceUrl": "<some-url>",
            "tags": [
                "Completeness"
            ],
            "metadata": {}
        }
    ],
    "start": "2022-10-04 10:00:00",
    "end": "2022-10-04 10:10:00",
    "metadata": {}
}
```

Using the `Submission.submit_quality()` method, DQ results can be submitted as either a single **check** or as a **collection** of checks.

### Great Expectations

The `great_expectations` submodule supports the handling of validation results from running expectations and suites against a dataframe.

Utility functions are provided to convert the validations results into a shape supported by Luco:

```python
import LucoPy.data_quality.great_expectations.utils as ge_utils

check = ge_utils.convert_expectation_to_check(expectation)

check = ge_utils.convert_suite_to_collection(suite)
```

Where `expectation` and `suite` are the validation results as dict objects.

1) `convert_expectation_to_check(expectation_results, metadata_mappings={})`

    Convert an expectation validation result dict into a `CheckResult` object.

    Args:
    - expectation_results (dict) : Validation result dict
    - metadata_mappings (dict) : Custom mappings of key:value pairs in the `meta` field.

    Returns:
    - CheckResult

2) `convert_suite_to_collection(expectation_suite_results: dict, suite_mappings={}, expectation_mappings={})`

    Convert a suite validation result dict into a `CollectionResult` object.

    Args:
    - expectation_suite_results (dict) : Validation result dict
    - suite_mappings (dict) : Custom mappings of key:value pairs in the suite level `meta` field.
    - expectation_mappings (dict) : Custom mappings of key:value pairs in the expectation level `meta` fields.

    Returns:
    - CollectionResult

Data stored in the `meta` fields of the validation result objects can be mapped and then surfaced in the Luco UI. There are a number of *recognised fields* which Luco will detect and display differently to other metadata. The currently supported fields and their default custom mappings are:

Expectation Meta

| Recognised Field | Default Expected Name | Description |
|----------|----------|----------|
| onFail    | onFail    | Behaviour for when an expectation fails |
| referenceUrl   | referenceUrl    | URL linking to the expectation definition |
| tags   | tags    | Tags linked to the Data Quality Categories defined in Luco |

Expectation Suite Meta

| Recognised Field | Default Expected Name | Description |
|----------|----------|----------|
| toolVersion    | great_expectations_version    | Version of GE used |
| name    | expectation_suite_name    | Name of the expectation suite |
| start    | validation_time    | Datetime of when the validation was performed |
| referenceUrl   | referenceUrl    | URL linking to the expectation suite definition |
| tags   | tags    | Tags linked to the Data Quality Categories defined in Luco |

In order to implement custom mappings for these recognised fields, a dictionary of the custom mappings should be provided. E.g.

```python

# Keys should be the recognised fields
# Values should be the fields present in meta
expectation_mapping = {
    "onFail": "Action",
    "referenceUrl": "reference_url"
}

check = convert_expectation_to_check(expectation_result,
                                     metadata_mappings=expectation_mapping)
```

---

## Version History
LucoPy-1.3.4 : Bug fix: Default expectation result format to 'BASIC' so it doesn't need to be explicity defined.

LucoPy-1.3.3 : Update return format of Submission.get_metrics() method. Potential breaking change for users of the method.

LucoPy-1.3.2 : DQ module improvements. Bug fixes around string rendering of expectation configurations and observed values.

LucoPy-1.3.1 : DQ module improvements. New method CollectionResult.is_exception_thrown().

LucoPy-1.3.0 : DQ module improvements. Support expectation results in JSON or Expectation format.

LucoPy-1.2.9 : Improvement to great_expectations handing in DQ module. Remove need to convert validation results to dict.

LucoPy-1.2.8 : Bug fix type checking in Submission.submit_quality() method.

LucoPy-1.2.7 : Introduction of a data_quality module with support for great_expectations. Added support for slot sequences defined as a single dict rather than list of dicts.

LucoPy-1.2.6 : Expose submission start and end times as attributes of the Submission object.

LucoPy-1.2.5 : New method to get submission delivery schedule, improved error handling and Custom exceptions. Expose current submission status.

LucoPy-1.2.4 : Bug fix for Submission.submit_metrics to allow a value of zero and catch incorrectly provided metric: value pairs.

LucoPy-1.2.3 : New method to import slot sequences. Some minor quality of life updates.

LucoPy-1.2.2 : Bug fix around unscheduled slots. More informative error handling.

LucoPy-1.2.1 : Updated `find_slot_id` method to use new POST /slots/ endpoint to create unscheduled slots. No change to user.

LucoPy-1.2.0 : First version hosted on PyPI.

---
