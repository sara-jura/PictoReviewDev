from django import forms
from django.forms import formset_factory


class RelevanceForm(forms.Form):
    relevance = forms.CharField(max_length=20,required=False)
    relevance_min = forms.IntegerField(required=False,label="min")
    relevance_max = forms.IntegerField(required=False,label="max")
    weight = forms.IntegerField(initial=1,required=False,label="weight")


class NoveltyForm(forms.Form):
    novelty = forms.CharField(max_length=20, required=False)
    novelty_min = forms.IntegerField(required=False,label="min")
    novelty_max = forms.IntegerField(required=False,label="max")
    weight = forms.IntegerField(initial=1,required=False,label="weight")


class TechQualityForm(forms.Form):
    techQuality = forms.CharField(max_length=20, required=False,label="Technical Quality")
    techQuality_min = forms.IntegerField(required=False,label="min")
    techQuality_max = forms.IntegerField(required=False,label="max")
    weight = forms.IntegerField(initial=1,required=False,label="weight")


class StateOfArtForm(forms.Form):
    stateOfArt = forms.CharField(max_length=20, required=False)
    stateOfArt_min = forms.IntegerField(required=False,label="min")
    stateOfArt_max = forms.IntegerField(required=False,label="max")
    weight = forms.IntegerField(initial=1,required=False,label="weight")


class EvaluationForm(forms.Form):
    evaluation = forms.CharField(max_length=20, required=False)
    evaluation_min = forms.IntegerField(required=False,label="min")
    evaluation_max = forms.IntegerField(required=False,label="max")
    weight = forms.IntegerField(initial=1,required=False,label="weight")


class SignificanceForm(forms.Form):
    significance = forms.CharField(max_length=20, required=False)
    significance_min = forms.IntegerField(required=False,label="min")
    significance_max = forms.IntegerField(required=False,label="max")
    weight = forms.IntegerField(initial=1,required=False,label="weight")


class PresentationForm(forms.Form):
    presentation= forms.CharField(max_length=20, required=False)
    presentation_min = forms.IntegerField(required=False,label="min")
    presentation_max = forms.IntegerField(required=False,label="max")
    weight = forms.IntegerField(initial=1,required=False,label="weight")


class ConfidenceForm(forms.Form):
    confidence= forms.CharField(max_length=20, required=False)
    confidence_min = forms.IntegerField(required=False,label="min")
    confidence_max = forms.IntegerField(required=False,label="max")
    weight = forms.IntegerField(initial=1,required=False,label="weight")


class OverallScoreForm(forms.Form):
    overallScore= forms.CharField(max_length=20, required=False)
    overallScore_min = forms.IntegerField(required=False,label="min")
    overallScore_max = forms.IntegerField(required=False,label="max")
    weight = forms.IntegerField(initial=1,required=False,label="weight")




RelevanceFormSet = formset_factory(RelevanceForm, extra=0, max_num=3, min_num=1, validate_max=True,validate_min=True)
NoveltyFormSet = formset_factory(NoveltyForm, extra=0, max_num=3,min_num=1,validate_max=True,validate_min=True)
TechQualityFormSet = formset_factory(TechQualityForm, extra=0, max_num=3,min_num=1,validate_max=True,validate_min=True)
StateOfArtFormSet = formset_factory(StateOfArtForm, extra=0, max_num=3,min_num=1,validate_max=True,validate_min=True)
EvaluationFormSet = formset_factory(EvaluationForm, extra=0, max_num=3,min_num=1,validate_max=True,validate_min=True)
SignificanceFormSet = formset_factory(SignificanceForm, extra=0, max_num=3,min_num=1,validate_max=True,validate_min=True)
PresentationFormSet = formset_factory(PresentationForm, extra=0, max_num=3,min_num=1,validate_max=True,validate_min=True)
ConfidenceFormSet = formset_factory(ConfidenceForm, extra=0, max_num=3,min_num=1,validate_max=True,validate_min=True)
OverallScoreFormSet = formset_factory(OverallScoreForm, extra=0, max_num=3,min_num=1,validate_max=True,validate_min=True)


class CallMockupForm(forms.Form):
    JSON_header= forms.CharField(widget=forms.Textarea)
    JSON_body = forms.CharField(widget=forms.Textarea)
    JSON_header.widget.attrs.update({'class': 'form-control'})
    JSON_body.widget.attrs.update({'class': 'form-control'})