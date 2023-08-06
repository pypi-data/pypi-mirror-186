from fastapi.responses import JSONResponse

GENERAL_ERROR = 'GENERAL_ERROR'
GENERAL_ERROR_MESSAGE = 'Something is wrong.'

def create_error(code: str=GENERAL_ERROR, message: str=GENERAL_ERROR_MESSAGE, exception: Exception = None):
    return {
        'error' : {
            'code': code,
            'message': message,
            'exception': str(exception) 
        }
    }

class BaseError(JSONResponse):
    pass

class BookingNotFound(BaseError):
    code = 'BOOKING_NOT_FOUND'
    message = 'Booking id {BOOKING_ID} does not exists.'
    def __init__(self, booking_id=None):
        super().__init__(content={
            'error': {
                'code': self.code,
                'message': self.message,
                'BOOKING_ID': booking_id
            }
        })

class BookingStatusError(BaseError):
    code = 'BOOKING_STATUS_ERROR'
    message = 'Action cannot be performed on booking {BOOKING_ID} when its status is {BOOKING_STATUS}.'
    def __init__(self, booking_id=None, booking_status=''):
        super().__init__(content={
            'error': {
                'code': self.code,
                'message': self.message,
                'BOOKING_ID': booking_id,
                'BOOKING_STATUS': booking_status,
            }
        })

class BookingTimeout(BaseError):
    code = 'BOOKING_TIMEOUT'
    message = 'Request timed out, please try again later.'
    def __init__(self):
        super().__init__(content={
            'error': {
                'code': self.code,
                'message': self.message,
            }
        })

class BookingRequestError(BaseError):
    code = 'BOOKING_REQUEST_ERROR'
    message = 'Booking request error.'
    def __init__(self, ex=None):
        super().__init__(content={
            'error': {
                'code': self.code,
                'message': self.message,
                'exception': str(ex)
            }
        })
