from django.http import HttpResponse
from .forms import *
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core import serializers
import json
from django.middleware.csrf import get_token
from rdflib import URIRef, BNode, Literal,Graph,Namespace
from rdflib.namespace import RDF, FOAF
from django.conf import settings

import requests


def index(request):
    return render(request,"mappings/index.html")


def defineMappings(request):
    if request.method == 'POST':
        relFormset=RelevanceFormSet(request.POST,prefix="relevance")
        if relFormset.is_valid():
            string = ""
            g = Graph()
            n = Namespace("http://schema.org/")
            for f in relFormset:
                cd = f.cleaned_data

                relevance=BNode()
                g.add((relevance,RDF.type,n.Rating))
                g.add((relevance,n.reviewAspect,Literal("relevance")))
                g.add((relevance,n.bestRating,Literal(cd.get("relevance_max"))))
                g.add((relevance,n.worstRating,Literal(cd.get("relevance_min"))))
                g.bind("schema",n)
            response=HttpResponse(g.serialize(format='turtle'),content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename="mapping.rdf"'
            return response

    formsets = {
        'relevanceFormset':RelevanceFormSet(prefix='relevance'),
        'noveltyFormset':NoveltyFormSet(prefix='novelty'),
        'techQualityFormset':TechQualityFormSet(prefix="techQuality"),
        'stateOfArtFormset':StateOfArtFormSet(prefix="stateOfArt"),
        'evaluationFormset':EvaluationFormSet(prefix="evaluation"),
        'significanceFormset':SignificanceFormSet(prefix="significance"),
        'presentationFormset':PresentationFormSet(prefix="presentation"),
        'confidenceFormset':ConfidenceFormSet(prefix="confidence"),
        'overallScoreFormset':OverallScoreFormSet(prefix="overallScore"),
        }
    return render(request, 'mappings/formset.html', {'formsets': formsets})

def uploadReviews(request):
    if request.method == "POST":
        form=CallMockupForm(request.POST)
        if form.is_valid():
            try:
                json_head = form["JSON_header"].value()
                json_body=form["JSON_body"].value()
                contents= "{"+json_head+","+json_body+"}"
                response=requests.post(settings.API_URL, json=json.loads(contents))
                message=response.json()
                status = 200
                return JsonResponse(response.json(),safe=False, json_dumps_params={'indent': 2})
            except:
                message={"message":"Something went wrong, perhaps the data wasn't in the right format?"}
                status=500
            finally:
                return JsonResponse(message, status=status)

    else:
        form= CallMockupForm()
        return render (request,"mappings/callMockup.html",{'form': form})

