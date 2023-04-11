from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.task2.models import Review, Service
from apps.task2.permissions import ReviewUserOrReadOnly
from apps.task2.serializers import ReviewSerializer, ServiceSerializer


# Create your views here.

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        service = Service.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(service=service, review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this service!!!")
        if service.number_rating == 0:
            service.avg_rating = serializer.validated_data['rating']
        else:
            service.avg_rating = (service.avg_rating + serializer.validated_data['rating']) / 2

        service.number_review = service.number_review + 1
        service.save()

        serializer.save(service=service, review_user=review_user)


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(service=pk)


class ReviewDetail(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]


class ServiceListAV(APIView):
    def get(self, request, pk):
        stream_platform = Service.objects.get(pk=pk)
        serializer = ServiceSerializer(stream_platform, context={'request': request})
        return Response(serializer.data)
