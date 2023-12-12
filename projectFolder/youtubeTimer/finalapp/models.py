from django.db import models

# Create your models here.
class NewDay(models.Model):
    date = models.DateField()
    hours = models.IntegerField()
    minutes = models.IntegerField()


class StopwatchEntry(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    hours = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.date} - {self.hours} hours {self.minutes} minutes"
    
class UserAccount(models.Model):
    username = models.CharField(max_length=50, default='Matheny')
    email = models.EmailField(default='luke@gmail.com')
    password = models.CharField(max_length=50, default='password')  # Simplified example, use Django's authentication system in a real-world scenario

    def __str__(self):
        return self.username
    

class UserCredentials(models.Model):
    correct_username = models.CharField(max_length=50, default='demo')
    correct_password = models.CharField(max_length=50, default='demo')

    def __str__(self):
        return self.correct_username
    
class Person(models.Model):
    nickname = models.CharField(max_length=255, default='Bon')
    bio = models.TextField(default='Lives in Tampa')
    age = models.IntegerField(default=22)