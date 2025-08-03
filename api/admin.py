from django.contrib import admin
from .models import (
    Country,
    City,
    TourPackage,
    PackageSchedule,
    Enquiry,
    Banner,
    TourPackagePhoto,
    SchedulePhoto,
)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "country"]
    list_filter = ["country"]
    search_fields = ["name"]


class TourPackagePhotoInline(admin.TabularInline):
    model = TourPackagePhoto
    extra = 1


class SchedulePhotoInline(admin.TabularInline):
    model = SchedulePhoto
    extra = 1


@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    inlines = [TourPackagePhotoInline]
    list_display = ["id", "title", "source_country", "destination_country"]


@admin.register(PackageSchedule)
class PackageScheduleAdmin(admin.ModelAdmin):
    inlines = [SchedulePhotoInline]
    list_display = ["id", "title", "package", "from_date", "to_date", "amount"]


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "phone", "related_schedule"]
    list_filter = ["related_schedule"]
    search_fields = ["name", "email", "message"]


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "image"]
