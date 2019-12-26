from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import *
import json

# Create your views here.
@csrf_exempt
def index(request):
    """return JsonResponse(request.body,safe=False)
     return JsonResponse({"ahoj":"ahoj"},safe=False)"""
    try:
        data=json.loads(request.body)
        metrics=getMetrics(data["mappingsheader"]["mappings"],data["mappingsbody"],list(data["mappingsheader"]["mappings"].keys()))
        return JsonResponse(metrics,  json_dumps_params={'indent': 2},safe=False)
    except:
         JsonResponse({'status': 'false', 'message': "Something went wrong, perhaps the data wasn't in the right format?"}, status=500)


