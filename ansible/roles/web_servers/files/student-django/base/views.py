from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Student, Lecturer
from .serializers import StudentSerializer, LecturerSerializer
from django.db.models import Q

@api_view(['GET', 'POST'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/students',
        'GET /api/students/:id',
        'GET /api/lecturers'
    ]
    return Response(routes)

@api_view(['GET'])
def getStudents(request):
    query = request.GET.get('query')
    if query is None: 
        query = ''
    students = Student.objects.filter(Q(full_name__icontains=query) | Q(username__icontains=query))
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStudentDetail(request, id):
    student = Student.objects.get(id=2)
    serializer = StudentSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getLecturers(request):
    list = Lecturer.objects.all()
    serializer = LecturerSerializer(list, many=True)
    return Response(serializer.data)