from django.db import models

# Create your models here.
# chat/models.py
from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

class ChatThread(models.Model):
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    participants = models.ManyToManyField(User)

class Message(models.Model):
    thread = models.ForeignKey(ChatThread, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
