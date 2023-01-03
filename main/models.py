from django.db import models
from django.contrib.auth.models import User


class BossExtra(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    joindate = models.DateField(auto_now_add=True)
    mobile = models.CharField(max_length=40)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.user.first_name

    @property
    def get_id(self):
        return self.user.id

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
