from rest_framework import serializers
from api.models import Enquiry, TourPackage, PackageSchedule, Banner, TourPackagePhoto, SchedulePhoto, Country, City


class TourPackagePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackagePhoto
        fields = ['id', 'image','package']

class SchedulePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchedulePhoto
        fields = ['id', 'image', 'schedule']

class ScheduleSerializer(serializers.ModelSerializer):
    photos = SchedulePhotoSerializer(many=True, read_only=True)
    package_title = serializers.CharField(source='package.title', read_only=True)

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


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class TourPackageAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourPackage
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['source_country'] = {
            'id': instance.source_country.id,
            'name': instance.source_country.name
        } if instance.source_country else None

        rep['destination_country'] = {
            'id': instance.destination_country.id,
            'name': instance.destination_country.name
        } if instance.destination_country else None

        rep['source_city'] = {
            'id': instance.source_city.id,
            'name': instance.source_city.name
        } if instance.source_city else None

        rep['destination_city'] = {
            'id': instance.destination_city.id,
            'name': instance.destination_city.name
        } if instance.destination_city else None

        return rep

class EnquirySerializer(serializers.ModelSerializer):
    related_schedule_title = serializers.SerializerMethodField()

    class Meta:
        model = Enquiry
        fields = ['id', 'name', 'email', 'phone', 'message', 'related_schedule', 'related_schedule_title']

    def get_related_schedule_title(self, obj):
        print(f"Checking enquiry ID {obj.id} - related_schedule: {obj.related_schedule}")
        if obj.related_schedule:
            return obj.related_schedule.title
        return 'General Enquiry'
