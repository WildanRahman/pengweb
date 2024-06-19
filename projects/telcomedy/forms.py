from django import forms 
from .models import * 

class DataMeme(forms.ModelForm):
    class Meta:
        model = Data_Comedy
        exclude = ()
        fields = '__all__'
        error_message = {
            'judul' : {
                'required' : 'judul harus diisi'
            }
        }

class DataPengguna(forms.ModelForm):
    class Meta:
        model = Data_Pengguna
        exclude = ()
        fields = '__all__'
        error_message = {
            'email' : {
                'required' : 'Email harus diisi'
            }
        }