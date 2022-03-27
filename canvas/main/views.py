from django.views import generic as generic_views

from canvas.main.forms import CreateProductFrom
from canvas.main.models import Product


class IndexView(generic_views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome to Canvas'
        context['user'] = self.request.user
        return context


class CreateProductView(generic_views.CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = CreateProductFrom
