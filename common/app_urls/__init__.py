from django.urls import include, path

from common.views import DecoratedTokenObtainPairView, DecoratedTokenRefreshView, DecoratedTokenVerifyView

app_name = 'common_urls'
urlpatterns = [
    #JWT
    path('token/', DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', DecoratedTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', DecoratedTokenVerifyView.as_view(), name='token_verify'),

    path('quiz/', include('quiz.urls', namespace='api_quiz')),
    path('common/', include('common.urls', namespace='api_common')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/', include('dj_rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls', namespace='api_accounts')),
]
