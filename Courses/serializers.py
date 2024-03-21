from core.models import Teacher, Subject
from rest_framework import serializers

#ModelSerializer
class SubjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Subject
        fields ='__all__'

class TeacherSerializer(serializers.ModelSerializer):

    Subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model= Teacher
        fields =['id','name','email','Subjects']
        # fields ='__all__' #Order will not maintain doesn't look good

        read_only_fields = ('id',)


