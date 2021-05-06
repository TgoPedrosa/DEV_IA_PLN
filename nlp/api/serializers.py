from rest_framework import serializers

from .models import Preprocess


class PreprocessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preprocess
        fields = "__all__"
