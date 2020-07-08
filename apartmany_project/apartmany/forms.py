from .models import Comment
from django import forms
from django.forms import HiddenInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

# Setting up the Picture Url's for the dropddown list
picture_urls = ()
for i in range(1, 51):
    picture_urls = picture_urls + ((f'apartmany/img/1 de 3 Avatars FLAT/Avatars Set Flat Style-{i}.png', f'Avatar {i}'),)

class CommentForm(forms.ModelForm):
    name = forms.CharField(label='Name',
                            max_length=100,
                            required=True)
    title = forms.CharField(label='Title',
                             max_length=100,
                             required=True)
    rating = forms.IntegerField(label='Rating',
                                initial=5,
                                required=True)
    content = forms.CharField(label='Message',
                              widget=forms.Textarea,
                              required=True)
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name'
        self.fields['title'].widget.attrs['placeholder'] = 'Title of Comment'
        self.fields['rating'].widget = HiddenInput()
        # Pictures
        self.fields['picture'] = forms.ChoiceField(choices=picture_urls)
        # This needs to be removed later
        self.fields['picture'].required = False
        # Set up a helper to manipulate the Rating Field
        self.helper = FormHelper()
        # Add a layout to your helper
        self.helper.layout = Layout(Field('rating', css_class="form-control rating-value"))
    
    class Meta:
        model = Comment
        fields = ('name', 'picture', 'rating', 'title', 'content')
        
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    subject = forms.CharField(max_length=200)
    message = forms.CharField()
    
class ReservationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    type = forms.ChoiceField()
    number = forms.ChoiceField()
    start = forms.CharField(max_length=8)
    end = forms.CharField(max_length=8)
    guests = forms.ChoiceField()
    message = forms.CharField()