from django import forms

class MonedaForm(forms.Form):
    pais = forms.CharField(label="País")
    continente = forms.CharField(label="Continente")
    valor = forms.CharField(label="Valor")  
    year = forms.IntegerField(label="Año")
    material = forms.CharField(label="Material")
    forma = forms.CharField(label="Forma")
    descripcion = forms.CharField(label="Descripción")
    imgfrente = forms.ImageField(label="Imagen frente")
    imgdorso = forms.ImageField(label="Imagen dorso")


    
class BilleteForm(forms.Form):
    pais = forms.CharField(label="País")
    continente = forms.CharField(label="Continente")
    valor = forms.CharField(label="Valor")  
    year = forms.IntegerField(label="Año")
    material = forms.CharField(label="Material")
    descripcion = forms.CharField(label="Descripción")
    imgfrente = forms.ImageField(label="Imagen frente")
    imgdorso = forms.ImageField(label="Imagen dorso")
    
class EstampillaForm(forms.Form):
    pais = forms.CharField(label="País")
    valor = forms.CharField(label="Valor")  
    year = forms.IntegerField(label="Año")
    descripcion = forms.CharField(label="Descripción")
    forma = forms.CharField(label="Forma")
    imgfrente = forms.ImageField(label="Imagen frente")

class FichayMedallaForm(forms.Form):
    tipodeobjeto = forms.CharField()
    pais = forms.CharField(label="País")
    valor = forms.CharField(label="Valor")  
    year = forms.IntegerField(label="Año")
    descripcion = forms.CharField(label="Descripción")
    forma = forms.CharField(label="Forma")
    imgfrente = forms.ImageField(label="Imagen frente")
    imgdorso = forms.ImageField(label="Imagen dorso")
