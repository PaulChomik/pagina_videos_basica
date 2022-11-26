from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
'''
PAra activar y actualizar los modelos hay que hacer
python manage.py makemigrations
python manage.py migrate

Los siguientes son los modelos creados en tablas, si queremos borrarlos bastara con
borrarlos de models.py
'''
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='img_avatar1.png')
    def __str__(self):
        return f'Perfil de {self.user.username}'

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    timestamp=models.DateTimeField(default=timezone.now)
    content=models.TextField()

    class Meta:
        ordering=['-timestamp']
    #este codigo solo muestra en el admin site el post
    def __str__(self):
        return f'{self.user.username}:{self.content}'

class Movie(models.Model):
    '''
    tengo qe crear un campo movie que tenga
    - nombre  -comentario o sinopsis  -link para ver el video
    -comentarios de los usuarios
    '''
    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='Movie')
    name=models.CharField(max_length=30)
    link=models.URLField(null=True,blank=True,verbose_name='Direccion del Trailer')
    sinopsis=models.TextField()
    image=models.ImageField(default='img_avatar1.png')
    timestamp=models.DateTimeField(default=timezone.now)

    class Meta:
        ordering=['-timestamp']
    def __str__(self):
        return f'{self.name}:{self.sinopsis},{self.link}'
