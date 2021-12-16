from django.contrib import admin
from .models import Pizza, Pizzeria


class PizzaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Pizza, PizzaAdmin)


class PizzeriaAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.owner


admin.site.register(Pizzeria, PizzeriaAdmin)