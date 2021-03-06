from django.urls import path

from app.views import index
from app.views.certificate import *
from app.views.customer import *

urlpatterns = [
    path('', index.index, name='index'),
    path('customers/',
         CustomerListView.as_view(),
         name='customer_list'),
    path('customer/<int:pk>/',
         CustomerView.as_view(),
         name='customer_index'),
    path('customer/<int:pk>/certs/',
         CustomerCertificatesView.as_view(),
         name='customer_certificates'),
    path('customer/<int:pk>/active-certs/',
         CustomerActiveCertificatesView.as_view(),
         name='customer_active_certificates'),
    path('certificates/', CertificateListView.as_view(),
         name='certificate_list'),
    path('certificate/<int:pk>/',
         CertificateView.as_view(),
         name='certificate_index'),
    path('certificate/<int:pk>/activate/',
         CertificateActivateView.as_view(),
         name='certificate_activate'),
]
