from typing import Any

import httpx

import example_common


def lambda_handler(event: dict[str, Any], context: Any) -> str:
    parsed_event = example_common.ExampleDto.model_validate(event)
    httpx.get("https://example.com")
    return parsed_event.message
