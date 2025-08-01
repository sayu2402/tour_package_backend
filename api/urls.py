from django.urls import path
from .views import EnquiryCreateAPIView, PackageDetailAPIView, PackageListAPIView, BannerListAPIView

urlpatterns = [
    path('enquiry/', EnquiryCreateAPIView.as_view(), name='enquiry-create'),
    path('packages/', PackageListAPIView.as_view(), name='package-list'),
    path('packages/<int:id>/', PackageDetailAPIView.as_view(), name='package-detail'),
    path('banners/', BannerListAPIView.as_view(), name='banner-list'),
]
