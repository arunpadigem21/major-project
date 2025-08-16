# frontend/views.py
from django.shortcuts import render, redirect
from .models import IPAddress
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import IPAddress
from django.http import JsonResponse
from .models import IPAddress

from django.contrib.auth import authenticate, login
from django.contrib import messages

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect('home')  # change to your dashboard/home page URL name
            else:
                return render(request, 'signin.html', {'error': 'Access denied. Superuser only.'})
        else:
            return render(request, 'signin.html', {'error': 'Invalid credentials.'})
    
    return render(request, 'signin.html')
from django.contrib.auth import logout
@never_cache
@login_required
def signout(request):
    logout(request)
    return redirect('signin')
@never_cache
@login_required
def home(request):
    return render(request, 'index.html')

@never_cache
@login_required
def settings_view(request):
    return render(request, 'settings.html')

@never_cache
@login_required
def add_ip_view(request):
    if request.method == "POST":
        ip_address = request.POST.get("ip_address")
        if ip_address:
            IPAddress.objects.get_or_create(ip_address=ip_address, defaults={'is_active': True})
        return redirect('add_ip')  # Avoid form resubmission

    ip_list = IPAddress.objects.all().order_by('-created_at')
    return render(request, 'add_ip.html', {'ip_list': ip_list})
@never_cache
@login_required
@csrf_exempt
def deactivate_ip(request):
    if request.method == "POST":
        ip = request.POST.get('ip_address')
        ip_entry = IPAddress.objects.filter(ip_address=ip).first()
        if ip_entry:
            ip_entry.is_active = False
            ip_entry.save()
    return redirect('add_ip')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
@never_cache
@login_required
@csrf_exempt
def toggle_ip_status(request):
    if request.method == "POST":
        ip = request.POST.get('ip_address')
        ip_entry = IPAddress.objects.filter(ip_address=ip).first()
        if ip_entry:
            ip_entry.is_active = not ip_entry.is_active
            ip_entry.save()
            return JsonResponse({
                'status': 'success',
                'new_status': ip_entry.is_active,
                'ip_address': ip_entry.ip_address
            })
    return JsonResponse({'status': 'error'}, status=400)

@never_cache
@login_required
@csrf_exempt
def delete_ip(request):
    if request.method == 'POST':
        ip = request.POST.get('ip_address')
        if ip:
            IPAddress.objects.filter(ip_address=ip).delete()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})





#========================================================
from django.http import JsonResponse
from .models import IPAddress

def active_ips(request):
    active_ips = IPAddress.objects.filter(is_active=True).values_list('ip_address', flat=True)
    return JsonResponse({'active_ips': list(active_ips)})


#=====================16-02-2025======


def ip_stats(request):
    active_count = IPAddress.objects.filter(is_active=True).count()
    inactive_count = IPAddress.objects.filter(is_active=False).count()
    total_count = IPAddress.objects.count()

    data = {
        'active': active_count,
        'inactive': inactive_count,
        'total': total_count,
    }

    return JsonResponse(data)
