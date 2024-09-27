from rest_framework import serializers

from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"

    def validate_title(self, value):
        if value == "" or len(value) < 5:
            raise serializers.ValidationError(
                "A body must have a title with lenght > 5")
        return value
