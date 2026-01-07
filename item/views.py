from django.shortcuts import render, get_object_or_404
from .models import Item

def item_detail(requeest, pk):
    item = get_object_or_404(Item, pk=pk)
    
    return (requeest, "details.html",
            {
              'item': item
            })
