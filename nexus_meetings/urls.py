from django.urls import path
from .views import ScheduleMeetingView
from .views import ScheduleMeetingView, UpdateMeetingStatusView

urlpatterns = [
    path('schedule/', ScheduleMeetingView.as_view()),
    path('schedule/', ScheduleMeetingView.as_view()),
    path('<int:meeting_id>/update/', UpdateMeetingStatusView.as_view()),
]

