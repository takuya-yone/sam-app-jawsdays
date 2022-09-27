import json
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer
from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit

tracer = Tracer()
logger = Logger()
metrics = Metrics(
    namespace="sam-app-jawsdays",
    service="HelloWorldFunction")

@metrics.log_metrics
@tracer.capture_lambda_handler
@logger.inject_lambda_context(log_event=False)
def lambda_handler(event, context):

    # Powertools Logger
    logger.info('aiueo')

    # Add Metic
    metrics.add_metric(
        name="CallCount",
        unit=MetricUnit.Count,
        value=1)

    # Return Response
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }
