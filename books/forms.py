from django import forms
from .models import Book
# from cloudinary.forms import CloudinaryFileField


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ["title", "author", "price", "pages", "year", "sold_out", "image", "description"]



class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book 
        fields = ["title", "author", "price", "pages", "year", "sold_out", "image", "description"]

    # new_image = forms.ImageField(required=False)


    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     if self.instance:
    #         self.fields['new_image'].initial = self.instance.image


    # def save(self, commit=True):

    #     book = super().save(commit=False)
    #     if self.cleaned_data.get('new_image'):
    #         print('ok')
    #         if book.image.name != 'default.png':
    #             book.image.delete()
    #         book.image = self.cleaned_data['new_image']
    #     if commit:
    #         print('okkk')
    #         book.save()
    #     return book