from django import forms

from .models import Users


class CustomUserCreationForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = '__all__'


class CustomUserChangeForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = '__all__'


class SignupForm(forms.ModelForm):
    password2 = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password again'})
    )

    class Meta:
        model = Users
        fields = ('email', 'full_name', 'password', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'email'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'full name'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        max_length=128
    )
