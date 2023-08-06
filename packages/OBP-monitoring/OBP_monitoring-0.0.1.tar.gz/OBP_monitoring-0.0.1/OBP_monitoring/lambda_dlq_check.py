import logging

from botocore.exceptions import ClientError

from OBP_monitoring.utils import list_lambda_functions

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def lambda_dlq_check(self, regions) -> dict:
    """
    :param regions:
    :param self:
    :return:
    """
    logger.info(" ---Inside lambdafn :: lambda_dlq_check()")

    result = True
    failReason = ''
    offenders = []
    compliance_type = "Lambda DLQ check"
    description = "Checks whether an AWS Lambda function is configured with a dead-letter queue."
    resource_type = "AWS Lambda"
    risk_level = 'Medium'

    # regions = self.session.get_available_regions('lambda')

    for region in regions:
        try:
            client = self.session.client('lambda', region_name=region)
            function_lst = list_lambda_functions(client)

            for function in function_lst:
                response = client.get_function_configuration(
                    FunctionName=function['FunctionName']
                )
                try:
                    dead_letter_arn = response['DeadLetterConfig']
                    if dead_letter_arn is None:
                        raise KeyError
                except KeyError:
                    result = False
                    offenders.append(function['FunctionName'])
                    failReason = 'Amazon Lambda function is not associated with a Dead-Letter Queue (DLQ)'

        except ClientError as e:
            logger.error("Something went wrong with the region {}: {}".format(region, e))

    return {
        'Result': result,
        'failReason': failReason,
        'resource_type': resource_type,
        'Offenders': offenders,
        'Compliance_type': compliance_type,
        'Description': description,
        'Risk Level': risk_level
    }