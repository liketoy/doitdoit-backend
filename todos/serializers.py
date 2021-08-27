from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude = ("modified",)
        read_only_fields = (
            "user",
            "id",
            "created",
        )

    def create(self, validate_data):
        request = self.context.get("request")
        todo = Todo.objects.create(**validate_data, user=request.user)
        return todo
