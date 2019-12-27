from django import forms
from django.forms import formset_factory


class MetricForm(forms.Form):
    def __init__(self, *args, metric="metric", **kwargs):
        self.metric=metric
        super().__init__(*args, **kwargs)
        self.fields['field_name'].label = metric

    field_name = forms.CharField(max_length=20, required=False)
    field_min = forms.IntegerField(required=False, label="min")
    field_max = forms.IntegerField(required=False, label="max")
    field_weight = forms.IntegerField(initial=1, required=False, label="weight")


def generateFormset():
    return formset_factory(MetricForm, extra=0, max_num=3, min_num=1, validate_max=True, validate_min=True)


MetricFormset=generateFormset()


class CallMockupForm(forms.Form):
    JSON_header = forms.CharField(widget=forms.Textarea)
    JSON_body = forms.CharField(widget=forms.Textarea)
    JSON_header.widget.attrs.update({'class': 'form-control'})
    JSON_body.widget.attrs.update({'class': 'form-control'})
