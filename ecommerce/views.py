from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, ContactForm, RegisterForm

User = get_user_model()

# Create your views here.
def home_page(request):
  return render(request, 'home_page.html')

def contact_page(request):
  contact_form = ContactForm(request.POST or None)

  context = {
    'title': 'Contact Us',
    'form': contact_form,
  }

  if contact_form.is_valid():
    print(contact_form.cleaned_data)

  return render(request, 'contact_page.html', context)

def login_page(request):
  form = LoginForm(request.POST or None)
  context = {
    'form': form,
  } 
  if form.is_valid():
    # get the username and password date
    username = form.cleaned_data.get('username')
    password = form.cleaned_data.get('password')
    # authenticated the cleaned data from request to database
    user = authenticate(request, username=username, password=password)
    # we get the user from database
    if user is not None:
      # we allow the user proceed to login
      login(request, user)
      # redirect to the home page with greetings
      return redirect('home_page')
  else:
    print("error")
  return render(request, 'auth/login_page.html', context)

def register_page(request):
  form = RegisterForm(request.POST or None)
  context = {
    'form': form,
  }
  if form.is_valid():
    username = form.cleaned_data.get('username')
    email = form.cleaned_data.get('email')
    password = form.cleaned_data.get('password')
    new_user = User.objects.create_user(username, email, password)
    print(new_user)
  else:
    print("form error")

  return render(request, 'auth/register_page.html', context)