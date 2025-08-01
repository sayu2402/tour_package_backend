from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import TourPackage
from .serializers import EnquirySerializer, TourPackageSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


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