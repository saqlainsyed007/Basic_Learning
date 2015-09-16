from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User


# Every class here is a database table and variables are atributes to table.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # This is used to identify the returned object.
    # We use unique field of the class for this purpose
    def __unicode__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    was_published_recently.short_description = 'Published recently?'
    was_published_recently.boolean = True


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text


# To Extend User Model and add CompanyName and UserImage
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    user_image = models.ImageField(upload_to='profile_images', blank='true')
