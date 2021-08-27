from rest_framework.routers import DefaultRouter
from . import views


app_name = "todos"

router = DefaultRouter()
router.register("", views.TodoViewSet)
urlpatterns = router.urls
