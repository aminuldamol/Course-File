from django.shortcuts import render
from userPanel.models import guideline, feature, subjects, community, found, blogs


# Create your views here.

def homePage(request):
    guide = guideline.objects.raw("select * from userpanel_guideline order by date_time limit 0,3 ")
    featr = feature.objects.raw("select * from userpanel_feature limit 0,3 ")
    subject = subjects.objects.raw("select * from userpanel_subjects limit 0,8 ")
    commu = community.objects.raw("select * from userpanel_community")
    fnd = found.objects.raw("select * from userpanel_found limit 1 ")
    context = {
        'guidelines':guide,
        'features':featr,
        'subjects':subject,
        'community':commu,
        'found':fnd,
    }
    return render(request,'view_file/index.html',context)

def aboutPage(request):
    guide = guideline.objects.raw("select * from userpanel_guideline order by date_time limit 0,3 ")
    featr = feature.objects.raw("select * from userpanel_feature limit 0,3 ")
    subject = subjects.objects.raw("select * from userpanel_subjects limit 0,8 ")
    commu = community.objects.raw("select * from userpanel_community")
    fnd = found.objects.raw("select * from userpanel_found limit 1 ")
    context = {
        'guidelines': guide,
        'features': featr,
        'subjects': subject,
        'community': commu,
        'found': fnd,
    }
    return render(request,'view_file/about.html',context)

def blogPage(request):
    all_blog = blogs.objects.all()
    context = {
        'blogs':all_blog
    }
    return render(request,'view_file/blog.html',context)

def blogDetailsPage(request,id):

    blog = blogs.objects.get(id=id)
    context = {
        'blog': blog
    }
    return render(request,'view_file/blog_details.html',context)

def contactPage(request):
    return render(request,'view_file/contact.html')

def coursePage(request):
    guide = guideline.objects.raw("select * from userpanel_guideline order by date_time limit 0,3 ")
    featr = feature.objects.raw("select * from userpanel_feature")
    subject = subjects.objects.raw("select * from userpanel_subjects")

    context = {
        'guidelines': guide,
        'features': featr,
        'subjects': subject,
    }
    return render(request,'view_file/course.html',context)

def course_detailsPage(request):
    return render(request, 'view_file/course_details.html')

def profilePage(request):
    return render(request,'view_file/profile.html')

def loginPage(request):
    return render(request,'view_file/login.html')

def registerPage(request):
    return render(request,'view_file/register.html')
