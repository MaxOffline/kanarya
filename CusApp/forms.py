from .models import newcustomer,Item
from django import forms
from django.contrib.auth.models import User




class Register(forms.ModelForm):
    username= forms.CharField( max_length = 12)
    password = forms.CharField(max_length = 15, widget = forms.PasswordInput)


    class Meta:

        model = User
        fields = ("username", "password","email")


class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = newcustomer
        fields = ("Customer_Name","Clothes_Price","Clothes_Kilos")

class Login_Form(forms.Form):
    username = forms.CharField(max_length = 15)
    password = forms.CharField(widget=forms.PasswordInput, max_length = 12)

class SearchForm(forms.ModelForm):
    class Meta:
        model = newcustomer
        fields = ("Customer_Name",)

class BuggyForm(forms.ModelForm):
    submitted = forms.BooleanField(widget=forms.HiddenInput,required=False)
    cart = forms.CharField(widget=forms.HiddenInput,required=False)
    class Meta:
        model = Item
        fields = ("url","color","weight","submitted")
