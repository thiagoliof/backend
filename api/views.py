from rest_framework import generics
from .serializers import TimeSerializer
from .models import Time

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Time.objects.all()
    serializer_class = TimeSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = Time.objects.all()
    serializer_class = TimeSerializer