from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.
# here django alos have as_dict function but it doesn't have primary key in it..

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    transaction_status = models.BooleanField(default=False, null=False)
    transaction_description = models.TextField(default=" ")
    transaction_model_name = models.CharField(max_length=20)
    transaction_timstamp = models.DateTimeField(default=timezone.now)
    transaction_user_id = models.CharField(default="admin", null=False, max_length=30)

#
# url
# time_stamp
# user_ids
