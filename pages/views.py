from django.shortcuts import render
from django.views import View

# Create your views here.


class HomeView(View):
    template_name = 'index.html'

    def get(self, request):
        context = {}

        return render(request, self.template_name, context)
