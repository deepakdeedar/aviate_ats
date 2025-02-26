from django.db import models
from django.db.models import Q

class Candidate(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(age__gte=18), name='age_gte_18'),
            models.CheckConstraint(check=Q(phone_number__regex=r'^\+?[0-9]{10,15}$'), name='valid_phone_number'),
        ]
    
    def __str__(self):
        return self.name