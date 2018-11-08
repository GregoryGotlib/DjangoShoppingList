from django.shortcuts import render,redirect
from .models import List
from django.contrib import messages
from .forms import ListForm

def home(request):
    # If i fill a form and add an item it will be a "POST" request
    if request.method == 'POST':

        # This will be the form that i just created
        form = ListForm(request.POST or None)

        # If the form is valid
        if form.is_valid():
            form.save()
            # Returns all the items i have in DB
            all_items = List.objects.all
            messages.success(request, ('Product has been added!'))
            return render( request,'shoppinglist/home.html',{ 'all_items': all_items})
        else:
          return redirect('home')
    else:
        all_items = List.objects.all
        return render( request,'shoppinglist/home.html',{ 'all_items': all_items})

# This function delete product from my list
def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,(item.item + ' has been deleted!'))

    # redirecting without sending data
    return redirect('home')

# This function sets added product to TRUE
def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.added = True
    item.save()
    return redirect('home')


# This function sets added product to FALSE
def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.added = False
    item.save()
    return redirect('home')

# This function enables  to edit product
def edit(request, list_id):
    item = List.objects.get(pk=list_id)

    if request.method == 'POST':
        form = ListForm(request.POST or None , instance=item)

        if form.is_valid():
            form.save()
            messages.success(request, ('Product has been edited!'))
            return redirect('home')

        else:
             return redirect('home')

    else:
         return render( request,'shoppinglist/edit.html',{ 'item': item })
