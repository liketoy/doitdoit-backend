from datetime import datetime
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Todo
from .serializers import TodoSerializer
from .permissions import IsOwner


class TodoViewSet(ModelViewSet):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get_permissions(self):

        if self.action == "create":
            permission_classes = [permissions.IsAuthenticated]
        elif self.action == "update" or self.action == "partial_update":
            permission_classes = [IsOwner]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=False)
    def search(self, request):
        date = request.GET.get("date")
        filter_kwargs = {}
        today = datetime.now().strftime("%Y-%m-%d")
        if date is not None:
            filter_kwargs["end_date"] = date
        try:
            todos = Todo.objects.filter(**filter_kwargs, user=request.user)
        except ValueError:
            todos = Todo.objects.filter(end_date=today, user=request.user)
        paginator = self.paginator
        results = paginator.paginate_queryset(todos, request)
        serializer = TodoSerializer(results, many=True)
        return paginator.get_paginated_response(serializer.data)
