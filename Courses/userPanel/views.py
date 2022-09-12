import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from userPanel.forms import sliderForm, foundForm,featurForm,tipsForm,subjectsForm,communityForm,guidelineForm,blogsForm,contactForm
from userPanel.models import slider, found, feature, tips, subjects, community, guideline, blogs, contact
from userPanel.setup import file_save, handle_JPEG_image_file, handle_JPG_image_file, handle_VIDEO_file,extention
from django.contrib import messages
# Create your views here.
fs = FileSystemStorage()

def Dashboard(request):
    return render(request, 'html/set_page/index.html')

def setSlider(request):
    try:
        if request.method == 'POST':
            data = sliderForm(request.POST, request.FILES)
            if data.is_valid():
                title = request.POST['sl_title']
                pragraph = request.POST['sl_pragraph']
                path = file_save(request.FILES['sl_image'], extention(request.FILES['sl_image']))
                if path != False:
                    catch = slider(sl_title=title,sl_pragraph=pragraph,sl_image=path)
                    catch.save()
                    messages.success(request,"Save Successfully")
                    return redirect("/userPanel/view_slider/")
    except:
            messages.error(request, "Invalid Input")
            return redirect("/userPanel/set_slider/")
    form = sliderForm()
    return render(request, 'html/set_page/set_slider.html',{'form':form})
def viewSlider(request):
    all = slider.objects.all()
    return render(request,'html/view_page/slider.html',{"record":all})
def updateSlider(request,id):
    item = slider.objects.get(id=id)
    file = sliderForm(instance=item)
    if request.method == "POST":
        title = request.POST['sl_title']
        pragraph = request.POST['sl_pragraph']
        item.sl_title = title
        item.sl_pragraph = pragraph
        try:
            if request.FILES['sl_image']:
                deltPath = "userPanel" + item.sl_image.name
                fs.delete(deltPath)
                path = file_save(request.FILES['sl_image'], extention(request.FILES['sl_image']))
                item.sl_image = path
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("/userPanel/view_slider/")
    return render(request,'html/update_page/up_slider.html',{"form":file,"id":id})
def delSlider(request,id):
    try:
        data = slider.objects.get(id=id)
        deltPath = "userPanel" + data.sl_image.name
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("/userPanel/view_slider/")
    except:
        try:
            data = slider.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("/userPanel/view_slider/")
        except:
            return redirect("/userPanel/view_slider/")

def setFound(request):
    try:
        if request.method == 'POST':
            data = foundForm(request.POST, request.FILES)
            if data.is_valid():
                title = request.POST['fnd_title']
                pragraph = request.POST['fnd_pragraph']
                path = file_save(request.FILES['fnd_image'], extention(request.FILES['fnd_image']))
                if path != False:
                    catch = found(fnd_title=title,fnd_pragraph=pragraph,fnd_image=path)
                    catch.save()
                    messages.success(request,"Save Successfully")
                    return redirect("/userPanel/view_found/")
    except:
        messages.error(request, "Invalid Input")
        return redirect("/userPanel/set_found/")
    form = foundForm()
    return render(request, 'html/set_page/set_found.html',{'form':form})
def viewFound(request):
    all = found.objects.all()
    return render(request,'html/view_page/found.html',{"record":all})
def updateFound(request,id):
    item = found.objects.get(id=id)
    file = foundForm(instance=item)
    if request.method == "POST":
        title = request.POST['fnd_title']
        pragraph = request.POST['fnd_pragraph']
        item.fnd_title = title
        item.fnd_pragraph = pragraph
        try:
            if request.FILES['fnd_image']:
                deltPath = "userPanel" + item.fnd_image.name
                fs.delete(deltPath)
                path = file_save(request.FILES['fnd_image'], extention(request.FILES['fnd_image']))
                item.fnd_image = path
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("/userPanel/view_found/")
    return render(request,'html/update_page/up_found.html',{"form":file,"id":id})
def delFound(request,id):
    try:
        data = found.objects.get(id=id)
        deltPath = "userPanel" + data.fnd_image.name
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("/userPanel/view_found/")
    except:
        try:
            data = found.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("/userPanel/view_found/")
        except:
            return redirect("/userPanel/view_found/")

