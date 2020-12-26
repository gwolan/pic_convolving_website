from django import forms
from .EffectType import EffectType


class ChooseEffectRadioForm(forms.Form):
    def __init__(self, effect_type, effect_label, *args, **kwargs):
        super(ChooseEffectRadioForm, self).__init__(*args, **kwargs)

        self.fields["pref-effect"] = forms.BooleanField(label=effect_label,
                                                        required=True,
                                                        widget=forms.CheckboxInput(attrs={
                                                            "type": "radio",
                                                            "id": effect_type}))


radio_list = list()
for key, value in EffectType.__members__.items():
    radio_list.append(ChooseEffectRadioForm(key, value.value[0]))

