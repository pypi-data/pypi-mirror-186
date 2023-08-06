# sbcommons

Packages shared between different lambda functions

### 0.75
- Added subscription related events under klaviyo sub-module.
- Added KlaviyoClient method for getting all metrics and added an <end_ts> argument in the get_events() method, enabling to extract data from <since_ts> up to <end_ts> (i.e. extracting data for a specific time period).  

### 0.74
- Bug fixes in aws secrets

### 0.73
- Added a new UDF to the utils for all functions. To be able to evaluate to python objects.
- Also added to the secrets module to evaluate all return secrets from AWS

### 0.72
- Added decorator function that posts to SNS topic if the decorated function raises an exception. 

### 0.71
- Added new functionality to CRM client to be able to post events for a metric and also use translation entries

### 0.70
- Added a new function to get secrets from AWS. https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html

### 0.69
- Added utility class for sending messages to slack.

### 0.68
- Added new function to update events in a metric for Klayiyo Client

### 0.67
- Added abstract class crm.client and made Klaviyo and Symplify clients inherit from it.
- Added metric and event class under crm.klaviyo.
- Changed typing import in parse_utils, importing OrderedDict instead of MutableMapping.

### 0.66
- Fixed issue with RotatingFileHandler appending wrong suffixes to log file names.

### 0.65 - Deprecated
- Added the RotatingFileHandler class for time-rotating logging files.

### 0.64
- Minor bug fixes to allow for package dependencies

### 0.63
- Upgraded all the packages to python 3.9 packages

### 0.62

- Added parse_utils sub-module for parsing configuration files and other text files.
- Added an execute_query method to aws.redshift.RedshiftClient for performing select statements given a string parameter.
- Making teams into a utility class instead of a client

### 0.61 - Deprecated
- Added teams client
