$(document).ready(function () {
$('#orderExampleButton').click(function () {
  $('#id_JSON_header').val(orderHead);
  $('#id_JSON_body').val(orderBody);
});
$('#fieldNamesExampleButton').click(function () {
  $('#id_JSON_header').val(fieldHead);
  $('#id_JSON_body').val(fieldBody);
});


});

var fieldHead = '"mappingsheader": {\n' +
    '    "orderMapping": false,\n' +
    '    "mappings": {\n' +
    '        "relevance": [\n' +
    '            {"name": "rel1", "min": 0, "max": 5, "weight": 2},\n' +
    '            {"name": "rel2", "min": -5, "max": 5, "weight": 1}\n' +
    '        ],\n' +
    '        "novelty": [\n' +
    '            {"name": "nov", "min": -1, "max": 1, "weight": 1}\n' +
    '        ],\n' +
    '        "techQuality": [\n' +
    '            {"name": "tech", "min": 0, "max": 5, "weight": 1}\n' +
    '        ],\n' +
    '        "stateOfArt": [\n' +
    '            {"name": "state", "min": 0, "max": 5, "weight": 1}\n' +
    '        ],\n' +
    '        "evaluation": [\n' +
    '            {"name": "eval", "min": 0, "max": 5, "weight": 1}\n' +
    '        ],\n' +
    '        "significance": [\n' +
    '            {"name": "sig", "min": 0, "max": 5, "weight": 1}\n' +
    '        ],\n' +
    '        "presentation": [\n' +
    '            {"name": "", "min": null, "max": null, "weight": 1}\n' +
    '        ],\n' +
    '          "confidence": [\n'+
    '            {"name": "conf", "min": 0, "max": 5, "weight": 1}\n' +
    '        ],\n'+
    '          "overallScore": [\n'+
    '            {"name": "oscore", "min": 0, "max": 5, "weight": 1}\n' +
    '       ]\n'+
    '    }\n' +
    '}';
var fieldBody= '"mappingsbody":{\n' +
    '\t\t"rev1":{"rel1": 1, "rel2": 2, "nov": 0, "tech": 3, "state": 3, "eval": 2, "sig": 1,"conf": 1,"oscore": 1},\n' +
    '\t\t"rev2":{"rel1": 1, "rel2": 2, "nov": 0, "tech": 3, "state": 3, "eval": 2, "sig": 1,"conf": 1,"oscore": 1}\n' +
    '\t\t}';

var  orderHead = '"mappingsheader": {\n' +
    '    "orderMapping": true,\n' +
    '    "mappings": {\n' +
    '        "relevance": [\n' +
    '            {"name": 0, "min": 0, "max": 5, "weight": 2},\n' +
    '            {"name": 1, "min": -5, "max": 5, "weight": 1}\n' +
    '        ],\n' +
    '        "novelty": [\n' +
    '            {"name": 2, "min": -1, "max": 1, "weight": 1}\n' +
    '        ],\n' +
    '        "techQuality": [\n' +
    '            {"name": 3, "min": 0, "max": 5, "weight": 1}\n' +
    '        ],\n' +
    '        "stateOfArt": [\n' +
    '            {"name": 4, "min": 0, "max": 5, "weight": 1}\n' +
    '        ],\n' +
    '        "evaluation": [\n' +
    '            {"name": 5, "min": 0, "max": 5, "weight": 1}\n' +
    '        ],\n' +
    '        "significance": [\n' +
    '            {"name": 6, "min": 0, "max": 5, "weight": 1}\n' +
    '        ],\n' +
    '        "presentation": [\n' +
    '            {"name": "", "min": null, "max": null, "weight": null}\n' +
    '        ],\n' +
    '          "confidence": [\n'+
    '            {"name": 7, "min": 0, "max": 5, "weight": 1}\n' +
    '        ],\n'+
    '          "overallScore": [\n'+
    '            {"name": 8, "min": 0, "max": 5, "weight": 1}\n' +
    '       ]\n'+
    '    }\n' +
    '}';
var orderBody='"mappingsbody": {\n' +
    '        "1":[1, 2, 0, 3, 3, 2, 1 ,1 ,1],\n' +
    '        "2":[1, 2, 0, 3, 3, 2, 1, 1, 1]\n' +
    '    }';