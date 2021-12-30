from django.db import models
from django.contrib.auth.models import User

# Create our models here
class UserProfileInfo(models.Model):
# Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE,)


# Add Additional Attribute
    protfolio=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_img', blank=True)

    def __str__(self):
        return self.user.username

