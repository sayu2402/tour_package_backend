from django.contrib import admin
from .models import Country, City, TourPackage, PackageSchedule, Enquiry

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'country']
    list_filter = ['country']
    search_fields = ['name']


@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'source_country', 'destination_country']
    list_filter = ['source_country', 'destination_country']
    search_fields = ['title', 'description']


@admin.register(PackageSchedule)
class PackageScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'package', 'from_date', 'to_date', 'amount']
    list_filter = ['package']
    search_fields = ['title', 'description']


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'related_schedule']
    list_filter = ['related_schedule']
    search_fields = ['name', 'email', 'message']
