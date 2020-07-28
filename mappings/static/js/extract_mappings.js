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

            }
        };


        $.each(data, function (key, value) {
                var baseReg =  "^[a-zA-Z]+-[0-9]-field";
                var reg = new RegExp(baseReg + "_name$");
                if (reg.test(key)) {
                    field_base=key.match(baseReg);
                    metric=key.match("^[a-zA-Z]+");
                    if(!(metric in groupedData["mappings"]))
                        groupedData["mappings"][metric]=[];
                    (groupedData["mappings"][metric]).push({
                        "max": parseInt(data[field_base + "_max"]),
                        "name": (groupedData.orderMapping) ? parseInt(value) :value,
                        "min": parseInt(data[field_base  + "_min"]),
                        "weight": parseInt(data[field_base + "_weight"])


                    })
                }
            });

        var finalData = JSON.stringify(groupedData, null, 2)
        $('#json-header').empty();
        $('#json-header').append('"mappingsheader":' +finalData)

    });
});