from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from .models import Pizza


def index(request, pid):
    pizza = Pizza.objects.get(id=pid)
    return HttpResponse(
        content={
            'id': pizza.id,
            'title': pizza.description,
            'status': 'error',
            'message': 'pizza not found'
        }
    )


class RandomPizza(View):
    template_name = 'ten_pizzas.html'

    def get(self, request):
        pizzas = Pizza.objects.order_by('?')[:10]
        return render(request, self.template_name, {'pizzas': pizzas})
