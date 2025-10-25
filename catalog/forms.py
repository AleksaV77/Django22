from django.core.exceptions import ValidationError
from django.db.models import BooleanField
from django.forms import ModelForm, forms

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at", "updated_at", "owner")


class ProductModeratorForm(ModelForm):
    class Meta:
        model = Product
        fields = ("unpublish_product",)

    words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    def clean_product_name(self):
        product_name = self.cleaned_data.get("product_name")
        for word in self.words:
            if word.lower() in product_name.lower():
                raise ValidationError(f"Слово {word} нельзя использовать")
        return product_name

    def clean_product_description(self):
        product_description = self.cleaned_data.get("product_description")
        for word in self.words:
            if word.lower() in product_description.lower():
                raise ValidationError(f"Слово {word} нельзя использовать")
        return product_description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной")
        return price

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label}
            )
