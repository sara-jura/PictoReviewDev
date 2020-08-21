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

var fieldHead = `"mappingsheader":{
                       "orderMapping":false,
                       "mappings":{
                          "relevance":[
                             {
                                "name":"Appropriateness",
                                "min":1,
                                "max":5,
                                "weight":1
                             }
                          ],
                          "novelty":[
                             {
                                "name":"Originality / innovativeness",
                                "min":1,
                                "max":5,
                                "weight":1
                             }
                          ],
                          "techQuality":[
                             {
                                "name":"Implementation and soundness",
                                "min":1,
                                "max":5,
                                "weight":1
                             }
                          ],
                          "stateOfArt":[
                             {
                                "name":"Related work",
                                "min":1,
                                "max":5,
                                "weight":1
                             }
                          ],
                          "evaluation":[
                             {
                                "name":"Evaluation",
                                "min":1,
                                "max":5,
                                "weight":1
                             }
                          ],
                          "significance":[
                             {
                                "name":"Impact of ideas and results",
                                "min":1,
                                "max":5,
                                "weight":1
                             }
                          ],
                          "presentation":[
                             {
                                "name":"Clarity and quality of writing",
                                "min":1,
                                "max":5,
                                "weight":1
                             }
                          ],
                          "confidence":[
                             {
                                "name":"Reviewer's confidence",
                                "min":1,
                                "max":5,
                                "weight":1
                             }
                          ],
                          "overallScore":[
                             {
                                "name":"Overall evaluation",
                                "min":-2,
                                "max":2,
                                "weight":1
                             }
                          ]
                       }
                    }
`;
var fieldBody=`"mappingsbody":{
                  "rev1":{
                     "Appropriateness":4,
                     "Originality / innovativeness":3,
                     "Implementation and soundness":4,
                     "Related work":4,
                     "Evaluation":4,
                     "Impact of ideas and results":3,
                     "Clarity and quality of writing":3,
                     "Reviewer's confidence":3,
                     "Overall evaluation":0
                  },
                  "rev2":{
                     "Appropriateness":5,
                     "Originality / innovativeness":3,
                     "Implementation and soundness":3,
                     "Related work":3,
                     "Evaluation":3,
                     "Impact of ideas and results":3,
                     "Clarity and quality of writing":2,
                     "Reviewer's confidence":4,
                     "Overall evaluation":-1
                  },
                  "rev3":{
                     "Appropriateness":4,
                     "Originality / innovativeness":4,
                     "Implementation and soundness":3,
                     "Related work":3,
                     "Evaluation":4,
                     "Impact of ideas and results":3,
                     "Clarity and quality of writing":5,
                     "Reviewer's confidence":4,
                     "Overall evaluation":2
                  }
               }` ;

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