from django.shortcuts import render
from django.http import HttpResponse


def index(request):


    context = {
        "licenses_count": 0,
        "comparison_count": 0,
        "is_dashboard": True
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
            context={
                "is_licenses": True
                }
            )


def comparisons(request):
    return render(
            request=request,
            template_name="comparison/comparison-list.html",
            context={
                "is_comparisons": True
                }
            )

def comparison_categories(request,comparison_event_id):
    return render(
            request=request,
            template_name="comparison/comparison-category-list.html",
            context={
                "is_comparisons": True,
                "comparison_event_id": comparison_event_id
                }
            )
