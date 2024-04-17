from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.conf import settings

# 3rd party apps
from render_block import render_block_to_string
from utils.htmx_patterns.utils import for_htmx

from .models import Voucher

app_name = __package__


# Create your views here.
def voucher_list(request):

    qs = Voucher.objects.all()

    # get the meta data for user permissions
    model_app = qs.model._meta.app_label
    model_name = qs.model._meta.model_name
    app_model = f'{model_app}-{model_name}'

    context = {
        'object_list': qs,
        'tz': settings.TIME_ZONE
    }

    template = f'{app_name}/{ model_name}/list.html'

    # if via htmx, display only the appropriate template block
    if request.htmx:
        
        block = request.GET.get('use_block', f'{app_model}-list')

        html = render_block_to_string(template, block, context)
        return HttpResponse(html)
    
    # else display the whole page which includes the extended base.html
    else:
        return render(request, template, context)


@for_htmx(use_block_from_params=True)
def voucher_list_viaTemplateResponse(request):

    qs = Voucher.objects.all()

    model_name = qs.model._meta.model_name

    context = {
        'object_list': qs,
    }

    template = f'{app_name}/{ model_name}/list.html'

    return TemplateResponse(request, template, context)