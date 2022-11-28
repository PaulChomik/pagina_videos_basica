from django.contrib import admin
from .models import Post, Profile,Movie

# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Movie)