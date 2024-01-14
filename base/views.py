from django.shortcuts import redirect, render
from .models import Project,Skill,Tag
from .forms import ProjectForm
# Create your views here.
def homePage(request):
    projects = Project.objects.all()
    detailedskills = Skill.objects.exclude(body ='')
    skills = Skill.objects.filter(body='')
    context={'projects':projects, 'skills':skills, 'detailedskills':detailedskills}
    return render(request, 'base/home.html',context )

def projectPage(request,pk):
    project=Project.objects.get(id=pk)
    context={'project':project}
    return render(request, 'base/project.html', context)

def addProject(request):
    form=ProjectForm()

    if request.method == 'POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request, 'base/project_form.html',context)

def editProject(request,pk):
    project=Project.objects.get(id=pk)
    form=ProjectForm(instance=project)

    if request.method == 'POST':
        form=ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request, 'base/project_form.html',context)