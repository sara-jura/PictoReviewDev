from django.http import HttpResponse
from .forms import *
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.conf import settings
from .utils import createGraph
import requests
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string

def index(request):
    return render(request, 'mappings/index.html')


def defineMappings(request):
    metrics = {
        'relevance': 'Relevance',
        'novelty': 'Novelty',
        'techQuality': 'Technical Quality',
        'stateOfArt': 'State of Art',
        'evaluation': 'Evaluation',
        'significance': 'Significance',
        'presentation': 'Presentation',
        'confidence': 'Confidence',
        'overallScore': 'Overall Score'
    }
    if request.method == 'POST':
        formsets = []
        for key in metrics:
            formsets.append(MetricFormset(request.POST, form_kwargs={'metric': metrics[key]}, prefix=key))
        form = IRIForm(request.POST)
        if(form.is_valid()):
            form_IRI= form.cleaned_data.get("field_iri")
            if form_IRI=="":
                form_IRI= settings.MAPPINGS_URL+get_random_string(8).lower()
            save_id=get_random_string(8).lower()
            g = createGraph(formsets, form_IRI)
            #default_storage.save(get_random_string(8).lower(),ContentFile(g.serialize(format='turtle')))
            response = HttpResponse(g.serialize(format='turtle'), content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename="mapping.ttl"'
            return response
    formsets = []
    form=IRIForm
    for key in metrics:
        formsets.append(MetricFormset(form_kwargs={'metric': metrics[key]}, prefix=key))
    return render(request, 'mappings/formset.html', {'formsets': formsets,"form":form})


def uploadReviews(request):
    if request.method == 'POST':
        form = CallMockupForm(request.POST)

        if form.is_valid():
            try:
                json_head = form['JSON_header'].value()
                json_body = form['JSON_body'].value()
                contents = '{' + json_head + ',' + json_body + '}'
                json_data=json.loads(contents)
            except:
                message = {
                    'Error': 'Something went wrong, perhaps the data wasn\'t in the right format?'}
                status = 500
                return JsonResponse(message, status=status, json_dumps_params={'indent': 2})
            response = requests.post(request.build_absolute_uri("/metricsTransformer"), json=json_data)
            return JsonResponse(response.json(), safe=False, json_dumps_params={'indent': 2})
            # try:
            #     json_head = form['JSON_header'].value()
            #     json_body = form['JSON_body'].value()
            #     contents = '{' + json_head + ',' + json_body + '}'
            #     response = requests.post('http://'+str(request.get_host())+"/metricsTransformer", json=json.loads(contents))
            #     message = response.json()
            #     status = 200
            #     return JsonResponse(response.json(), safe=False, json_dumps_params={'indent': 2})
            # except:
            #     message = {'message': 'Something went wroong, perhaps the data wasn\'t in the right format?'+'http://'+str(request.get_host())+"/metricsTransformer"}
            #     status = 500
            # finally:
            #     return JsonResponse(message, status=status)

    else:
        form = CallMockupForm()
        return render(request, 'mappings/callMockup.html', {'form': form})


def dumpFile(request,conf_prefix):
    return HttpResponse(default_storage.open(conf_prefix),content_type="text/plain")
