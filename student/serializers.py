from rest_framework import serializers
from student.models import semester,subject, student, Result

class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = semester
        fields = '__all__'

class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subject
        fields = '__all__'                    

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'

    def validate_current_sem(self, value):
        if value<1 or value>8 : 
            raise serializers.ValidationError("Sem out of range")
            
class ResultSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'