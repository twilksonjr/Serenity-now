from __future__ import unicode_literals
from django.db import models
from apps.breath_app.models import User
from django.contrib import messages
from datetime import datetime,timedelta
import re

class SerenityShiftManager(models.Manager):
    def serenityshift_validator(self, postData):
    # add keys and values to errors dictionary for each invalid field

        errors = {}
        if len(postData['name'])==0:
            errors["name"] = "Please enter a valid name"
        if len(postData['journal'])==0:
            errors["destination"] = "Please enter a triggering event"
        if len(postData['gratitude_list'])==0:
            errors["gratitude_list"] = "Please at least one gratitude"
        if len(postData['activity_list'])==0:
            errors["activity_list"] = "Please enter at least one activity"
        if len(postData['notes'])==0:
            errors["plan"] = "Please enter at least one observation"
        if len(postData['destination']) < 3:
            errors["destination"] = "Destination should be at least 3 characters"
        if len(postData['plan']) < 3:
            errors["plan"] = "Plan should be at least 3 characters"

        return errors




class SerenityShift(models.Model):
    suds_level_begin = models.IntegerField(default=0)
    suds_level_end = models.IntegerField(default=0)
    player = models.ForeignKey(User, related_name="list_of_shifts_associated_with_user", default = "")
    currency = models.IntegerField(default=0)
    taste = models.IntegerField(default=0)
    touch = models.IntegerField(default=0)
    visual = models.IntegerField(default=0)
    auditory = models.IntegerField(default=0)
    smell = models.IntegerField(default=0)
    num_breathing = models.IntegerField(default=0)
    journal = models.TextField(default = "")
    gratitude_list = models.TextField(default = "")
    activity_list = models.TextField(default = "")
    observations = models.TextField(default = "")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SerenityShiftManager() 