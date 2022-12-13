from django.forms import ModelForm
from django import forms
from .models import Executive,Committee,Committee_Member,Union,Zone, Fellowship,Patron,Chaplain,Alumni_rep, Position,Program,Zone_Name
# USER AUTHENTICATION
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from import_export import resources


class ExecutiveForm(ModelForm):
    class Meta:
        model = Executive
        fields ='__all__'
      
       
    def __init__(self, *args, **kwargs):
        super(ExecutiveForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class CommitteeForm(ModelForm):
    class Meta:
        model = Committee    
        fields ='__all__'
     
       
    def __init__(self, *args, **kwargs):
        super(CommitteeForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class MembersForm(ModelForm):
    class Meta:
        model = Committee_Member
        fields ='__all__'
     
       
    def __init__(self, *args, **kwargs):
        super(MembersForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class UnionsForm(ModelForm):
    class Meta:
        model = Union
        fields ='__all__'
       
    def __init__(self, *args, **kwargs):
        super(UnionsForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})



class ZoneForm(ModelForm):
    class Meta:
        model = Zone
        fields ='__all__'
       
    def __init__(self, *args, **kwargs):
        super(ZoneForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class FellowshipForm(ModelForm):
    class Meta:
        model = Fellowship
        fields ='__all__'
       
    def __init__(self, *args, **kwargs):
        super(FellowshipForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class PatronForm(ModelForm):
    class Meta:
        model = Patron
        fields ='__all__'
       
    def __init__(self, *args, **kwargs):
        super(PatronForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class ChaplainForm(ModelForm):
    class Meta:
        model = Chaplain
        fields ='__all__'
       
    def __init__(self, *args, **kwargs):
        super(ChaplainForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class AlumniRepForm(ModelForm):
    class Meta:
        model = Alumni_rep
        fields ='__all__'
       
    def __init__(self, *args, **kwargs):
        super(AlumniRepForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})
    
class PositionsForm(ModelForm):
    class Meta:
        model = Position
        fields ='__all__'
       
    def __init__(self, *args, **kwargs):
        super(PositionsForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class ZoneNameForm(ModelForm):
    class Meta:
        model = Zone_Name
        fields ='__all__'
       
    def __init__(self, *args, **kwargs):
        super(ZoneNameForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields ='__all__'
       
    def __init__(self, *args, **kwargs):
        super(ProgramForm, self).__init__(*args, **kwargs)
        # or this super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})

# USER AUTHENTICATION AND CREATION FORMAT
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields =['first_name','email','username','password1','password2']
        label = {
           'first_name':'Name',
        }  

    def __init__(self,*args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})  
class ExecutiveResource(resources.ModelResource):
     class Meta:
            model = Executive
    


