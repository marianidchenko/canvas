from django.shortcuts import render
from django.views import generic as generic_views


class InternalErrorView(generic_views.TemplateView):
    def get(self, request):
        return render(request, 'error.html')
