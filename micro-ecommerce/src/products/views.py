from django.shortcuts import get_object_or_404
from django.shortcuts import redirect, render

# Create your views here.
from .forms import ProductForm
from .models import Product


def product_create_view(request):
    context = {}
    form = ProductForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        if request.user.is_authenticated:
            obj.user = request.user
            obj.save()
            return redirect("/products/create/")
        else:
            form.add_error(
                None,
                "You must be logged in to create products",
            )

    context["form"] = form
    return render(request, "products/create.html", context)


def product_list_view(request):
    object_list = Product.objects.all()
    context = {
        "object_list": object_list,
    }
    return render(request, "products/list.html", context)


def product_detail_view(request, handle=None):
    object = get_object_or_404(Product, handle=handle)
    is_owner = (
        object.user == request.user
        if request.user.is_authenticated
        else False
    )
    context = {"object": object}
    if is_owner:
        form = ProductForm(
            request.POST or None,
            instance=object,
        )
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
        context["form"] = form
    return render(request, "products/detail.html", context)
