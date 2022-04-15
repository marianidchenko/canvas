from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as generic_views

from canvas.main.forms import CreateProductFrom, ProductEditForm, ProductRestockForm, ProductDeleteForm
from canvas.main.models import Product


class CreateProductView(LoginRequiredMixin, generic_views.CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = CreateProductFrom
    success_url = reverse_lazy('manage products')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super(CreateProductView, self).form_valid(form)


class ManageProductsView(LoginRequiredMixin, generic_views.ListView):
    model = Product
    template_name = 'product_manage.html'
    context_object_name = 'products'

    def get_queryset(self):
        return self.model.objects.filter(profile=self.request.user.profile).order_by('product_quantity')


class EditProductView(LoginRequiredMixin, generic_views.UpdateView):
    model = Product
    template_name = 'product_edit.html'
    form_class = ProductEditForm
    success_url = reverse_lazy('manage products')


class RestockProductView(LoginRequiredMixin, generic_views.UpdateView):
    model = Product
    template_name = 'product_restock.html'
    form_class = ProductRestockForm
    success_url = reverse_lazy('manage products')


class DeleteProductView(generic_views.DeleteView):
    model = Product
    template_name = 'product_delete.html'
    form_class = ProductDeleteForm
    success_url = reverse_lazy('manage products')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            return redirect('manage products')
        else:
            return super(DeleteProductView, self).post(request, *args, **kwargs)