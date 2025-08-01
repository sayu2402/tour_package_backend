from rest_framework import serializers
from api.models import Enquiry, TourPackage, PackageSchedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageSchedule
        fields = '__all__'


class TourPackageSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = TourPackage
        fields = '__all__'

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = ['id', 'name', 'email', 'phone', 'message', 'related_schedule']
