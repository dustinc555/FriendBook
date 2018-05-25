from django import forms
from friend.models import *

from django.contrib.auth.models import User

#not much here for now
# but i plan to expand on the comment form maybe
class CommentForm(forms.Form):
    comment = forms.CharField(max_length=300, label='')
    
    def clean(self):
        user_comment = self.cleaned_data['comment']

        if len(user_comment) > 300:
            raise forms.ValidationError('Cannot exceed 300 characters!!!')

class TopicCommentForm(forms.Form):
    comment = forms.CharField(max_length=500, label='')
    
    def clean(self):
        user_comment = self.cleaned_data['comment']

        if len(user_comment) > 500:
            raise forms.ValidationError('Cannot exceed 500 characters!!!')

class UserForm(forms.Form):

    username = forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput, label='Enter a password.', required=True)
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput, label='Enter your password again.', required=True)

    first_name = forms.CharField(max_length=20, required=False)
    last_name = forms.CharField(max_length=20, required=False)
    email= forms.EmailField(max_length=40, required=False)

    def clean(self):

        # make sure the passwords match
        pw1 = self.cleaned_data['password1']
        pw2 = self.cleaned_data['password2']

        if pw1 != pw2:
            raise forms.ValidationError('Passwords do not match')
        else:
            del self.cleaned_data['password1']
            del self.cleaned_data['password2']

            self.cleaned_data['password'] = pw1

        # check to see if the username exists
        users = User.objects.all()

        username = self.cleaned_data['username']
        for user in users:
            if username == user.username:
                raise forms.ValidationError('Sorry, that username is taken.')
        
class TopicForm(forms.Form):
    topic = forms.CharField(max_length=50)


    def clean(self):
        # bad word filter, should all be lowercase
        badWords = ['']
        userEntered = self.cleaned_data['topic'].lower()
        
        for word in badWords:
            if userEntered == word:
                raise forms.ValidationError('Thats a bad word you sicko...')
    

   
class FriendPictureForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['profile_image']


            
