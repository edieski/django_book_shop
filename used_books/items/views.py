from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Item
from .forms import NewItemForm, EditItemForm

def detail(request, pk):

    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'items/detail.html', {
        'item':item,
        'related_items':related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
    
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            files = request.FILES  # multivalued dict
            image = files.get("image")
            item.image = image
            item.save()

            return redirect('items:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'items/form.html',  
                  {'form' : form,
                           'title': 'New item', })

@login_required
def delete(request, item_id):
    item = get_object_or_404(Item, pk=item_id, created_by=request.user)
    item.delete()
    return redirect('dashboard:dashboard')
@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
    
        form = NewItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            item = form.save(commit=False)
            files = request.FILES  # multivalued dict
            image = files.get("image")
            item.image = image
            item.save()

            return redirect('items:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'items/form.html',  
                  {'form' : form,
                           'title': 'New item', })
