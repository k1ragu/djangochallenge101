from django.contrib import admin
from .models import Car
from .models import Plant
from .models import Animal

# Register your models here.
admin.site.register(Car)
admin.site.register(Plant)
admin.site.register(Animal)

