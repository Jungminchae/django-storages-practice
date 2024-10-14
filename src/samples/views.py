from rest_framework.generics import CreateAPIView
from samples.serializers import SampleSerializer
from samples.models import Sample


class SampleCreateView(CreateAPIView):
    serializer_class = SampleSerializer
    queryset = Sample.objects.all()
