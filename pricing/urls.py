from django.urls import path
from .views import PricingListView, PricingSelectView

urlpatterns = [
    path("", PricingListView.as_view(), name="pricing_list"),
    path("select/", PricingSelectView.as_view(), name="pricing_detail"),
]
