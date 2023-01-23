
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Account.forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def home_view(request):
    return render(request, 'Account/index.html')

def logout_view(request):
    return render(request, 'Account/logout.html')

def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'Account/signup.html', {'form':form})
