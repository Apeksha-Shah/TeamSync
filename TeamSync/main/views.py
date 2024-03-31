from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import login,logout,authenticate
from .models import ProjectList
from django.contrib.auth.decorators import login_required

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
        p_name = request.POST['p_name']
        p_code = request.POST['p_code']
        status = request.POST.get('status','0')     # by default status = 0 

        status = True if status=='1' else False
    
        p1 = ProjectList(
            fkey = request.user,
            project_name = p_name,
            project_code = p_code,
            status = status,
        )
        p1.save()
        return redirect('main:project')
    all_projects = ProjectList.objects.filter(fkey=request.user.id)
    return render(request,'Project/project.html',{'all_projects':all_projects})
   
@login_required(login_url='/login')
def project_detail(request, project_code):
    project = get_object_or_404(ProjectList, project_code=project_code, fkey=request.user)
    # Assuming your ProjectList model has html_code, css_code, and js_code fields
    context = {
        'html_code': project.html_code,
        'css_code': project.css_code,
        'js_code': project.js_code,
        'project_code': project_code,
    }
    return render(request, 'editor.html', context)  # Adjust 'editor.html' as needed