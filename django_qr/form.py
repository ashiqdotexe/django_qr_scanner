from django import forms

class QRGenerator(forms.Form):
    retaurent_name = forms.CharField(
        max_length=25,
        label="Restaurent name",
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "plceholder":"Please insert retaurent name",
        })
    )
    url = forms.URLField(
        max_length=256,
        label="URL",
        widget=forms.URLInput(attrs={
            "class":"form-control",
            "plceholder":"Please insert URL name",
        })
    )
    
                                    