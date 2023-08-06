from typing import List, Optional

from stxsdk.typings import DataType, FailureResponse, SuccessResponse


def format_failure_response(
    errors: List[str], message: Optional[str] = None
) -> FailureResponse:
    return FailureResponse(
        success=False, data=None, errors=errors, message=message or "Request Failed"
    )


def format_success_response(
    data: DataType, message: Optional[str] = None
) -> SuccessResponse:
    return SuccessResponse(
        success=True,
        data=data,
        errors=None,
        message=message or "Request Processed Successfully",
    )
