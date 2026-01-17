from django.db import models
from users.models import User

class Meeting(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    investor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='investor_meetings'
    )
    entrepreneur = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='entrepreneur_meetings'
    )

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Meeting {self.investor} - {self.entrepreneur}"
