from django.db import models
import re
from datetime import datetime, date
# Create your models here.

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}

        Name_REGEX = re.compile(r'^[a-zA-Z.+_-]+$')
        email_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        # Validating the length of users first name
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First Name should be at least 2 characters."

        # Validating users first name and ensuring its only Letters
        if not Name_REGEX.match(postData['first_name']):
            errors['first_name'] = "Invalid first name."

        # Validating the length of users last name
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters."

        # Validating users last name and ensuring its only Letters
        if not Name_REGEX.match(postData['last_name']):
            errors['last_name'] = "Invalid last name."

        # Email validation
        if not email_REGEX.match(postData['email']):
            errors['email'] = "Please use a valid email."

        #Validating if the registered email is unique
        email_duplicate = User.objects.filter(email=postData['email'])
        if email_duplicate:  # Non-EMPTY LIST
            errors['email_in_use'] = "Email already in use."


        # if no date given or if the date is a future date, throw the error.
        if postData['birthday'] == '' or datetime.strptime(postData["birthday"], '%Y-%m-%d') > datetime.today():
            print(datetime.today())
            errors['birth_date'] = "Birth Date should be in the past."

        if postData['birthday'] == '':
            errors['error'] = "Please Provide Email"
        # Validating if the user is age of 13 and above
        else: 
            today = datetime.today()
            birthday = datetime.strptime(postData["birthday"], '%Y-%m-%d')
            print(today.year - birthday.year) 
            if today.year - birthday.year < 13:
                errors['birth_Date_requirement'] = "You are no allowed to use this application" 
        

        if len(postData['password']) < 8:
            errors['password'] = "Password should be at least 8 characters."

        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Password and Password confirmation Should Match."

        return errors

    def email_validator(self, postData):
        email_duplicate = User.objects.filter(email=postData)
        if email_duplicate:  # Non-EMPTY LIST
            return True
        else:
            return False

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    birthday = models.DateField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
