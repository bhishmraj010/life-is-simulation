from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def reports_home(request):
    return render(request, 'reports/home.html')