from django.db import models
from django.contrib.auth.models import User as django_user

class User(django_user):
    blah = models.PositiveIntegerField()