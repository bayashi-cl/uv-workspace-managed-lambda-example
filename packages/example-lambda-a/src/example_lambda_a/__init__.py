from typing import Any

import boto3

import example_common


def lambda_handler(event: Any, context: Any) -> str:
    lambda_ = boto3.client("lambda")
    lambda_.invoke(
        FunctionName="example-lambda-b",
        InvocationType="Event",
        Payload=example_common.ExampleDto(message="from a").model_dump_json(),
    )

    return "done"
