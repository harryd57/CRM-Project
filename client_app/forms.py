from django import forms
from account.admin import UserCreationForm
from account.models import MyUser
from . models import ClientAccount


class ClientSignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'id': 'floatingPassword', 'placeholder': 'Verify Password'}))

    class Meta:
        model = MyUser
        fields = ('email', 'company_name', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'name@email.com'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Company Name'}),
        }

    def data_save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        return user


class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientAccount
        fields = ('phone_no', 'website', 'location')
        widgets = {
            'phone_no': forms.NumberInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Company Name'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Company Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'Company Name'}),
        }
