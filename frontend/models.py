from django.db import models

class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Added field

    def __str__(self):
        return f"{self.ip_address} - {'Active' if self.is_active else 'Inactive'}"
