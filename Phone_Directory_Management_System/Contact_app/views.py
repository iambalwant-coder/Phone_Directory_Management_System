from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

# Create your views here.

def home(request):
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        contact_obj = Contact()
        contact_obj.first_name = first_name
        contact_obj.last_name = last_name
        contact_obj.phone_number = phone_number
        contact_obj.email = email
        contact_obj.save()
        messages.success(request, 'Contact added successfully.')
        return redirect('add_contact')
    return render(request, 'add_contact.html')

def delete_contact(request,id):
    delete = Contact.objects.get(pk=id)
    delete.delete()
    messages.success(request, 'Contact deleted successfully.')
    return redirect('view_all')

def view_all(request):
    contacts = Contact.objects.all()
    return render(request, 'view_all.html', {'contacts': contacts})

def edit(request,id):
    contact = Contact.objects.get(pk=id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        contact.first_name = first_name
        contact.last_name = last_name
        contact.phone_number = phone_number
        contact.email = email
        contact.save()
        messages.success(request, 'Contact updated successfully.')
        return redirect('view_all')

    return render(request,'edit_contact.html',{'contact':contact})

def trash(request):
    contacts = Contact.objects.all()
    return render(request, 'trash.html', {'contacts': contacts})
    