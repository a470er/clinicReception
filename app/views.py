from django.views.generic import View
from django.shortcuts import render
from .models import GlobalStatus

# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        globalstatus_data = GlobalStatus.objects.order_by("created")
        return render(request, 'app/index.html', {
            'globalstatus': globalstatus_data,
        })