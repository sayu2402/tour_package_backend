from django.urls import path
from .views import *

urlpatterns = [
    path("enquiry/", EnquiryCreateAPIView.as_view(), name="enquiry-create"),
    path("packages/", PackageListAPIView.as_view(), name="package-list"),
    path("packages/<int:id>/", PackageDetailAPIView.as_view(), name="package-detail"),
    path("banners/", BannerListAPIView.as_view(), name="banner-list"),
    path(
        "admin/countries/",
        CountryListCreateAPIView.as_view(),
        name="country-list-create",
    ),
    path(
        "admin/countries/<int:id>/",
        CountryDetailAPIView.as_view(),
        name="country-detail",
    ),
    path("admin/cities/", CityListCreateAPIView.as_view(), name="city-list-create"),
    path("admin/cities/<int:id>/", CityDetailAPIView.as_view(), name="city-detail"),
    path(
        "admin/tour-packages/",
        TourPackageListCreateAPIView.as_view(),
        name="tour-package-list-create",
    ),
    path(
        "admin/tour-packages/<int:id>/",
        TourPackageDetailAPIView.as_view(),
        name="tour-package-detail",
    ),
    path(
        "admin/schedules/",
        ScheduleListCreateAPIView.as_view(),
        name="schedule-list-create",
    ),
    path(
        "admin/schedules/<int:id>/",
        ScheduleDetailAPIView.as_view(),
        name="schedule-detail",
    ),
    path(
        "admin/banners/", BannerListCreateAPIView.as_view(), name="banner-list-create"
    ),
    path(
        "admin/banners/<int:id>/", BannerDetailAPIView.as_view(), name="banner-detail"
    ),
    path(
        "admin/tour-photos/",
        TourPackagePhotoListCreateAPIView.as_view(),
        name="tourphoto-list-create",
    ),
    path(
        "admin/tour-photos/<int:id>/",
        TourPackagePhotoDetailAPIView.as_view(),
        name="tourphoto-detail",
    ),
    path(
        "admin/schedule-photos/",
        SchedulePhotoListCreateAPIView.as_view(),
        name="schedulephoto-list-create",
    ),
    path(
        "admin/schedule-photos/<int:id>/",
        SchedulePhotoDetailAPIView.as_view(),
        name="schedulephoto-detail",
    ),
    path("admin/enquiries/", EnquiryListAPIView.as_view(), name="enquiry-list"),
]
