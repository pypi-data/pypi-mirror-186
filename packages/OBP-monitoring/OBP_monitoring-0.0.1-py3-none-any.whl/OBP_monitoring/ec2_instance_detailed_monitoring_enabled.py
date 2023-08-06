import botocore
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# checks compliance.py for ec2 instance detailed monitoring enabled
def ec2_instance_detailed_monitoring_enabled(self, regions) -> dict:
    """
    :param self:
    :return:
    """
    logger.info(" ---Inside ec2 :: ec2_instance_detailed_monitoring_enabled")

    result = True
    failReason = ''
    offenders = []
    compliance_type = "EC2 instance detailed monitoring enabled"
    description = "Checks if detailed monitoring is enabled for EC2 instances."
    resource_type = "EC2 Instance"
    risk_level = 'Low'

    # regions = self.session.get_available_regions('ec2')

    for region in regions:
        try:
            client = self.session.client('ec2', region_name=region)
            marker = ''
            while True:
                response = client.describe_instances(
                    MaxResults=1000,
                    NextToken=marker
                )
                if len(response['Reservations']) > 0:
                    for reservation in response['Reservations']:
                        for instance in reservation['Instances']:
                            monitoring = instance['Monitoring']['State']
                            if monitoring != 'enabled':
                                result = False
                                failReason = "Monitoring is not enabled in instances"
                                offenders.append(region+': '+instance['InstanceId'])

                try:
                    marker = response['NextToken']
                    if marker == '':
                        break
                except KeyError:
                    break
        except botocore.exceptions.ClientError as e:
            logger.error('Something went wrong with region {}: {}'.format(region, e))

    return {
        'Result': result,
        'failReason': failReason,
        'resource_type': resource_type,
        'Offenders': offenders,
        'Compliance_type': compliance_type,
        'Description': description,
        'Risk Level': risk_level
    }
