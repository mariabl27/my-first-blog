from django.contrib import admin
from .models import Post

admin.site.register(Post) # making model visible on the admin page
# Register your models here.
