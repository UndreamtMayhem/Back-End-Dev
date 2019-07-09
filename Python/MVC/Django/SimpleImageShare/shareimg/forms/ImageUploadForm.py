from django import forms

class ImageUploadForm(forms.Form):
    title = forms.CharField(max_length = 600, required=True)
    description = forms.CharField(max_length = 600, required=True)
    file = forms.ImageField(required=True)