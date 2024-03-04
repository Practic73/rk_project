from django.urls import include, path

from .views import CurrenciesViewSet, CyrrencyViewSet

urlpatterns = [
    path('v1/currencies/', CurrenciesViewSet.as_view(), name='currencies'),
    path('v1/currency/<int:pk>', CyrrencyViewSet.as_view()),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
