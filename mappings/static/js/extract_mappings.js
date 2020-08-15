$(document).ready(function () {

    $("#submit-json").click(function (e) {
        // prevent from normal form behaviour
         $('#error-div').addClass('d-none')
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

        var errorFlag=false
        $.each(data, function (key, value) {
                var baseReg =  "^[a-zA-Z]+-[0-9]-field";
                var reg = new RegExp(baseReg + "_name$");
                if (reg.test(key)) {
                    field_base=key.match(baseReg);
                    max=parseInt(data[field_base + "_max"])
                    min=parseInt(data[field_base  + "_min"])
                    weight=parseInt(data[field_base + "_weight"])
                    name=(groupedData.orderMapping) ? parseInt(value) :value
                    if (value && (isNaN(max) || isNaN(min) || isNaN(weight) )) {
                        $('#error-div').removeClass('d-none')
                        $('#error-div').html("You ńeed to include min/max/weight values for each metric you wish to map.")
                        errorFlag=true
                        return false
                    }
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
        if (errorFlag) return
        var finalData = JSON.stringify(groupedData, null, 2)
        $('#json-header').empty();
        $('#json-header').append('"mappingsheader":' +finalData)

    });
});