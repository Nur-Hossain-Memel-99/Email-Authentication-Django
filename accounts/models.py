from django.db import models
#importing user
from django.contrib.auth.models import User



class Profile(models.Model):

    user = models.OneToOneField(User , on_delete=models.CASCADE)
    #random token generate
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    #which user 
    def __str__(self):
        return self.user.username


