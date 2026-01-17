from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Meeting
from users.models import User
from django.utils.dateparse import parse_datetime
from rest_framework import status

class ScheduleMeetingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        investor = request.user
        entrepreneur_id = request.data.get('entrepreneur_id')
        start = parse_datetime(request.data.get('start_time'))
        end = parse_datetime(request.data.get('end_time'))

        entrepreneur = User.objects.get(id=entrepreneur_id)

        conflict = Meeting.objects.filter(
            start_time__lt=end,
            end_time__gt=start,
            status='accepted'
        ).exists()

        if conflict:
            return Response({"error": "Time slot already booked"}, status=400)

        Meeting.objects.create(
            investor=investor,
            entrepreneur=entrepreneur,
            start_time=start,
            end_time=end
        )

        return Response({"message": "Meeting request sent"})

class UpdateMeetingStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, meeting_id):
        action = request.data.get("action")

        try:
            meeting = Meeting.objects.get(id=meeting_id)
        except Meeting.DoesNotExist:
            return Response({"error": "Meeting not found"}, status=404)

        if action == "accept":
            meeting.status = "accepted"
        elif action == "reject":
            meeting.status = "rejected"
        else:
            return Response(
                {"error": "Invalid action. Use accept or reject"},
                status=400
            )

        meeting.save()

        return Response({
            "message": f"Meeting {meeting.status} successfully"
        })
