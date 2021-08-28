from django.db import models
from django.utils import timezone


method = [
    ('GET', 'method GET'),
    ('POST', 'method POST'),
    ('HEAD', 'method HEAD'),
    ('PUT', 'method PUT'),
    ('PATCH', 'method PATCH'),
    ('DELETE', 'method DELETE'),
    ('OPTIONS', 'method OPTIONS'),
]


class LogModel(models.Model):
    path = models.CharField(max_length=200)
    method = models.CharField(max_length=200, choices=method)
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f'{str(self.path)}, {str(self.method)}, {str(self.method)}'
