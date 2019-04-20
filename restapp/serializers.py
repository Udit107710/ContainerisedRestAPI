from rest_framework import serializers
from .models import Results
from django.contrib.auth.models import User

class ResultSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Results
        exclude = ['prediction']

    def validate_petal_length(self,value):
        if value < 0.0 :
            raise serializers.ValidationError("Petal length is neagtive")
        return value

    def validate_petal_width(self,value):
        if value < 0.0 :
            raise serializers.ValidationError("Petal width is negative")
        return value

    def validate_sepal_length(self,value):
        if value < 0.0 : 
            raise serializers.ValidationError("Sepal width is negative")
        return value

    def validate_sepal_width(self,value):
        if value < 0.0 :
            raise serializers.ValidationError("Sepal width is neagtive")
        return value

class UserSerializer(serializers.ModelSerializer):
    results = serializers.PrimaryKeyRelatedField(many=True, queryset=Results.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'results')
