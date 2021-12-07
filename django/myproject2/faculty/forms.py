from django.forms import ModelForm

from faculty.models import  *

class ContactForm(ModelForm):
    class Meta:
        model=Contact
        #fields=[' ',' ',' ']
        fields='__all__'

    
class FacultyRegistration(ModelForm):
    class Meta:
        model=Registration
        fields='__all__'
        

class imgloadForm(ModelForm):
    class Meta:
        model=ImgLoad
        fields='__all__'

class Emp(ModelForm):
    class Meta:
        model=Employee
        fields =['salary']
