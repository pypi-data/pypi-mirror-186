import logging
import botocore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# checks compliance.py for rds automatic minor version enabled
def rds_enhanced_monitoring_enabled(self, regions) -> dict:
    """

    :param self:
    :return dict: rds enhanced monitoring enabled compliance.py details
    """
    logger.info(" ---Inside rds :: rds_enhanced_monitoring_enabled()")

    result = True
    failReason = ''
    offenders = []
    compliance_type = "RDS instance enhanced monitoring enabled"
    description = "Checks if enhanced monitoring is enabled for RDS instances."
    resource_type = "RDS Instance"
    risk_level = 'Medium'

    # regions = self.session.get_available_regions('rds')

    for region in regions:
        try:
            client = self.session.client('rds', region_name=region)
            marker = ''
            while True:
                response = client.describe_db_instances(
                    MaxRecords=100,
                    Marker=marker
                )
                for instance in response['DBInstances']:
                    monitoring_interval = int(instance['MonitoringInterval'])
                    if monitoring_interval <= 0:
                        result = False
                        failReason = "enhanced monitoring is not enabled"
                        offenders.append(region + ': ' + instance['DBInstanceIdentifier'])

                try:
                    marker = response['Marker']
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
