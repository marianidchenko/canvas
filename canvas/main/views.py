from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
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


class AllProductsView(generic_views.ListView):
    model = Product
    template_name = 'browse.html'
    context_object_name = 'products'
    paginate_by = 10


class CreateProductView(generic_views.CreateView, LoginRequiredMixin):
    model = Product
    template_name = 'product_create.html'
    form_class = CreateProductFrom
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super(CreateProductView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('index')
        else:
            return super(CreateProductView, self).post(request, *args, **kwargs)