def setFeature(request):
    try:
        if request.method == 'POST':
            data = featurForm(request.POST, request.FILES)
            if data.is_valid():
                name = request.POST['feat_name']
                title = request.POST['feat_title']
                pragraph = request.POST['feat_pragraph']
                path = file_save(request.FILES['feat_image'], extention(request.FILES['feat_image']))
                if path != False:
                    catch = feature(feat_name=name,feat_title=title,feat_pragraph=pragraph,feat_image=path)
                    catch.save()
                    messages.success(request,"Save Successfully")
                    return redirect("/userPanel/view_feature/")
    except:
        messages.error(request, "Invalid Input")
        return redirect("/userPanel/set_feature/")
    form = featurForm()
    return render(request, 'html/set_page/set_feature.html',{'form':form})
def viewFeature(request):
    all = feature.objects.all()
    return render(request,'html/view_page/feature.html',{"record":all})
def updateFeature(request,id):
    item = feature.objects.get(id=id)
    file = featurForm(instance=item)
    if request.method == "POST":
        name = request.POST['feat_name']
        title = request.POST['feat_title']
        pragraph = request.POST['feat_pragraph']
        item.feat_name = name
        item.feat_title = title
        item.feat_pragraph = pragraph
        try:
            if request.FILES['feat_image']:
                deltPath = "userPanel" + item.feat_image.name
                fs.delete(deltPath)
                path = file_save(request.FILES['feat_image'], extention(request.FILES['feat_image']))
                item.feat_image = path
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("/userPanel/view_feature/")
    return render(request,'html/update_page/up_feature.html',{"form":file,"id":id})
def delFeature(request,id):
    try:
        data = feature.objects.get(id=id)
        deltPath = "userPanel" + data.feat_image.name
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("/userPanel/view_feature/")
    except:
        try:
            data = feature.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("/userPanel/view_feature/")
        except:
            return redirect("/userPanel/view_feature/")


def setTips(request):
    try:
        if request.method == 'POST':
            data = tipsForm(request.POST, request.FILES)
            if data.is_valid():
                title = request.POST['tps_title']
                pragraph = request.POST['tps_pragraph']
                line = request.POST['tps_line']
                path = file_save(request.FILES['tps_file'], extention(request.FILES['tps_file']))
                if path != False:
                    catch = tips(tps_title=title,tps_pragraph=pragraph,tps_line=line,tps_file=path)
                    catch.save()
                    messages.success(request,"Save Successfully")
                    return redirect("/userPanel/view_tips/")
    except:
        messages.error(request, "Invalid Input Tips Form")
        return redirect("/userPanel/set_tips/")
    form = tipsForm()
    return render(request, 'html/set_page/set_tips.html',{'form':form})
def viewTips(request):
    all = tips.objects.all()
    return render(request,'html/view_page/tips.html',{"record":all})
def updateTips(request,id):
    item = tips.objects.get(id=id)
    file = tipsForm(instance=item)
    if request.method == "POST":
        title = request.POST['tps_title']
        pragraph = request.POST['tps_pragraph']
        line = request.POST['tps_line']
        item.tps_title = title
        item.tps_pragraph = pragraph
        item.tps_line = line
        try:
            if request.FILES['tps_file']:
                deltPath = "userPanel" + item.tps_file.name
                fs.delete(deltPath)
                path = file_save(request.FILES['tps_file'], extention(request.FILES['tps_file']))
                item.tps_file = path
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("/userPanel/view_tips/")
    return render(request,'html/update_page/up_tips.html',{"form":file,"id":id})
def delTips(request,id):
    try:
        data = tips.objects.get(id=id)
        deltPath = "userPanel" + data.tps_file.name
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("/userPanel/view_tips/")
    except:
        try:
            data = tips.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("/userPanel/view_tips/")
        except:
            return redirect("/userPanel/view_tips/")


def setSubject(request):
    try:
        if request.method == 'POST':
            data = subjectsForm(request.POST, request.FILES)
            if data.is_valid():
                name = request.POST['sub_name']
                fee = request.POST['sub_fee']
                duration = request.POST['sub_duration']
                details = request.POST['sub_details']
                path = file_save(request.FILES['sub_image'], extention(request.FILES['sub_image']))
                if path != False:
                    catch = subjects(sub_name=name,sub_fee=fee,sub_duration=duration,sub_details=details,sub_image=path)
                    catch.save()
                    messages.success(request,"Save Successfully")
                    return redirect("/userPanel/view_subject/")
    except:
        messages.error(request, "Invalid Input")
        return redirect("/userPanel/set_subject/")
    form = subjectsForm()
    return render(request, 'html/set_page/set_subject.html',{'form':form})
