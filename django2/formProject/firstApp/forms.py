from django import forms
#from django.core import validators

# class EmployeeForm(forms.Form):
#     ename = forms.CharField(validators=[validators.MaxLengthValidator(10),validators.MinLengthValidator(3)])
#     eaddr = forms.CharField()
#     eno = forms.IntegerField()
#     esal = forms.FloatField()
    
    # def clean_ename(self):
    #     inputname = self.cleaned_data['ename'] 
        
    #     if len(inputname) < 5: 
    #         raise forms.ValidationError("The minimum length of the employee name should be 5 or more.")
            
    #     return inputname
    # def clean_eaddr(self):
    #     inputaddr = self.cleaned_data['eaddr'] 
        
    #     if inputaddr !="Kathmandu": 
    #         raise forms.ValidationError("The Address Should be Kathmandu")
            
    #     return inputaddr
    
# def starts_with_v(value):
#   if value[0].lower()!='v':
#     raise forms.ValidationError("Name should satrt with v.")
# class EmployeeForm(forms.Form):
#     ename = forms.CharField(validators=[starts_with_v])
#     eaddr = forms.CharField()
#     eno = forms.IntegerField()
#     esal = forms.FloatField()
    
# class EmployeeForm(forms.Form):
#     ename = forms.CharField()
#     eaddr = forms.CharField()
#     eno = forms.IntegerField()
#     esal = forms.FloatField()
    
#     def clean(self):
#       total_clean_data=super().clean()
#       inputname=total_clean_data['ename']
#       if inputname[0].lower !='v':
#         raise forms.ValidationError("Name should start with v.")
#       inputaddr= total_clean_data['eaddr']
#       if inputaddr !='kathmandu':
#         raise forms.ValidationError("Address should be Kathmandu.")

# class EmployeeForm(forms.Form):
#     ename = forms.CharField(label="Employee Name : ")
#     eaddr = forms.CharField(label="Employee Address : ")
#     eno = forms.IntegerField(label="Employee Number : ")
#     esal = forms.FloatField(label="Employee Salary : ")
#     epass=forms.CharField(widget=forms.PasswordInput())
#     repass=forms.CharField(label="Re-Enter your password",widget=forms.PasswordInput())
    
#     def clean(self):
#       total_clean_data=super().clean()
#       fpass=total_clean_data["epass"]
#       spass=total_clean_data["repass"]
#       if fpass!=spass:
#         raise forms.ValidationError("Both password should be same.")
 
from firstApp.models import Employee
class EmployeeForm(forms.ModelForm):
  #code for validators
  class Meta:
    model = Employee
    fields ="__all__"
    widgets={'ename':forms.TextInput(attrs={'class':'form-control','placeholder':"Input Your Name Here"})}
  
      
    
    