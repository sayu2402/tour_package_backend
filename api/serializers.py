from rest_framework import serializers
from api.models import Enquiry, TourPackage, PackageSchedule, Banner, TourPackagePhoto, SchedulePhoto


class TourPackagePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackagePhoto
        fields = ['id', 'image']

class SchedulePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchedulePhoto
        fields = ['id', 'image']

class ScheduleSerializer(serializers.ModelSerializer):
    photos = SchedulePhotoSerializer(many=True, read_only=True)

    class Meta:
        model = PackageSchedule
        fields = '__all__'

class TourPackageSerializer(serializers.ModelSerializer):
    source_country = serializers.StringRelatedField()
    source_city = serializers.StringRelatedField()
    destination_country = serializers.StringRelatedField()
    destination_city = serializers.StringRelatedField()
    photos = TourPackagePhotoSerializer(many=True, read_only=True)
    schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = TourPackage
        fields = '__all__'


class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = '__all__'



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'