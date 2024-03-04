from rest_framework import generics
from currencies.models import Currency
from .serializers import CurrencySerializer
from rest_framework.pagination import LimitOffsetPagination


class CurrenciesViewSet(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = LimitOffsetPagination


class CyrrencyViewSet(generics.RetrieveAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
