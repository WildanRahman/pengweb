from django import forms 
from .models import * 

class DataBerita(forms.ModelForm):
    class Meta:
        model = Data_Berita
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