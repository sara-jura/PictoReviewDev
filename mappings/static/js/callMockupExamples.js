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
    '            {"max": 5, "name": "rel1", "min": 0,"weight":1},\n' +
    '            {"max": 5, "name": "rel2", "min": -5,"weight":1}\n' +
    '        ],\n' +
    '        "novelty": [\n' +
    '            {"max": 1, "name": "nov", "min": -1,"weight":1}\n' +
    '        ],\n' +
    '        "techQuality": [\n' +
    '            {"max": 5, "name": "tech", "min": 0,"weight":1}\n' +
    '        ],\n' +
    '        "stateOfArt": [\n' +
    '            {"max": 5, "name": "state", "min": 0,"weight":1}\n' +
    '        ],\n' +
    '        "evaluation": [\n' +
    '            {"max": 5, "name": "eval", "min": 0,"weight":1}\n' +
    '        ],\n' +
    '        "significance": [\n' +
    '            {"max": 5, "name": "sig", "min": 0,"weight":1}\n' +
    '        ],\n' +
    '        "presentation": [\n' +
    '            {"max": null, "name": "", "min": null,"weight":1}\n' +
    '        ],\n' +
    '          "confidence": [\n'+
    '            {"max": 5,"name": "conf","min": 0,"weight":1}\n' +
    '        ],\n'+
    '          "overallScore": [\n'+
    '            {"max": 5,"name": "oscore","min": 0,"weight":1}\n' +
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
    '            {"max": 5, "name": 0, "min": 0},\n' +
    '            {"max": 5, "name": 1, "min": -5}\n' +
    '        ],\n' +
    '        "novelty": [\n' +
    '            {"max": 1, "name": 2, "min": -1}\n' +
    '        ],\n' +
    '        "techQuality": [\n' +
    '            {"max": 5, "name": 3, "min": 0}\n' +
    '        ],\n' +
    '        "stateOfArt": [\n' +
    '            {"max": 5, "name": 4, "min": 0}\n' +
    '        ],\n' +
    '        "evaluation": [\n' +
    '            {"max": 5, "name": 5, "min": 0}\n' +
    '        ],\n' +
    '        "significance": [\n' +
    '            {"max": 5, "name": 6, "min": 0}\n' +
    '        ],\n' +
    '        "presentation": [\n' +
    '            {"max": null, "name": "", "min": null}\n' +
    '        ],\n' +
    '          "confidence": [\n'+
    '            {"max": 5,"name": 7, "min": 0}\n' +
    '        ],\n'+
    '          "overallScore": [\n'+
    '            {"max": 5,"name": 8,"min": 0}\n' +
    '       ]\n'+
    '    }\n' +
    '}';
var orderBody='"mappingsbody": {\n' +
    '        "1":[1, 2, 0, 3, 3, 2, 1,1,1],\n' +
    '        "2":[1, 2, 0, 3, 3, 2, 1,1,1]\n' +
    '    }';