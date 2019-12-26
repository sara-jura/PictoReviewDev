
        $(function () {
            $('.noveltyFormset').formset({
                formCssClass: prefixes.noveltyPrefix+'-form',
                addCssClass: prefixes.noveltyPrefix+'-form-add',
                deleteCssClass: prefixes.noveltyPrefix+'-form-rem',
                prefix: prefixes.noveltyPrefix
            });

            $('.relevanceFormset').formset({
                formCssClass: prefixes.relevancePrefix+'-form',
                addCssClass: prefixes.relevancePrefix+'-form-add',
                deleteCssClass: prefixes.relevancePrefix+'-form-rem',
                prefix: prefixes.relevancePrefix
            });
            $('.techQualityFormset').formset({
                formCssClass: prefixes.techQualityPrefix+'-form',
                addCssClass: prefixes.techQualityPrefix+'-form-add',
                deleteCssClass: prefixes.techQualityPrefix+'-form-rem',
                prefix: prefixes.techQualityPrefix
            });
            $('.stateOfArtFormset').formset({
                formCssClass: prefixes.stateOfArtPrefix+'-form',
                addCssClass: prefixes.stateOfArtPrefix+'-form-add',
                deleteCssClass: prefixes.stateOfArtPrefix+'-form-rem',
                prefix: prefixes.stateOfArtPrefix
            });
            $('.evaluationFormset').formset({
                formCssClass: prefixes.evaluationPrefix+'-form',
                addCssClass: prefixes.evaluationPrefix+'-form-add',
                deleteCssClass: prefixes.evaluationPrefix+'-form-rem',
                prefix: prefixes.evaluationPrefix
            });
            $('.significanceFormset').formset({
                formCssClass: prefixes.significancePrefix+'-form',
                addCssClass: prefixes.significancePrefix+'-form-add',
                deleteCssClass: prefixes.significancePrefix+'-form-rem',
                prefix: prefixes.significancePrefix
            });
            $('.presentationFormset').formset({
                formCssClass: prefixes.presentationPrefix+'-form',
                addCssClass: prefixes.presentationPrefix+'-form-add',
                deleteCssClass: prefixes.presentationPrefix+'-form-rem',
                prefix: prefixes.presentationPrefix
            });
            $('.confidenceFormset').formset({
                formCssClass: prefixes.confidencePrefix+'-form',
                addCssClass: prefixes.confidencePrefix+'-form-add',
                deleteCssClass: prefixes.confidencePrefix+'-form-rem',
                prefix: prefixes.confidencePrefix
            });
            $('.overallScoreFormset').formset({
                formCssClass: prefixes.overallScorePrefix+'-form',
                addCssClass: prefixes.overallScorePrefix+'-form-add',
                deleteCssClass: prefixes.overallScorePrefix+'-form-rem',
                prefix: prefixes.overallScorePrefix
            });
        }) ;