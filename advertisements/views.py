from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Advertisement as Adv
from .serializers import AdvertisementSerializer as AdvSerializer
from .filters import AdvertisementFilter

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Adv.objects.all()
    serializer_class = AdvSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []
