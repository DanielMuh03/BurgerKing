from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import CreateProductForm, UpdateProductForm
from .models import *


class CategoryListView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'


class ProductListView(ListView):
    model = Product
    template_name = 'list.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        slug = self.kwargs.get('slug')
        queryset = queryset.filter(category__slug=slug)
        return queryset


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        slug = self.kwargs.get('slug')
        context['slug'] = slug
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'create_product.html'
    form_class = CreateProductForm

   # def get_success_url(self):
       # return reverse('detail', kwargs={'product_id': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['product_form'] = self.get_form()
        return context


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'update_product.html'
    form_class = UpdateProductForm
    pk_url_kwarg = 'product_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['product_form'] = self.get_form()
        return context


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'delete_product.html'
    pk_url_kwarg = 'product_id'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        slug = self.object.category.slug
        self.object.delete()
        return redirect('list', slug)
