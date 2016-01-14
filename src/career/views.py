from django.shortcuts import render
from .models import Project
# Create your views here.
def project(request, project_name_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    context_dict = {}

    try:

        project = Project.objects.get(slug=project_name_slug)

        context_dict['project'] = project
        context_dict['features'] =  project.features.split('\n')
        context_dict['tools'] =  project.tools.split('\n')
    except Project.DoesNotExist:

        pass

    return render(request, 'single-post.html', context_dict)
def career(request):

    project =  Project.objects.all()
    context_dict = {'projects':project}


    return render(request ,'service.html',context_dict)