from rdflib import Literal, Graph, Namespace
from rdflib.namespace import RDF, RDFS
from django.utils.crypto import get_random_string
from django.conf import settings


def createGraph(formsets):
    g = Graph()
    form_id = get_random_string(8).lower()
    new = Namespace("http://example.org/mappings/" + form_id + "#")
    picr = Namespace(settings.MAPPINGS_URL + 'picr/')
    papeval = Namespace(settings.MAPPINGS_URL + 'papeval/')
    g.bind(form_id, new)
    g.bind('picr', picr)
    g.bind('papeval', papeval)
    for fs in formsets:
        if fs.is_valid():
            for f in fs:
                cd = f.cleaned_data
                fieldNode = new[cd.get("field_name").title().replace(" ", "")]
                mappingNode = new[cd.get("field_name").title().replace(" ", "") + "2" + f.metric.replace(" ", "")]
                g.add((fieldNode, RDF.type, picr.ReviewFormCriterion))
                g.add((fieldNode, picr.weight, Literal(cd.get("field_weight"))))
                g.add((fieldNode, picr.minVal, Literal(cd.get("field_min"))))
                g.add((fieldNode, picr.maxVal, Literal(cd.get("field_max"))))
                g.add((fieldNode, RDFS.label, Literal(cd.get("field_name"))))
                g.add((mappingNode, RDF.type, picr.F2M_Mapping))
                g.add((mappingNode, picr['fieldOfMapping'], fieldNode))
                g.add((mappingNode, picr.metricOfMapping, papeval[f.metric.replace(" ", "")]))
                g.add((mappingNode, picr.mappingOf, new['']))
    g.add((new[''],RDF.type,picr.ReviewForm))
    return g
