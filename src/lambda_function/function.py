import boto3
import logging
import os
import time


def handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    inspector = boto3.client('inspector')

    logger.info('Starting Inspector run {}'.format(os.environ['ASSESSMENT_TEMPLATE_ARN']))
    run_name = '{}{}'.format(os.environ.get('RUN_NAME_PREFIX', ''), time.strftime('%Y-%m-%d %H:%M:%S'))
    inspector.start_assessment_run(
        assessmentTemplateArn=os.environ['ASSESSMENT_TEMPLATE_ARN'],
        assessmentRunName=run_name
    )
    logger.info('Started Inspector run {}'.format(run_name))

    return event
