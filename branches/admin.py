from django.contrib import admin

from branches import models

to_register = [
    models.Restaurant,
    models.Employee,
]

admin.site.register(to_register)
