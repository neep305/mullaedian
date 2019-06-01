from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Place

# Create your views here.
def index(request):
    # return render(request,'places/index')
    place_list = Place.objects.order_by('-reg_date')[:]
    # output = ', '.join([p.restaurant for p in place_list])

    # template = loader.get_template('places/index.html')
    context = {
        'place_list': place_list,
    }
    # return HttpResponse('Hello This is Places page %s' % output)
    # return HttpResponse(template.render(context, request))
    return render(request, 'places/index.html', context)

def detail(request, shop_id):
    try:
        place_info = Place.object.get(pk=shop_id)
    except:
        raise Http404("Place info doesn't exist")
    # return HttpResponse('Shop Id is %s.' % shop_id)
    return render(request, 'places/index.html', {'place_info': place_info})