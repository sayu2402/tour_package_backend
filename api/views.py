from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import TourPackage, Banner, Country, City
from .serializers import *
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class EnquiryCreateAPIView(APIView):
    def post(self, request):
        serializer = EnquirySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Enquiry submitted successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PackageListAPIView(ListAPIView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer


class PackageDetailAPIView(RetrieveAPIView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer
    lookup_field = 'id'


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class CountryListCreateAPIView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'id'

class CityListCreateAPIView(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = 'id'

class TourPackageListCreateAPIView(ListCreateAPIView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageAdminSerializer

class TourPackageDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageAdminSerializer
    lookup_field = 'id'

class ScheduleListCreateAPIView(ListCreateAPIView):
    queryset = PackageSchedule.objects.all()
    serializer_class = ScheduleSerializer

class ScheduleDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = PackageSchedule.objects.all()
    serializer_class = ScheduleSerializer
    lookup_field = 'id'

class BannerListCreateAPIView(ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    lookup_field = 'id'

class TourPackagePhotoListCreateAPIView(ListCreateAPIView):
    queryset = TourPackagePhoto.objects.all()
    serializer_class = TourPackagePhotoSerializer

class TourPackagePhotoDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TourPackagePhoto.objects.all()
    serializer_class = TourPackagePhotoSerializer
    lookup_field = 'id'

class SchedulePhotoListCreateAPIView(ListCreateAPIView):
    queryset = SchedulePhoto.objects.all()
    serializer_class = SchedulePhotoSerializer

class SchedulePhotoDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SchedulePhoto.objects.all()
    serializer_class = SchedulePhotoSerializer
    lookup_field = 'id'