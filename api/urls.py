from django.urls import path
from .views import *

urlpatterns = [
    path('enquiry/', EnquiryCreateAPIView.as_view(), name='enquiry-create'),
    path('packages/', PackageListAPIView.as_view(), name='package-list'),
    path('packages/<int:id>/', PackageDetailAPIView.as_view(), name='package-detail'),
    path('banners/', BannerListAPIView.as_view(), name='banner-list'),
    path('countries/', CountryListCreateAPIView.as_view(), name='country-list-create'),
    path('countries/<int:id>/', CountryDetailAPIView.as_view(), name='country-detail'),
    path('cities/', CityListCreateAPIView.as_view(), name='city-list-create'),
    path('cities/<int:id>/', CityDetailAPIView.as_view(), name='city-detail'),
    path('tour-packages/', TourPackageListCreateAPIView.as_view(), name='tour-package-list-create'),
    path('tour-packages/<int:id>/', TourPackageDetailAPIView.as_view(), name='tour-package-detail'),
    path('schedules/', ScheduleListCreateAPIView.as_view(), name='schedule-list-create'),
    path('schedules/<int:id>/', ScheduleDetailAPIView.as_view(), name='schedule-detail'),
    path('banners/', BannerListCreateAPIView.as_view(), name='banner-list-create'),
    path('banners/<int:id>/', BannerDetailAPIView.as_view(), name='banner-detail'),
    path('tour-photos/', TourPackagePhotoListCreateAPIView.as_view(), name='tourphoto-list-create'),
    path('tour-photos/<int:id>/', TourPackagePhotoDetailAPIView.as_view(), name='tourphoto-detail'),
    path('schedule-photos/', SchedulePhotoListCreateAPIView.as_view(), name='schedulephoto-list-create'),
    path('schedule-photos/<int:id>/', SchedulePhotoDetailAPIView.as_view(), name='schedulephoto-detail'),
]
