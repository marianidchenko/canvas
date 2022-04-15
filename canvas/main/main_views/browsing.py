from django.views import generic as generic_views

from canvas.common_tools.helpers import get_profile_by_username
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

    def get_queryset(self):
        products = Product.objects.exclude(product_quantity=0).order_by('-created_on', 'product_name')
        return products

    paginate_by = 8


class SearchProductsView(generic_views.ListView):
    model = Product
    template_name = 'browse.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            result = Product.objects.filter(product_name__icontains=query).exclude(product_quantity=0)
        else:
            result = Product.objects.all()
        return result
    paginate_by = 8


class ProfileProductViews(generic_views.ListView):
    model = Product
    template_name = 'browse.html'
    context_object_name = 'products'
    paginate_by = 8

    def get_queryset(self):
        profile = get_profile_by_username(self.kwargs['username'])
        return self.model.objects.filter(profile=profile)


class ProductDetailView(generic_views.DetailView):
    model = Product
    template_name = 'product_details.html'