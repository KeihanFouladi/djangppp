from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserRegister
# Create your views here.


def user_register(request):
    if request.method == 'POST':
        pass
        # form = UserRegister(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return render(request, 'account_app/register_done.html')
    else:
        form = UserRegister()
    return render(request, 'account_app/register.html', {'form': form})
    