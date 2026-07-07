from django.shortcuts import redirect, render, HttpResponse, get_object_or_404
from .models import Item
from .forms import Itemform
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.exceptions import PermissionDenied
# Create your views here.

def home(request):
    query = request.GET.get('q')

    items = Item.objects.exclude(status='C')

    if query:
        items = items.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(location__icontains=query)
        )
    
    items = items.order_by('-created_at')
    return render(request, "home.html", context={'items': items})

@login_required
def lost(request):
    if request.method == 'POST':
        form = Itemform(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()

            return redirect('home')
    else:
        form = Itemform()
    return render(request, "lostitemreg.html", context={'form': form})

def found(request):
    items = Item.objects.filter(status='F')
    items = items.order_by('-created_at')
    return render(request, "founditem.html", context={'items': items})

def lost_items(request):
    items = Item.objects.filter(status='L').order_by('-created_at')
    return render(request, "lostitem.html", context={'items': items})

@login_required
def dashboard(request):
    items = Item.objects.filter(user=request.user).order_by('-created_at')
    return render(request, "dashboard.html", context={'items': items})

@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if item.user != request.user:
        raise PermissionDenied("You do not have permission to edit this item.")
    
    if request.method == 'POST':
        form = Itemform(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = Itemform(instance=item)
    return render(request, "lostitemreg.html", context={'form': form, 'is_edit': True, 'item': item})

@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if item.user != request.user:
        raise PermissionDenied("You do not have permission to delete this item.")
    
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard')
    return redirect('dashboard')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Auto-logs user in upon successful sign-up
            return redirect('home')  # Change to your landing redirect url
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def claimed(request):
    items = Item.objects.filter(status='C').order_by('-created_at')
    return render(request, "claimeditem.html", context={'items': items})

@login_required
def claim_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.status = 'C'
        item.claimed_by = request.user
        item.save()
        next_url = request.META.get('HTTP_REFERER', 'home')
        return redirect(next_url)
    return redirect('home')

def setup_db(request):
    from django.core.management import call_command
    from django.contrib.auth.models import User
    from django.http import HttpResponse
    try:
        call_command('migrate')
        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            return HttpResponse("Database migrated and superuser created (admin / admin123). Please delete this endpoint after use for security!")
        return HttpResponse("Database migrated successfully. Superuser already exists.")
    except Exception as e:
        return HttpResponse(f"Error setting up database: {str(e)}")