from django.db import models


class ContactMessage(models.Model):
    """Stores leads submitted through the home page contact form."""

    SERVICE_CHOICES = [
        ('residential', 'Residential Construction'),
        ('commercial', 'Commercial Construction'),
        ('renovation', 'Renovation & Remodeling'),
        ('other', 'Other / Not Sure'),
    ]

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES, default='other')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} ({self.created_at:%Y-%m-%d})'
