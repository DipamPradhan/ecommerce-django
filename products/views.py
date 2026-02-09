from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import SingleObjectMixin

from .forms import ReviewForm
from .models import Product
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Avg, Count


# Create your views here.
class CommentGet(DetailView):
    model = Product
    template_name = "products/product_detail.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Product
    form_class = ReviewForm
    template_name = "products/product_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.product = self.object
        review.reviewer = self.request.user
        review.save()
        return super().form_valid(form)

    def get_success_url(self):
        product = self.object
        return reverse("product_detail", kwargs={"pk": product.pk})


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    paginate_by = 10

    def get_queryset(self):
        return Product.objects.annotate(
            avg_rating=Avg("reviews__rating"),
            review_count=Count("reviews"),
        )


class ProductDetailView(LoginRequiredMixin, DetailView):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "products/product_add.html"
    fields = [
        "name",
        "image",
        "price",
        "description",
        "stock",
    ]

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = "products/product_update.html"
    fields = ["name", "image", "price", "description", "stock"]

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.seller


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "products/product_delete.html"
    success_url = reverse_lazy("product_list")

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.seller
