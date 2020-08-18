from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import *
import json

# Create your views here.
@csrf_exempt
def index(request):

    try:
        data=json.loads(request.body)

        metrics=getMetrics(data["mappingsheader"]["mappings"],data["mappingsbody"],list(data["mappingsheader"]["mappings"].keys()))
        return JsonResponse(metrics,  json_dumps_params={'indent': 2},safe=False)
    except:
         return JsonResponse({'Error': "Something went wrong with the mapping, try checking the validity of your values"}, status=500)


