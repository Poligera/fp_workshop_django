from django.contrib import admin

from .models import Joke, Language
# Register your models here.
admin.site.register(Language)
admin.site.register(Joke)
