from django.urls import path
from . import views
from platform_student.views import index, MaterialDetailView, QuizView, check_answer
from platform_student.apps import LearningPlatformConfig


app_name = LearningPlatformConfig.name


urlpatterns = [
    path('', index, name='index'),
    path('material_list/<int:section_id>/', views.material_list, name='material_list'),
    path('material_detail/<int:pk>/', MaterialDetailView.as_view(), name='material_detail'),
    path('check_answer/', check_answer, name='check_answer'),
    path('quiz/<int:material_id>/', QuizView.as_view(), name='quiz'),
]
