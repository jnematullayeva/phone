from django.shortcuts import render, redirect, get_object_or_404
from .models import Phones
from .forms import Phone


def phone_list(request):
    phones = Phones.objects.all()
    return render(request, 'crud/phone_list.html', {'phones': phones})


def phones_add(request):
    if request.method == 'POST':
        form = Phone(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('phone_list')
    else:
        form = Phone()
    return render(request, 'crud/phone_add.html', {'form': form})


def phone_update(request, pk):
    phone = get_object_or_404(Phones, pk=pk)
    if request.method == 'POST':
        form = Phone(request.POST, request.FILES, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('phone_list')
    else:
        form = Phone(instance=phone)
    return render(request, 'crud/phone_update.html', {'form': form, 'phone': phone})


def phone_delete(request, pk):
    phone = get_object_or_404(Phones, pk=pk)
    if request.method == 'POST':
        phone.delete()
        return redirect('phone_list')
    return render(request, 'crud/phone_delete.html', {'phone': phone})
