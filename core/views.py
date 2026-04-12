from django.http import HttpResponse
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'core/index.html'


def ping(request):
    return HttpResponse("OK")
