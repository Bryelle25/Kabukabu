from django.db import models
import uuid
from django.contrib.auth import get_user_model
User =get_user_model()


class Business(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, )
    type = models.EmailField(max_length=250,)
    country = models.CharField(max_length=250,)
    state = models.TextField()
    city = models.CharField(max_length=250,)
    street = models.CharField(max_length=200,)
    phone = models.CharField(max_length=25, )
    logo = models.ImageField(upload_to='business_logos/', )
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='businesses')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return   f'{self.name} - {self.owner.username}{self.name} - {self.owner.lastrname}'    