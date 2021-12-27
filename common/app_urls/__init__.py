from django.urls import include, path

app_name = 'common_urls'
urlpatterns = [
    path('quiz/', include('quiz.urls', namespace='api_quiz')),
]
