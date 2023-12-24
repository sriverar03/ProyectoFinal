from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm,UserModel


class PerfilFormulario(forms.ModelForm):
    class Meta:
        model = models.Perfil
        fields =["descripcion", "usuario"]
    
        widgets = {
            "descripcion":forms.TextInput(attrs={'class': 'form-control'}),                            
            "usuario" :forms.Select(attrs={'class':'form-control'}),
            "imagen" : forms.FileInput(attrs={'class':'form-control'})            
        }

class BlogFormulario(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields =["titulo", "subtitulo", "contenido","autor","imagen"]
    
        widgets = {
            "titulo":forms.TextInput(attrs={'class': 'form-control'}),
            "subtitulo":forms.TextInput(attrs={'class': 'form-control'}),
            "contenido":forms.Textarea(attrs={'class': 'form-control'}),                   
            "autor" :forms.Select(attrs={'class':'form-control'}),
            "imagen" : forms.FileInput(attrs={'class':'form-control'})            
        }



class ComentarioFormulario(forms.ModelForm):
    class Meta:
        model = models.Comentario
        fields =["comentario","autor","blog"]
    
        widgets = {           
            "comentario":forms.Textarea(attrs={'class': 'form-control'})
        }


class UserCreationFormulario(UserCreationForm):    

    class Meta:
        model = UserModel
        fields = ["first_name", "last_name","email","username","password1", "password2"]
        #help_texts = {k: "" for k in fields}
        
        widgets = {
            "first_name":forms.TextInput(attrs={'class': 'form-control'}),
            "last_name":forms.TextInput(attrs={'class': 'form-control'}),
            "email":forms.TextInput(attrs={'class': 'form-control'}),           
            "password1":forms.PasswordInput(attrs={'class': 'form-control'}), 
            "password2":forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'por favor confirme su password'}),                   
                       
        }

class UserUpdateFormulario(UserCreationForm):    

    class Meta:
        model = UserModel
        fields = ["first_name", "last_name","email","password1", "password2"]
        #help_texts = {k: "" for k in fields}
        
        widgets = {
            "first_name":forms.TextInput(attrs={'class': 'form-control'}),
            "last_name":forms.TextInput(attrs={'class': 'form-control'}),
            "email":forms.TextInput(attrs={'class': 'form-control'}),           
            "password1":forms.PasswordInput(attrs={'class': 'form-control'}), 
            "password2":forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'por favor confirme su password'}),                   
                       
        }


        
       


class UserAvatarFormulario(forms.ModelForm):

    class Meta:
        model = models.Avatar
        fields = ["imagen"]

