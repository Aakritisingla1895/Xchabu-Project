from django import forms
from userauth.models import CreateProject,User

class CreateForm(forms.ModelForm):
    class Meta:
        model = CreateProject  
        fields = "__all__"  