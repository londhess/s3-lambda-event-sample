#!/usr/bin/env python3

from aws_cdk import core

from s3_lambda_event_sample.s3_lambda_event_sample_stack import S3LambdaEventSampleStack


app = core.App()
S3LambdaEventSampleStack(app, "s3-lambda-event-sample",env={'region': 'ap-south-1'})

app.synth()
