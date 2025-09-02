from rest_framework.views import APIView

from service.constants import ResponseMessages
from service.utils import CustomResponseHandler


class HealthCheckView(APIView):
    def get(self, request, *args, **kwargs):
        """
        Health check endpoint to verify if the service is up and running.
        """
        return CustomResponseHandler(
            message=ResponseMessages.SERVICE_UP
        )
