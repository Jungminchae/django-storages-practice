from django.urls import path
from samples.views import SampleCreateView

urlpatterns = [
    path("", SampleCreateView.as_view(), name="sample-create"),
]
