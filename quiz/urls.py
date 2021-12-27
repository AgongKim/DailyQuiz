from django.urls import path
from quiz import views

app_name = 'api_quiz'

urlpatterns = [
    path('<int:cnt>/', views.QuizRandomView.as_view()),
    path('', views.QuizListView.as_view()),
]