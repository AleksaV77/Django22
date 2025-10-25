from django.core.exceptions import ValidationError
from django.forms import ModelForm

from blog.models import Blogs


class BlogsForm(ModelForm):
    class Meta:
        model = Blogs
        exclude = ("view_counter", "created_at")

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

    def clean_title(self):
        title = self.cleaned_data.get("title")
        for word in self.words:
            if word.lower() in title.lower():
                raise ValidationError(f"Слово {word} нельзя использовать")
        return title

    def clean_blogs_description(self):
        blogs_description = self.cleaned_data.get("blogs_description")
        for word in self.words:
            if word.lower() in blogs_description.lower():
                raise ValidationError(f"Слово {word} нельзя использовать")
        return blogs_description

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {"class": "form-control", "placeholder": field.label}
            )
