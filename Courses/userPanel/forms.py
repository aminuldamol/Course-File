from django import forms
from userPanel.models import slider,found,feature,tips,subjects,community,guideline,blogs,comments,reply,contact

class sliderForm(forms.ModelForm):
    class Meta:
        model = slider
        fields = "__all__"
        labels = {'sl_title': 'Slider Title','sl_pragraph': 'Slider Pragraph','sl_image': 'Slider Image',}

class foundForm(forms.ModelForm):
    class Meta:
        model = found
        fields = "__all__"
        labels = {'fnd_title':'Title','fnd_pragraph':'Pragraph','fnd_image':'Image',}

class featurForm(forms.ModelForm):
    class Meta:
        model = feature
        fields = "__all__"
        labels = {'feat_name':'Feature Name','feat_title':'Feature Title','feat_pragraph':'Feature Pragraph','feat_image':'Feature Image'}

class tipsForm(forms.ModelForm):
    class Meta:
        model =  tips
        fields = "__all__"
        labels = {'tps_title': 'Tips Title', 'tps_pragraph': 'Tips Pragraph', 'tps_line': 'Tips Line','tps_file':'Tips Image' }

class subjectsForm(forms.ModelForm):
    class Meta:
        model = subjects
        fields = "__all__"
        labels = {'sub_name':'Subject Name','sub_fee':'Subject Fee','sub_duration':'Subject Duration','sub_details':'Subject Details','sub_image':'Subject Image',}

class communityForm(forms.ModelForm):
    class Meta:
        model = community
        fields = "__all__"
        labels = {'com_name': 'Community Name', 'com_pragraph': 'Community Pragraph', 'com_address': 'Community Address','com_details': 'Community Details','com_image': 'Community Image'}

class guidelineForm(forms.ModelForm):
    class Meta:
        model =  guideline
        fields = "__all__"
        labels = {'guid_title': 'Guideline Title', 'guid_pragraph': 'Guideline Pragraph','guid_file': 'Guideline File'}

class blogsForm(forms.ModelForm):
    class Meta:
        model =  blogs
        fields = "__all__"
        labels = {'blog_name': 'Blog Name', 'blog_title': 'Blog Title', 'blog_comment': 'Blog Comment','blog_details': 'Blog Details','blog_image': 'Blog Image'}

class commentsForms(forms.ModelForm):
    class Meta:
        model =  comments
        fields = "__all__"

class replyForm(forms.ModelForm):
    class Meta:
        model =  reply
        fields = "__all__"

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = "__all__"
        labels = {'cont_person_name': 'Person Name', 'cont_person_email': 'Person Email', 'cont_person_subject': 'Person Subject','cont_person_message': 'Person Message'}
















