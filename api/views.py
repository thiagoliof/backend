from rest_framework import generics
from .serializers import TimeSerializer, PrimeiraFaseSerializer
from .models import Time, PrimeiraFase

class CreateTimeView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsTimeView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Time.objects.all()
    serializer_class = CreateTimeView




class CreatePrimeiraFaseView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = PrimeiraFase.objects.all()
    serializer_class = PrimeiraFaseSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsPrimeiraFaseView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = PrimeiraFase.objects.all()
    serializer_class = CreatePrimeiraFaseView