import logging

import botocore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def get_regions(self):
    logger.info(" ---Inside utils :: get_regions()--- ")
    """Summary

    Returns:
        TYPE: Description
    """

    client = self.session.client('ec2', region_name='us-east-1')
    region_response = {}
    try:
        region_response = client.describe_regions()
    except botocore.exceptions.ClientError as error:
        if error.response['Error']['Code'] == 'AuthFailure':
            logger.error(f" AccessKey credentails not found here: {error}")
            exit(1)
    except botocore.exceptions.NoCredentialsError as e:
        logger.error(f" Unable to locate credentials: {e} ")
        exit(1)

    regions = [region['RegionName'] for region in region_response['Regions']]
    return regions


# returns the list of lambda functions
def list_lambda_functions(client) -> dict:
    """
    :param client:
    :param self:
    :return:
    """
    logger.info(" ---Inside lambdafn.utils :: list_lambda_functions")

    function_lst = []

    marker = ''
    while True:
        if marker == '' or marker is None:
            response = client.list_functions()
        else:
            response = client.list_functions(
                Marker=marker
            )
        for fn in response['Functions']:
            function_lst.append(fn)

        try:
            marker = response['NextMarker']
            if marker == '':
                break
        except KeyError:
            break

    return function_lst

