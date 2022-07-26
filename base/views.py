import json
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse 
from .forms import *
from .models import Person
from django.core import serializers

from django.forms import formset_factory, modelformset_factory
import datetime

# delete files and manage files in file storage
from django.core.files.storage import default_storage
from django.conf import settings
import os

# dealing with restriction to static files
from django.views.static import serve
# Create your views here.

# POST - form + add to DB
def home(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            # get data from form in cleaned form
            name = form.cleaned_data['name']
            kg = form.cleaned_data['kg']
            # add to db
            a = Person(name=name,kg=kg)
            a.save()
            form.clean()
    else:
        form = SimpleForm()
        name = "None"
    context = {
        'form':form,
        'name':name,
    }
    return render(request,'base/index.html',context)


# testing Simple Formsets
def testFormsets(request):
    ArticleFormSet = formset_factory(ArticleForm,extra=3)
    formset = ArticleFormSet()

    if request.method == 'POST':
        formset = ArticleFormSet(request.POST)
        if formset.is_valid():
            print(formset.cleaned_data)
            # here u can save to DB

            for item in formset.cleaned_data:
                # check if in is not empty
                if item:
                    name_title = item['name_title']
                    pub_date = item['pub_date']
                    print(">>>>>>",name_title,pub_date)
                
            # ArticleForm(name_title=name_title, pub_date=pub_date).save()
        else:
            print("invlaid")
    context={
        'formset':formset,
    }   

    return render(request,'base/index.html',context)


# testing serialization
def getPersons(request):
    person_list = Person.objects.all()
    person_list_JSON = serializers.serialize('json',person_list)
    return JsonResponse(person_list_JSON,safe=False)

# testing form models
def postModelInfo(request):
    if request.method == 'POST':
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()
  
    context = {
        'postModelFrom': PersonModelForm() 
    }
    return render(request,'base/ModelForm.html',context)

def updateModelInfo(request,pk):
    object = get_object_or_404(Person, id=pk)
    updateModelForm = PersonModelForm(instance = object)
    if request.method == 'POST':
        updateModelForm = PersonModelForm(request.POST, instance = object)
        if updateModelForm.is_valid():
            updateModelForm.save()
    context={
        'postModelFrom': updateModelForm,
        'pk': pk
    }
    return render(request,'base/ModelForm.html',context)

def modelFormSets(request):
    PersonFormSet = modelformset_factory(Person, fields=('name','kg',),extra=1)
    if request.method == 'POST':
        print(request.POST)
        myformset =  PersonFormSet(request.POST)
        if myformset.is_valid():
            myformset.save()
            return redirect('base:home')
        else:
            print(myformset.errors,"\n>>",myformset)

    # ak chcem nacitat iba prazdne
    # polia tak nastav Person.objects.none()
    myformset = PersonFormSet(queryset=Person.objects.none())
    context = {
        'modelFormSets' : myformset,
    }
    return render(request,'base/modelFormSets.html',context)

def DoubleOneToMany(request):
    errors="None"
    if request.method == 'POST':
        form = CreateSecret(request.POST)
        if form.is_valid():
            form.save()
        else:
            errors = form.errors
            print(">>",errors)
    context = {
        'form': CreateSecret(),
        'errors': errors
    }
    return render(request,'base/dbrel.html',context)
    
def NBAforms(request):
    allInOneForm = modelformset_factory(Archive,fields=('user',),extra=10)
    formset = allInOneForm(queryset=Archive.objects.none())
    if request.method == 'POST':
        formset = allInOneForm(request.POST)

        if formset.is_valid():
            print("<<<")
            formset.save()
        else:
            print(">>",formset.non_form_errors())    


    context = {
        'all': formset
    }
   
    
    return render(request,'base/NBA.html',context)


def FetchReq(request):
    data = ""
    if request.method == 'POST':
        serialized_data = json.loads(request.body.decode())
        for sd in serialized_data:
            data += serialized_data[sd]
        context={
        'data':data,
        }
        return JsonResponse(context,safe=False)
   
    return render(request,'base/fetch.html')

    
def uploadFile(request):
    form = UploadFileForm()
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        print(">>>>>",request.FILES)
        if form.is_valid():
            form.save()
            return redirect('base:uploadFile')
        else:
            print(form.errors)

    context = {
        'form':form,
    }
    return render(request,'base/uploadFIle.html',context)

def uploadMultipleFiles(request):
    # form_w_multi_files -> for generating forms
    form_w_multi_files = uploadMultipleFilesForm()
    if request.method == 'POST':
        # form_w_multi_files -> for validation of form
        form_w_multi_files = uploadMultipleFilesForm(request.POST,request.FILES)
        files = request.FILES.getlist('pdf_file')
        if form_w_multi_files.is_valid():
            for f in files:
                individual_file = UploadFile(pdf_file=f)
                individual_file.save()
            return redirect('base:uploadMultipleFiles')
        else:
            print(form_w_multi_files.errors)

    context = {
        'multiform':form_w_multi_files,
    }
    return render(request,'base/uploadFIle.html',context)


# if u want to delete files, make sure u delete them also from
# storage ... u need to do this manually

def deleteAllFiles(request):
    filesInDB = UploadFile.objects.all()
    
    for file in filesInDB:
        # delete  file from storage
        # https://docs.djangoproject.com/en/4.0/topics/files/#storage-objects
        # relative path to file -> print(file.pdf_file.url) | file name -> file.pdf_file
        
        # get absolute Path to file
        absolute_path = os.path.join(settings.MEDIA_ROOT,str(file.pdf_file))
        path_to_file = default_storage.path(absolute_path)
        default_storage.delete(path_to_file)
        #delete file from DB
        file.delete()
    
    return render(request,'base/uploadFIle.html')

# access files only if u are authenticated || check urls
# https://docs.djangoproject.com/en/4.0/ref/views/#django.views.static.serve
# https://github.com/django/django/blob/7bdb682215de3bf7f8f38f8161b175c225ee25fa/django/views/static.py#L17
def restrictedFiles(request,mypath):
    if request.user.is_authenticated:
        return serve(request,mypath,document_root=settings.MEDIA_ROOT)
    else:
        return redirect('base:home')
