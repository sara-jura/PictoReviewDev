from django.http import HttpResponse
from .forms import *
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.conf import settings
from .utils import createGraph
import requests


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
        'overallScore': 'Overall score'
    }
    if request.method == 'POST':
        formsets = []
        for key in metrics:
            formsets.append(MetricFormset(request.POST, form_kwargs={'metric': metrics[key]}, prefix=key))

        g = createGraph(formsets)

        response = HttpResponse(g.serialize(format='turtle'), content_type='application/force-download')
        response['Content-Disposition'] = 'attachment; filename="mapping.rdf"'
        return response
    formsets = []
    for key in metrics:
        formsets.append(MetricFormset(form_kwargs={'metric': metrics[key]}, prefix=key))
    return render(request, 'mappings/formset.html', {'formsets': formsets})


def uploadReviews(request):
    if request.method == 'POST':
        form = CallMockupForm(request.POST)
        if form.is_valid():
            try:
                json_head = form['JSON_header'].value()
                json_body = form['JSON_body'].value()
                contents = '{' + json_head + ',' + json_body + '}'
                response = requests.post(settings.API_URL, json=json.loads(contents))
                message = response.json()
                status = 200
                return JsonResponse(response.json(), safe=False, json_dumps_params={'indent': 2})
            except:
                message = {'message': 'Something went wrong, perhaps the data wasn\'t in the right format?'}
                status = 500
            finally:
                return JsonResponse(message, status=status)

    else:
        form = CallMockupForm()
        return render(request, 'mappings/callMockup.html', {'form': form})
