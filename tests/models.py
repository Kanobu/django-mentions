from django.db import models
from mentions.models import MentionTextField


class User(models.Model):
    name = models.CharField(max_length=30)

    def get_absolute_url(self):
        return '/users/%d/' % self.pk


class Post(models.Model):
    text = MentionTextField(links=['users'])

    users = models.ManyToManyField(User)


