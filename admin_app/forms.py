from django import forms
from account.admin import UserCreationForm
from account.models import MyUser
from.models import AdminAccount


class AdminSignUpForm(UserCreationForm):
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


class AdminForm(forms.ModelForm):
    registration_code = forms.CharField(
        label="Set Registration Code", required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput', 'placeholder': 'create code'}))

    class Meta:
        model = AdminAccount
        fields = ('registration_code',)
