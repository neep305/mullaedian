from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404

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
    place_info = get_object_or_404(Place, pk=shop_id)

    return render(request, 'places/index.html', {'place_info': place_info})
