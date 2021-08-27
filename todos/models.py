from django.db import models
from core.models import CoreModel


class Todo(CoreModel):

    title = models.CharField(max_length=140)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="todos"
    )
    is_completed = models.BooleanField(default=False)
    end_date = models.DateField()

    class Meta:
        ordering = ["id"]
