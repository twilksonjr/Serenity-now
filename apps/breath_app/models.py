from __future__ import unicode_literals
from django.db import models
from django.contrib import messages
import bcrypt
import re
from datetime import datetime, timedelta


class LoginManager(models.Manager):
    def basic_validator(self, postData):
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        errors = {}
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if not re.match(email_regex, postData['email']):
            errors["email"] = "email must be valid"
        email_check = User.objects.filter(email=postData['email'])
        if len(email_check):
            errors['email'] = "Email is already registered"
        if len(postData["password"]) < 8:
            errors["password"] = "password should be at least 8 characters"
        if postData["password"] != postData["confirm_password"]:
            errors["confirm_password"] = "password and confirm password should match"
        return errors

    def login_validator(self, postData):
        errors = {}
        passwordFromForm = postData['login_password']
        email = postData['login_email']
        usersWithThatEmail = User.objects.filter(email=email)
        if len(usersWithThatEmail) == 0:
            errors['log_email'] = "email not found"
        # if the login information is correct:
        elif not bcrypt.checkpw(passwordFromForm.encode(), usersWithThatEmail[0].password.encode()):
            errors['log_password'] = 'Invalid password'
        return errors


class EventManager(models.Manager):
    def validate_event(self, postData):
        errors = {}
        if len(postData["journal_entry"]) < 3:
            errors["journal_entry"] = "Entry must be at least 3 characters"

        if len(postData["activity_list"]) < 3:
            errors['activity_list'] = "Activity section must be filled out"

        if len(postData["notes"]) < 3:
            errors['notes'] = "notes section must be filled out"
        # if not postData['plan']:
        #     errors['plan'] = "The plan field must filled in"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = LoginManager()

    def __repr__(self):
        return f"Users:({self.first_name}) ({self.last_name})"
