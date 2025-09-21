from .models import Allitems, Description, Feedback
from django import forms

class AddItems(forms.ModelForm):
    class Meta:
        model = Allitems
        fields = '__all__'

class AddDescription(forms.ModelForm):
    class Meta:
        model = Description
        fields = '__all__'

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']