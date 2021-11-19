from django import forms
from django.contrib.auth.models import User

class signupform(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']

class feedbackform(forms.Form):
    firstname=forms.CharField(label='First Name')
    lastname=forms.CharField(label='Last Name')
    email=forms.EmailField()
    country=forms.CharField()
    subject=forms.CharField(widget=forms.Textarea)
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput)

    def clean(self):
        print("bot validation")
        cleaned_data=super().clean()
        bot_handler_value=cleaned_data['bot_handler']
        if len(bot_handler_value)>0:
            raise forms.ValidationError('thanks bot..could not submit your data')