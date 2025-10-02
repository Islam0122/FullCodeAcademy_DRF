from django.urls import path
# from .views import NewListCreateAPIView, NewDetailAPIView
#
# urlpatterns = [
#     path('news/', NewListCreateAPIView.as_view()),
#     path('news/<int:pk>/', NewDetailAPIView.as_view()),
# ]

from .views import NewsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'news', NewsViewSet)
urlpatterns = router.urls