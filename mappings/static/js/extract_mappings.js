$(document).ready(function () {

    $("#submit-json").click(function (e) {
        // prevent from normal form behaviour
        console.log();
        e.preventDefault();
        // serialize the form data
        var data = $("#mappings-form").serializeArray().reduce(function (obj, item) {
            obj[item.name] = item.value;
            return obj;
        }, {});

        var groupedData = {
            orderMapping : !!$('#order-chckbx').is(':checked'),
            mappings:{
            relevance: [],
            novelty: [],
            techQuality: [],
            stateOfArt: [],
            evaluation: [],
            significance: [],
            presentation: [],
            confidence: [],
            overallScore: [],
            }
        };


        $.each(data, function (key, value) {
            $.each(prefixes, function (prefixName, prefixValue) {
                var baseReg = prefixValue + "-[0-9]-" + prefixValue;
                var reg = new RegExp(baseReg + "$")
                if (reg.test(key)) {
                    (groupedData["mappings"][prefixValue]).push({
                        "max": parseInt(data[key + "_max"]),
                        "name": (groupedData.orderMapping) ? parseInt(value) :value,
                        "min": parseInt(data[key + "_min"]),
                        "weight": parseInt(data[key + "_weight"])


                    })
                }
            });
        });
        var finalData = JSON.stringify(groupedData, null, 2)
        $('#json-header').empty();
        $('#json-header').append('"mappingsheader":' +finalData)

    });
});