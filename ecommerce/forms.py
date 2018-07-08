from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()

class ContactForm(forms.Form):
  name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Your name'
      }
    )
  )

  email = forms.EmailField(
    widget=forms.EmailInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Your email',
      }
    )
  )

  message = forms.CharField(
    widget=forms.Textarea(
      attrs={
        'class': 'form-control',
        'placeholder': 'Your message',
      }
    )
  )

class LoginForm(forms.Form):
  username = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'username'
      }
    )
  )
  password = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Your password'
      }
    )
  )

class RegisterForm(forms.Form):
  name = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Your name'
      }
    )
  )
  email = forms.EmailField(
    widget=forms.EmailInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Your email'
      }
    )
  )
  password = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Your password'
      }
    )
  )
  password2 = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control',
        'placeholder': 'Please confirm your password'
      }
    ),
    label='Confirm your password'
  )

  def clean_username(self):
    username = self.cleaned_data.get('username')
    qs = User.objects.filter(username=username)
    if qs.exists():
      raise ValidationError('Username is taken')

  def clean_username(self):
    username = self.cleaned_data.get('email')
    qs = User.objects.filter(email=email)
    if qs.exists():
      raise ValidationError('Email is taken')
     

  def clean(self):
    data = self.cleaned_data
    password = self.cleaned_data.get('password')
    password2 = self.cleaned_data.get('password2')
    if password2 != password:
      raise forms.ValidationError("Passwords must match")
    return data
