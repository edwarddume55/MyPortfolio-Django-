from django.shortcuts import render
from .models import Project,Skill,Tag
# Create your views here.
def homePage(request):
    projects = Project.objects.all()
    detailedskills = Skill.objects.exclude(body ='')
    skills = Skill.objects.filter(body='')
    context={'projects':projects, 'skills':skills, 'detailedskills':detailedskills}
    return render(request, 'base/home.html',context )