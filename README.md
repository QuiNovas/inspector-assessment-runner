# inspector-assessment-runner
AWS Lambda function that runs an AWS Inspector assessment

This function runs on any event passed to it and starts an Inspector assessment run.

## Environment Variables
- `ASSESSMENT_TEMPLATE_ARN` - **REQUIRED** - the Inspector Assessment Template ARN to run
- `RUN_NAME_PREFIX` - **OPTIONAL** The prefix name to apply to the assessment runs. This will be postfixed with the date/time. If not present, just the date/time will be used. 