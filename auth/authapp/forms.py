from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label=('Username'), widget=forms.TextInput(attrs={'placeholder': ('Username')}),         
                                required=True, error_messages={'required': ('Please enter your Username')})      
    password = forms.CharField(label=('Password'), 
                                widget=forms.PasswordInput(attrs={'placeholder': ('Password')}),                                
                                required=True, error_messages={'required': ('Please enter your password')})
