import logging

import botocore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def asg_elb_healthcheck_required(self, regions) -> dict:
    """
    :param self:
    :return dict:
    """
    logger.info(" ---Inside autoscaling :: asg_elb_healthcheck_required()")

    result = True
    failReason = ''
    offenders = []
    compliance_type = "AutoScaling Group ELB health check required"
    description = "Checks if ELB health check is enabled on autoscaling group"
    resource_type = "Auto Scaling Group"
    risk_level = 'Medium'

    # regions = self.session.get_available_regions('autoscaling')

    for region in regions:
        try:
            client = self.session.client('autoscaling', region_name=region)
            marker = ''
            while True:
                if marker == '':
                    response = client.describe_auto_scaling_groups(
                        MaxRecords=100
                    )
                else:
                    response = client.describe_auto_scaling_groups(
                        NextToken=marker,
                        MaxRecords=100
                    )
                for asg in response['AutoScalingGroups']:
                    if asg['HealthCheckType'] != 'ELB':
                        result = False
                        offenders.append(asg['AutoScalingGroupName'])
                        failReason = 'Health check type in autoscaling group is not ELB'

                try:
                    marker = response['NextToken']
                    if marker == '':
                        break
                except KeyError:
                    break
        except botocore.exceptions.ClientError:
            pass

    return {
        'Result': result,
        'failReason': failReason,
        'resource_type': resource_type,
        'Offenders': offenders,
        'Compliance_type': compliance_type,
        'Description': description,
        'Risk Level': risk_level
    }
