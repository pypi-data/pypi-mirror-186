import logging

from botocore.exceptions import ClientError

from OBP_monitoring.utils import list_lambda_functions

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# checks the compliance for lambda-inside-vpc
def lambda_concurrency_check(self, regions) -> dict:
    """
    :param self:
    :return:
    """
    logger.info(" ---Inside OBP Monitoring :: lambda_concurrency_check()")

    result = True
    failReason = ''
    offenders = []
    compliance_type = "lambda-concurrency-check"
    description = "Checks whether the AWS Lambda function is configured with function-level concurrent execution limit."
    resource_type = "AWS Lambda"
    risk_level = 'Medium'

    # regions = self.session.get_available_regions('lambda')

    for region in regions:
        try:
            client = self.session.client('lambda', region_name=region)
            function_lst = list_lambda_functions(client)

            for function in function_lst:
                try:
                    function_name = function['FunctionName']
                    # print(function_name)
                    function_concurrency = client.get_function_concurrency(FunctionName=function_name)
                    if 'ReservedConcurrentExecutions' not in function_concurrency:
                        raise KeyError

                except KeyError:
                    result = False
                    offenders.append(function['FunctionName'])
                    failReason = 'Lambda function is not configured with function-level concurrent execution limit.'

                except ClientError:
                    result = False
                    failReason = "Lambda function is not configured with function-level concurrent execution limit"
                    offenders.append(function['FunctionName'])
                    continue
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
