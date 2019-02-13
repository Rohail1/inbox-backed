from django.utils import timezone
from custom_user.models import AbstractEmailUser
from django.db import models


class User(AbstractEmailUser):

    date_of_birth = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
