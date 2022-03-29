from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import IntegrityError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from canvas.main.forms import CreateProductFrom
from canvas.main.models import Product, CartItem


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


class ProductDetailView(generic_views.DetailView):
    model = Product
    template_name = 'product_details.html'


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


class CartView(generic_views.ListView):
    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'cartitems'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total = 0
        for cartitem in CartItem.objects.filter(profile=self.request.user.profile):
            total += cartitem.product.product_price * cartitem.quantity
        context['total'] = total
        return context

    def get_queryset(self):
        return self.model.objects.filter(profile=self.request.user.profile)


def add_to_cart_view(request, pk):
    product = Product.objects.get(pk=pk)
    product.product_quantity -= 1
    try:
        cartitem = CartItem.objects.create(product=product, profile=request.user.profile, quantity=1)
    except IntegrityError:
        cartitem = CartItem.objects.filter(profile=request.user.profile)[0]
        cartitem.quantity += 1
    cartitem.save()
    product.product_quantity -= 1
    product.save()
    return redirect(reverse_lazy('browse'))



