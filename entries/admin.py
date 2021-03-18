from django.contrib import admin
from .models import Todo, Person

admin.site.register(Person)
admin.site.register(Todo)
