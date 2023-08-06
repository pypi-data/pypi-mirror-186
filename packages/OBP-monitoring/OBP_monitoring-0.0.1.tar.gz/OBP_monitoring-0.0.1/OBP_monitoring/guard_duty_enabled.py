from botocore.exceptions import ClientError

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# check the compliance for guard duty enabled
def guard_duty_enabled(self, regions) -> dict:
    """
    :param regions:
    :param self:
    :return:
    """
    logger.info(" ---Inside guard_duty :: guard_duty_enabled()")

    result = True
    failReason = ''
    offenders = []
    compliance_type = "Guard Duty Enabled"
    description = "Checks if Amazon GuardDuty is enabled in your AWS account and region"
    resource_type = "Guard Duty"
    risk_level = 'Medium'

    # regions = self.session.get_available_regions('guardduty')

    for region in regions:
        try:
            client = self.session.client('guardduty', region_name=region)
            detectors = []
            marker = ''
            while True:
                if marker == '' or marker is None:
                    response = client.list_detectors()
                else:
                    response = client.list_detectors(
                        NextToken=marker
                    )
                detectors.extend(response['DetectorIds'])

                try:
                    marker = response['NextToken']
                    if marker == '':
                        break
                except KeyError:
                    break

            if len(detectors) <= 0:
                result = False
                failReason = "Guard duty is not enabled"

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