from django.db import models
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class Goal(models.Model):
    description = models.CharField(max_length=1024,)
    def __unicode__(self):
        return self.description

class GoalInstance(models.Model):
    goal = models.ForeignKey(Goal)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    started = models.DateField()
    completed = models.BooleanField(default=False)
    def __unicode__(self):
        text = self.goal.description
        try:
            if self.user.significantother.gender == SignificantOther.MALE:
                text = text.replace('[o]', 'him')
                text = text.replace('[s]', 'he')
                text = text.replace('[p]', 'his')
            else:
                text = text.replace('[o]', 'her')
                text = text.replace('[s]', 'she')
                text = text.replace('[p]', 'her')
            text = text.replace('[n]', self.user.significantother.name)
        except ObjectDoesNotExist:
            pass
        return text


class SignificantOther(models.Model):
    MALE = 'MA'
    FEMALE = 'FE'

    GENDER_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female'),
    )

    name = models.CharField(max_length=255,)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    gender = models.CharField(max_length=2,
                              choices=GENDER_CHOICES)
    def __unicode__(self):
        return self.name

