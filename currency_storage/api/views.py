from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from currencies.models import Currency
from .serializers import CurrencySerializer


class CurrenciesViewSet(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = LimitOffsetPagination


class CyrrencyViewSet(generics.RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
