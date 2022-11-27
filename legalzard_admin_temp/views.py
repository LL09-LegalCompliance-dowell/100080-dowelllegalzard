from django.shortcuts import render
from django.http import HttpResponse


def index(request):


    context = {
        "licenses_count": 0,
        "comparison_count": 0,
    }
    return render(
            request=request,
            template_name="dashboard/index.html",
            context=context
            )



def licenses(request):
    return render(
            request=request,
            template_name="licenses/license-list.html",
            context={}
            )


def comparisons(request):
    return render(
            request=request,
            template_name="comparison/comparison-list.html",
            context={}
            )
