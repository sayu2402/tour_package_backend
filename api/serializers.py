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
    photos = TourPackagePhotoSerializer(many=True, read_only=True)
    schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = TourPackage
        fields = '__all__'


class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = ['id', 'name', 'email', 'phone', 'message', 'related_schedule']



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'