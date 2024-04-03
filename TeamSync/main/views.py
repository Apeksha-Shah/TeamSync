from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth import login,logout,authenticate
from .models import ProjectList
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,'main/home.html')


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request,'registration/sign_up.html',{'form': form})


def about(request):
    return render(request,'About/about.html')

@login_required(login_url='/login')
def contact(request):
    return render(request,'Contact/contact.html')

@login_required(login_url='/login')
def project(request):
    if request.method == "POST":
        if 'p_name' in request.POST and 'p_code' in request.POST:
            p_name = request.POST['p_name']
            p_code = request.POST['p_code']
            status = request.POST.get('status', '1')  

            status = True if status == '1' else False

            ProjectList.objects.create(
                fkey=request.user,
                project_name=p_name,
                project_code=p_code,
                status=status,
            )
        # Check if this is a project joining request
        elif 'join_project_code' in request.POST:
            join_project_code = request.POST['join_project_code']
            project_to_join = ProjectList.objects.filter(project_code=join_project_code).first()
            if project_to_join:
                project_to_join.contributors.add(request.user)

        return redirect('main:project')
    all_projects = ProjectList.objects.filter(
        Q(fkey=request.user.id) | Q(contributors=request.user)
    ).distinct()

    return render(request, 'Project/project.html', {'all_projects': all_projects})

@login_required(login_url='/login')
def project_detail(request, project_code):
    project = ProjectList.objects.filter(
        project_code=project_code
    ).filter(
        Q(fkey=request.user) | Q(contributors=request.user)
    ).distinct().first()

    if not project:
        messages.error(request, "Project does not exist or you do not have permission to view it.")
        return redirect('main:project') 

    context = {
        'html_code': project.html_code,
        'css_code': project.css_code,
        'js_code': project.js_code,
        'project_code': project_code,
    }
    return render(request, 'editor.html', context)

