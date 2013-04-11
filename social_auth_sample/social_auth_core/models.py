from django.db import models
from django.contrib.auth.models import User

class FbUser(User):
    some_number = models.CharField(max_length=50)