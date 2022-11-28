from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile
from django.dispatch import receiver


'''
la siguiente funcion solo hace que al crear un usuario se cree tambien un 
perfil de usuario, de manera automatica, sin que el admin tenga que añadirlo
'''
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)