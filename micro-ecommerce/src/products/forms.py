from django import forms
from django.utils.text import slugify
from .models import Product


input_css_class = "form-control"


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ["name", "handle", "price"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = input_css_class


    def clean_name(self):
        name = self.cleaned_data["name"]
        # Remove any leading or trailing white space from the name
        name = name.strip()
        # Replace any consecutive white space with a single space
        name = " ".join(name.split())
        # Generate a unique slug for the name
        slug = slugify(name)
        # Check if a product with this slug already exists
        if Product.objects.filter(handle=slug).exists():
            # Raise a validation error if a product with this name already exists
            raise forms.ValidationError("A product with this name already exists.")
        # Return the cleaned and validated name
        return name