def viewSubject(request):
    all = subjects.objects.all()
    return render(request,'html/view_page/subject.html',{"record":all})
def updateSubject(request,id):
    item = subjects.objects.get(id=id)
    file = subjectsForm(instance=item)
    if request.method == "POST":
        name = request.POST['sub_name']
        fee = request.POST['sub_fee']
        duration = request.POST['sub_duration']
        details = request.POST['sub_details']
        item.sub_name = name
        item.sub_fee = fee
        item.sub_duration = duration
        item.sub_details = details
        try:
            if request.FILES['sub_image']:
                deltPath = "userPanel" + item.sub_image.name
                fs.delete(deltPath)
                path = file_save(request.FILES['sub_image'], extention(request.FILES['sub_image']))
                item.sub_image = path
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("/userPanel/view_subject/")
    return render(request,'html/update_page/up_subject.html',{"form":file,"id":id})
def delSubject(request,id):
    try:
        data = subjects.objects.get(id=id)
        deltPath = "userPanel" + data.sub_image.name
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("/userPanel/view_subject/")
    except:
        try:
            data = subjects.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("/userPanel/view_subject/")
        except:
            return redirect("/userPanel/view_subject/")

def setCommunity(request):
    try:
        if request.method == 'POST':
            data = communityForm(request.POST, request.FILES)
            if data.is_valid():
                name = request.POST['com_name']
                pragraph = request.POST['com_pragraph']
                address = request.POST['com_address']
                details = request.POST['com_details']
                path = file_save(request.FILES['com_image'], extention(request.FILES['com_image']))
                if path != False:
                    catch = community(com_name=name,com_pragraph=pragraph,com_address=address,com_details=details,com_image=path)
                    catch.save()
                    messages.success(request,"Save Successfully")
                    return redirect("/userPanel/view_community/")
    except:
        messages.error(request, "Invalid Input")
        return redirect("/userPanel/set_community/")
    form = communityForm()
    return render(request, 'html/set_page/set_community.html',{'form':form})
def viewCommunity(request):
    all = community.objects.all()
    return render(request,'html/view_page/community.html',{"record":all})
def updateCommunity(request,id):
    item = community.objects.get(id=id)
    file = communityForm(instance=item)
    if request.method == "POST":
        name = request.POST['com_name']
        pragraph = request.POST['com_pragraph']
        address = request.POST['com_address']
        details = request.POST['com_details']
        item.com_name = name
        item.com_pragraph = pragraph
        item.com_address = address
        item.com_details = details
        try:
            if request.FILES['com_image']:
                deltPath = "userPanel" + item.com_image.name
                fs.delete(deltPath)
                path = file_save(request.FILES['com_image'], extention(request.FILES['com_image']))
                item.com_image = path
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("/userPanel/view_community/")
    return render(request,'html/update_page/up_community.html',{"form":file,"id":id})
def delCommunity(request,id):
    try:
        data = community.objects.get(id=id)
        deltPath = "userPanel" + data.com_image.name
        fs = FileSystemStorage()
        fs.delete(deltPath)
        messages.success(request, "Delete Successfully")
        return redirect("/userPanel/view_community/")
    except:
        try:
            data = community.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("/userPanel/view_community/")
        except:
            return redirect("/userPanel/view_community/")


def setGuideline(request):
    try:
        if request.method == 'POST':
            data = guidelineForm(request.POST, request.FILES)
            if data.is_valid():
                title = request.POST['guid_title']
                pragraph = request.POST['guid_pragraph']
                is_file = file_save(request.FILES['guid_file'], extention(request.FILES['guid_file']))
                if is_file != False:
                    catch = guideline(guid_title=title,guid_pragraph=pragraph,guid_file=is_file)
                    catch.save()
                    messages.success(request,"Save Successfully")
                    return redirect("/userPanel/view_guideline/")
    except:
        messages.error(request, "Invalid Input")
        return redirect("/userPanel/set_guideline/")
    form = guidelineForm()
    return render(request, 'html/set_page/set_guideline.html',{'form':form})
def viewGuideline(request):
    all = guideline.objects.all()
    return render(request,'html/view_page/guideline.html',{"record":all})
