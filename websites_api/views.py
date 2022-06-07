from rest_framework.viewsets import ModelViewSet
from rest_framework_api_key.permissions import HasAPIKey

from websites_api.models import Website
from websites_api.serializers import WebsiteSerializer


class WebsiteViewSet(ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    lookup_field = 'code'
    permission_classes = [HasAPIKey]

