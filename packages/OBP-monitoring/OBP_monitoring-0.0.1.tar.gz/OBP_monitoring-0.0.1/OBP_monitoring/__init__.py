from boto3 import session
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


__author__ = 'Klera DevOps'
__version__ = '0.0.1'


class aws_client:
    def __init__(self, **kwargs):
        if 'aws_access_key_id' in kwargs.keys() and 'aws_secret_access_key' in kwargs.keys():
            self.session = session.Session(
                aws_access_key_id=kwargs['aws_access_key_id'],
                aws_secret_access_key=kwargs['aws_secret_access_key'],
            )
        elif 'profile_name' in kwargs.keys():
            self.session = session.Session(profile_name=kwargs['profile_name'])

    from .lambda_concurrency_check import lambda_concurrency_check
    from .s3_event_notifications_enabled import s3_event_notifications_enabled
    from .asg_elb_healthcheck_required import asg_elb_healthcheck_required
    from .ec2_instance_detailed_monitoring_enabled import ec2_instance_detailed_monitoring_enabled
    from .guard_duty_enabled import guard_duty_enabled
    from .lambda_dlq_check import lambda_dlq_check
    from .rds_enhanced_monitoring_enabled import rds_enhanced_monitoring_enabled
    from .utils import get_regions

    def get_compliance(self) -> list:
        """
        :return:
        """
        regions = self.get_regions()
        compliance = [
            self.lambda_concurrency_check(regions),
            self.s3_event_notifications_enabled(),
            self.asg_elb_healthcheck_required(regions),
            self.ec2_instance_detailed_monitoring_enabled(regions),
            self.guard_duty_enabled(regions),
            self.lambda_dlq_check(regions),
            self.rds_enhanced_monitoring_enabled(regions),
        ]

        return compliance
