from django.db import models

# Create your models here.
class UserDetails(models.Model):

    user_name = models.CharField(max_length=30)
    user_email = models.EmailField()
    user_contact = models.CharField(max_length=15)
    user_gender = models.CharField(max_length=10)
    user_dob = models.DateField()
    user_pswd = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name