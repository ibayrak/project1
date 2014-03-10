# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.core.management import call_command
import csv
from project1.uploadcsv.models import Document
from project1.uploadcsv.forms import DocumentForm
from project1.uploadcsv.models import Member
def home(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return render_to_response('uploadcsv/showmember.html',
                {'members': get_members(newdoc)}, context_instance=RequestContext(request)
            )
            
    else:
        form = DocumentForm() # A empty, unbound form

    # Render list page with the documents and the form
    return render_to_response(
        'uploadcsv/home.html',
        {'form': form},
        context_instance=RequestContext(request)
    )

def get_members(newdoc):
    members=[]
    with open('project1/media/csv_uploads/sportslab_members.csv') as f:
      reader = csv.reader(f, delimiter=',')
      count=0
      for row in reader:
        if count!=0 :
            member= Member()
            member.name=row[0]
            member.surname=row[1]        
            member.email=row[2]
            member.phone=row[3]
            members.append(member)        
        count=+1
    return members
