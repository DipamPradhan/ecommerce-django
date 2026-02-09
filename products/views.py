from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Product

# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    paginate_by = 10


class ProductDetailView(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    template_name = "products/product_add.html"
    fields = [
        "name",
        "image",
        "price",
        "description",
        "stock",
        "seller",
    ]


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "products/product_update.html"
    fields = ["name", "image", "price", "description", "stock"]


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/product_delete.html"
    success_url = reverse_lazy("product_list")
