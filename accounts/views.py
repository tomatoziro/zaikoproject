from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('zaiko:index')
