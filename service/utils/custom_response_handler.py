from rest_framework.response import Response

from service.constants import ResponseStatuses


class CustomResponseHandler(Response):
    
    def __init__(self, data=None, success=True, status=ResponseStatuses.OK,
                message=None, meta=None, 
                headers=None,errors=None, content_type=None):
        
        response_data = {
            'success': success
        }
        
        if data is not None:
            response_data['data'] = data
        if message:
            response_data['message'] = message
        if meta:
            response_data['meta'] = meta
        if errors:
            response_data['errors'] = errors
        super().__init__(response_data, status=status, headers=headers,
                        content_type=content_type)
