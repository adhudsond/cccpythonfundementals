# Define custom exceptions
class InvalidDataError(Exception):
    """Raised when data validation fails"""
    pass
class ProcessingError(Exception):
    """Raised during data processing"""
    pass
# Use custom exceptions
def process_data(data):
    if data is None:
        raise InvalidDataError('Data cannot be None')
    if len(data) == 0:
        raise InvalidDataError('Data cannot be empty')
    # Process...
    return process_data
# Clear, specific error types!