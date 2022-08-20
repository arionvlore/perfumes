
from django.forms import ModelForm
from shop.models import Employer
from django import forms
from .models import Contact, Subscribe, Pay


class EmpForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = "__all__"


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'


class PayForm(forms.ModelForm):
    class Meta:
        model = Pay
        fields = "__all__"
