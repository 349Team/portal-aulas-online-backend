from rest_framework import routers
from django.urls import path, include
from .views import CourseViewSet, LearningViewSet, FavoriteCourseAPIView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'courses', CourseViewSet) 
router.register(r'learnings', LearningViewSet)

app_name = 'courses'

urlpatterns = [
    path('', include(router.urls)),
    path('favorite-course', FavoriteCourseAPIView.as_view(), name="favoritecourse")
]
