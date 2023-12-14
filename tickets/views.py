from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from item.models import Ticket

@login_required
def index(request):
    items = Ticket.objects.filter(owner=request.user)

    return render(request, 'tickets/index.html', {
        'items': items,
    })
