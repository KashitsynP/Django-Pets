from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponseRedirect

from pets.models import User, Pet
from pets.forms import AddUser, AddPet

def index(request):
    return render(request, 'index.html')

def add_user(request):
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AddUser()
    return render(request, 'add_user.html', {'form': form})


def add_pet(request):
    if request.method == 'POST':
        form = AddPet(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = AddPet()
    return render(request, 'add_pet.html', {'form': form})

# def all_users(request):
#     users = User.objects.prefetch_related('pets').all()
#     return render(request, 'all_users.html', {'users': users})

# def all_users(request):
#     # Получаем всех пользователей с их питомцами
#     users_with_pets = User.objects.prefetch_related('pets').all()    
#     return render(request, 'all_users.html', {'users_with_pets': users_with_pets})

def owner_list(request):
    owners = User.objects.all()
    return render(request, 'owner_list.html', {'owners': owners})

def owner_pets(request, owner_id):
    owner = User.objects.get(pk=owner_id)
    pets = owner.pets.all()
    return render(request, 'owner_pets.html', {'owner': owner, 'pets': pets})

def all_pets(request):
    pets = Pet.objects.all()
    return render(request, 'all_pets.html', {'pets': pets})
    
def Page_not_found(request, exception):
    return HttpResponseNotFound('<h1> Страница к котрой вы обратились не существует</h1>')
