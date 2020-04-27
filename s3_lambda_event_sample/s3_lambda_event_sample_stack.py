from aws_cdk import (
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_s3_notifications as aws_s3_notifications,
    core)


class S3LambdaEventSampleStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define aws lambda function
        my_lambda = _lambda.Function(self,"HelloHandler",
                            runtime=_lambda.Runtime.PYTHON_3_7,
                            handler="hello.handler",
                            code=_lambda.Code.asset('lambda'))

        # Define S3 bucket
        my_bucket = s3.Bucket(self,"ssl-s3-lambda-event-raw")

        #Create the s3 notification objects which points to Lambda
        notification = aws_s3_notifications.LambdaDestination(my_lambda)

        #Add Filters if required
        filter1=s3.NotificationKeyFilter(prefix="home/")
        #Add event trigger from s3 to lambda
        my_bucket.add_event_notification(s3.EventType.OBJECT_CREATED,notification,filter1)