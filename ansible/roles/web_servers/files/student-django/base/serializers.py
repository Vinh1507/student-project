from rest_framework.serializers import ModelSerializer
from base.models import Student, Lecturer

class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class LecturerSerializer(ModelSerializer):
    class Meta:
        model = Lecturer
        fields = '__all__'