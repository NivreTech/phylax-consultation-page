from rest_framework import serializers
from rest_framework import PatientInformation

class PatientInformationSerializers(serializers.ModelSerializers):
    class Meta: 
        model = PatientInformation
        fields = '__all__'