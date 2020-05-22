from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    
    image=models.ImageField(default='default.jpg', upload_to='profile_pics',blank=True, null=True)
    telephone=models.CharField(max_length=15, default='')
    codeP=models.CharField(max_length=6, default='')
    rue=models.CharField(max_length=100, default='')
    numero=models.CharField(max_length=100, default='')
    NbPers=models.IntegerField(default=0)
    user=models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Compte de {self.user.username}'

		