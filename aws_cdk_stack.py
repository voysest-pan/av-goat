from constructs import Construct
from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_s3 as s3, 
    aws_sns_subscriptions as subs,
)


class AwsCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.bucket(self, "av-aws-cdk-bucket")

        #  queue = sqs.Queue(
        #    self, "AwsCdkQueue",
        #    visibility_timeout=Duration.seconds(300),
        # )

        # topic = sns.Topic(
        #    self, "AwsCdkTopic"
        # )
        #
        # topic.add_subscription(subs.SqsSubscription(queue))
