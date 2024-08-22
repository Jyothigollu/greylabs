from django.urls import path
from .views import DepartmentListCreateView, PatientRecordsListCreateView, PatientRecordsDetailView

urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('patient_records/', PatientRecordsListCreateView.as_view(), name='patient-records-list-create'),
    path('patient_records/<int:pk>/', PatientRecordsDetailView.as_view(), name='patient-record-detail'),
]
