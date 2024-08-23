from rest_framework import generics, viewsets
from .models import PatientRecords, Department
from .serializers import PatientRecordsSerializer, DepartmentSerializer
from .permissions import IsPatientOrReadOnly, IsDoctorOrReadOnly
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to Grey Scientific Labs API!")


class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PatientRecordsListCreateView(generics.ListCreateAPIView):
    queryset = PatientRecords.objects.all()
    serializer_class = PatientRecordsSerializer
    permission_classes = [IsDoctorOrReadOnly]

class PatientRecordsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientRecords.objects.all()
    serializer_class = PatientRecordsSerializer
    permission_classes = [IsPatientOrReadOnly, IsDoctorOrReadOnly]



class PatientRecordsListCreateView(generics.ListCreateAPIView):
    queryset = PatientRecords.objects.all()
    serializer_class = PatientRecordsSerializer
    permission_classes = [IsAuthenticated, IsDoctorOrReadOnly]



