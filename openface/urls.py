from django.urls import path
from .views import ProcessVideoView

urlpatterns = [
    path('process_video/', ProcessVideoView.as_view(), name='process-video'),
]
