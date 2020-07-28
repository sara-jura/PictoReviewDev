from rdflib import Literal, Graph, Namespace
from rdflib.namespace import RDF, RDFS
from django.conf import settings

def createGraph(formsets,form_iri):
    g = Graph()

    new = Namespace(form_iri + "#")
    picr = Namespace('http://kizi.vse.cz/pictoreview/ontology#')
    metrics = Namespace('http://kizi.vse.cz/pictoreview/metrics#')
    g.bind('form', new)
    g.bind('picr', picr)
    g.bind('metrics', metrics)
    for fs in formsets:
        if fs.is_valid():
            for f in fs:
                cd = f.cleaned_data

                mappingNode = new[cd.get("field_name").title().replace(" ", "") + "2" + f.metric.replace(" ", "")]

                fieldNode = new[cd.get("field_name").title().replace(" ", "")]
                if not (fieldNode, None, None) in g:
                    g.add((fieldNode, RDF.type, picr.ReviewFormField))
                    g.add((fieldNode, picr.minVal, Literal(cd.get("field_min") if cd.get("field_min") is not None else 0)))
                    g.add((fieldNode,picr.fieldOf,new['']))
                    g.add((fieldNode, picr.maxVal, Literal(cd.get("field_max") if cd.get("field_max") is not None else 0)))
                    g.add((fieldNode, RDFS.label, Literal(cd.get("field_name"))))
                g.add((mappingNode, RDF.type, picr.F2M_Mapping))
                g.add((mappingNode, picr['fieldOfMapping'], fieldNode))
                g.add((mappingNode, picr.metricOfMapping, metrics[f.metric.replace(" ", "")]))
                g.add((mappingNode, picr['weightOfMapping'], Literal(cd.get("field_weight") if cd.get("field_weight") is not None else 0 )))
                #g.add((mappingNode, picr.mappingOf, new['']))
    g.add((new[''],RDF.type,picr.ReviewForm))
    return g
