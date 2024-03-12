from django.shortcuts import render
from app_legends import models


def main_view(request):

    magic_groups = models.MagicGroup.objects.all().order_by('id')

    context = {
        'magic_groups': magic_groups
    }

    return render(request, 'main/pages/home.html', context)