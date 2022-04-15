from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from canvas.common_tools.helpers import get_total_price, get_available_payment_methods, get_available_addresses, \
    get_cart_items
from canvas.main.forms import ChooseCardAndAddress
from canvas.main.models import Product, CartItem


def add_to_cart_view(request, pk):
    product = Product.objects.get(pk=pk)
    current_profile = request.user.profile
    product.product_quantity -= 1
    product.save()
    cartitem = CartItem.objects.filter(profile=current_profile, product=product)
    if not cartitem:
        cartitem = CartItem.objects.create(
            product=product,
            profile=current_profile
        )
    else:
        cartitem = cartitem[0]
    cartitem.quantity += 1
    cartitem.save()
    return redirect('browse')


class CartView(LoginRequiredMixin, generic_views.ListView):
    model = CartItem
    template_name = 'cart.html'
    context_object_name = 'cartitems'

    def get_context_data(self, **kwargs):
        current_profile = self.request.user.profile
        context = super().get_context_data(**kwargs)
        context['total'] = get_total_price(current_profile)
        context['cards'] = get_available_payment_methods(current_profile)
        context['addresses'] = get_available_addresses(current_profile)
        context['form'] = ChooseCardAndAddress
        return context

    def get_queryset(self):
        return self.model.objects.filter(profile=self.request.user.profile)


class RemoveCartItemView(LoginRequiredMixin, generic_views.DeleteView):
    model = CartItem
    template_name = 'cart_item_remove.html'
    success_url = reverse_lazy('cart')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('cart')
        else:
            item = self.get_object()
            item.product.product_quantity += item.quantity
            item.product.save()
            item.delete()
            return redirect('cart')


class CheckoutView(LoginRequiredMixin, generic_views.FormView):
    template_name = 'checkout.html'
    form_class = ChooseCardAndAddress
    success_url = reverse_lazy('purchased')

    def get_form_kwargs(self):
        kwargs = super(CheckoutView, self).get_form_kwargs()
        kwargs['profile'] = self.request.user.profile
        return kwargs

    def get_context_data(self, **kwargs):
        current_profile = self.request.user.profile
        context = super().get_context_data(**kwargs)
        context['items'] = get_cart_items(current_profile)
        context['total'] = get_total_price(current_profile)
        context['cards'] = get_available_payment_methods(current_profile)
        context['addresses'] = get_available_addresses(current_profile)
        return context

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('cart')
        else:
            CartItem.objects.filter(profile=request.user.profile).delete()
            return redirect('purchased')


class PurchasedView(LoginRequiredMixin, generic_views.TemplateView):
    template_name = 'purchased.html'