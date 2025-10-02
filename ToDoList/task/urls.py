from django.urls import path
from .views import ListTaskAPIView,DetailTaskAPIView

urlpatterns = [
    path('list/', ListTaskAPIView.as_view()),
    path('list/<int:task_id>/', DetailTaskAPIView.as_view()),
]
