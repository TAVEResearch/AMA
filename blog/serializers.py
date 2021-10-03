from .models import *
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
    class Meta :
        model = Question
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta :
        model = Comment
        fields = '__all__'

class Hall_of_FameSerializer(serializers.ModelSerializer):
    class Meta :
        model = Hall_of_Fame
        fields = '__all__'

class Top10Serializer(serializers.ModelSerializer):
    class Meta :
        model = Top10
        fields = '__all__'