from fastapi import status

class AppError(Exception):
    def __init__(
        self, 
        message, 
        code,
        status_code,
        errors = None
    ):
        super().__init__(message)
        self.message = message
        self.code = code
        self.status_code = status_code
        self.details = {"errors": errors}

def app_error(message, errors = None):
    return AppError(
        message=message,
        code="internal_error",
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        errors=errors,
    )

def business_error(message, errors = None):
    return AppError(
        message=message,
        code="business_error",
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        errors=errors,
    )

def validation_error(message, errors = None):
    return AppError(
        message=message,
        code="validation_error",
        status_code=status.HTTP_412_PRECONDITION_FAILED,
        errors=errors
    )

def not_found_error(message, errors = None):
    return AppError(
        message=message,
        code="not_found",
        status_code=status.HTTP_404_NOT_FOUND,
        errors=errors
    )
