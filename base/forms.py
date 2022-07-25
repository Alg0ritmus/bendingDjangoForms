from django import forms
from .models import *

class SimpleForm(forms.Form):
    name = forms.CharField(label='First Name',max_length=10,required=False)
    kg = forms.IntegerField(max_value=100, required=True)

class ArticleForm(forms.Form):
    name_title =  forms.CharField(max_length=100)
    pub_date = forms.DateField(required=False)

class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class CreateSecret(forms.ModelForm):
    class Meta:
        model= Secret
        fields=  '__all__'


class ArchiveNBA(forms.ModelForm):
    name = "ArchiveNBA"
    class Meta:
        model = Archive
        fields = '__all__'


class ArticleNBA(forms.ModelForm):
    name = "ArticleNBA"
    class Meta:
        model = Article
        exclude = ['established']

class CommentNBA(forms.ModelForm):
    name = "CommentNBA"
    class Meta:
        model = Comment
        exclude = ['established']

class PinnedNBA(forms.ModelForm):
    name = "PinnedNBA"
    class Meta:
        model = Pinned
        exclude = ['established'] 


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['pdf_file']


# add widget to upload multiple files
# https://docs.djangoproject.com/en/4.0/topics/http/file-uploads/#uploading-multiple-files
# https://stackoverflow.com/questions/38257231/how-can-i-upload-multiple-files-to-a-model-field#answer-52016594

# for saving files we can create this form (with widget) so 
# we can select multiple files and upload
# to save files, we acctualy need to create new instances 
# of FIle objects and save them individualy
class uploadMultipleFilesForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['pdf_file']
        widgets = {
            'pdf_file': forms.ClearableFileInput(attrs={'multiple': True}),
        }