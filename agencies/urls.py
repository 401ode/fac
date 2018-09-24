from django.urls import path

from .views import FederalAgencyListView

urlpatterns = [
    # De facto default.
    path('', FederalAgencyListView.as_view(), name='feds'),
    path('federal/', FederalAgencyListView.as_view(), name='feds'),
]