def updateGuideline(request,id):
    item = guideline.objects.get(id=id)
    file = guidelineForm(instance=item)
    if request.method == "POST":
        title = request.POST['guid_title']
        pragraph = request.POST['guid_pragraph']
        item.guid_title = title
        item.guid_pragraph = pragraph
        try:
            if request.FILES['guid_file']:
                fs.delete("userPanel" + item.guid_file.name)
                item.guid_file = file_save(request.FILES['guid_file'], extention(request.FILES['guid_file']))
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("/userPanel/view_guideline/")
    return render(request,'html/update_page/up_guideline.html',{"form":file,"id":id})
def delGuideline(request,id):
    try:
        data = guideline.objects.get(id=id)
        deltPath = "userPanel" + data.guid_file.name
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("/userPanel/view_guideline/")
    except:
        try:
            data = guideline.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("/userPanel/view_guideline/")
        except:
            return redirect("/userPanel/view_guideline/")


def setBlog(request):
    try:
        if request.method == 'POST':
            data = blogsForm(request.POST, request.FILES)
            if data.is_valid():
                name = request.POST['blog_name']
                title = request.POST['blog_title']
                comment = request.POST['blog_comment']
                details = request.POST['blog_details']
                path = file_save(request.FILES['blog_image'], extention(request.FILES['blog_image']))
                if path != False:
                    catch = blogs(blog_name=name,blog_title=title,blog_comment=comment,blog_details=details,blog_image=path)
                    catch.save()
                    messages.success(request,"Save Successfully")
                    return redirect("/userPanel/view_blog/")
    except:
        messages.error(request, "Invalid Input")
        return redirect("/userPanel/set_blog/")
    form = blogsForm()
    return render(request, 'html/set_page/set_blog.html',{'form':form})
def viewBlog(request):
    all = blogs.objects.all()
    return render(request,'html/view_page/blog.html',{"record":all})
def updateBlog(request,id):
    item = blogs.objects.get(id=id)
    file = blogsForm(instance=item)
    if request.method == "POST":
        name = request.POST['blog_name']
        title = request.POST['blog_title']
        comment = request.POST['blog_comment']
        details = request.POST['blog_details']
        item.blog_name = name
        item.blog_title = title
        item.blog_comment = comment
        item.blog_details = details
        try:
            if request.FILES['blog_image']:
                fs.delete("userPanel" + item.blog_image.name)
                item.blog_image = file_save(request.FILES['blog_image'], extention(request.FILES['blog_image']))
        except:
            pass
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("/userPanel/view_blog/")
    return render(request,'html/update_page/up_blog.html',{"form":file,"id":id})
def delBlog(request,id):
    try:
        data = blogs.objects.get(id=id)
        deltPath = "userPanel" + data.blog_image.name
        fs.delete(deltPath)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("/userPanel/view_blog/")
    except:
        try:
            data = blogs.objects.get(id=id)
            data.delete()
            messages.success(request, "Only Text Delete")
            return redirect("/userPanel/view_blog/")
        except:
            return redirect("/userPanel/view_blog/")


def setContact(request):
    try:
        if request.method == 'POST':
            data = contactForm(request.POST)
            if data.is_valid():
                name = request.POST['cont_person_name']
                email = request.POST['cont_person_email']
                subject = request.POST['cont_person_subject']
                message = request.POST['cont_person_message']
                catch = contact(cont_person_name=name,cont_person_email=email,cont_person_subject=subject,cont_person_message=message)
                catch.save()
                messages.success(request,"Save Successfully")
                return redirect("/userPanel/view_contact/")
    except:
        messages.error(request, "Invalid Input")
        return redirect("/userPanel/set_contact/")
    form = contactForm()
    return render(request, 'html/set_page/set_contact.html',{'form':form})
def viewContact(request):
    all = contact.objects.all()
    return render(request,'html/view_page/contact.html',{"record":all})
def updateContact(request,id):
    item = contact.objects.get(id=id)
    file = contactForm(instance=item)
    if request.method == "POST":
        name = request.POST['cont_person_name']
        email = request.POST['cont_person_email']
        subject = request.POST['cont_person_subject']
        message = request.POST['cont_person_message']
        item.cont_person_name = name
        item.cont_person_email = email
        item.cont_person_subject = subject
        item.cont_person_message = message
        item.save()
        messages.success(request, "Update Successfully")
        return redirect("/userPanel/view_contact/")
    return render(request,'html/update_page/up_contact.html',{"form":file,"id":id})
def delContact(request,id):
        data = contact.objects.get(id=id)
        data.delete()
        messages.success(request, "Delete Successfully")
        return redirect("/userPanel/view_blog/")
