from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse,FileResponse,JsonResponse,Http404
from django.db.models import Avg, Count, Min, Sum
from django.conf import settings
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import os,random,json,requests
from .forms import User1form
from .models import User1
from docxtpl import DocxTemplate
from docxtpl import InlineImage
import platform
from docx.shared import Mm
from pathlib import Path
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.utils.html import escape
if platform.system() == "Windows":
	from docx2pdf import convert
####################################################################
def index(request):
	if not request.user.is_authenticated:
		return render (request,'login.html' )
	try:		
		return render(request, 'ou.html')
	except:
		raise Http404("Not Found")
####################################################################
def logout_form(request):
	try:
		logout(request)
	except:
		pass
	return redirect ('/ecard')
####################################################################
def signin(request):
    try:
        if request.method == 'POST':
            #otp_chk=pyotp.TOTP('H4ZT2CIHQM5XO2VUSZPHWTBHMNQBDY3B')
            username=request.POST['username']
            password=request.POST['password']
            #if username=='admin':
            #    if otpcode!=otp_chk.now():
            #        return redirect ('/')
            user = authenticate(request, username=username, password=password)
            if user is not None :
                login(request , user)
                return redirect ('/ecard')
            else:
                return render(request, 'login.html')
    except:
        return render(request, 'login.html')
    return render(request, 'login.html')
####################################################################
def signup(request):
	if not request.user.is_authenticated:
		return render (request,'login.html' )
	try:
		if request.method == 'POST':
			form = User1form(request.POST , request.FILES )
			if form.is_valid():
				#instance=form.save(commit=False)
				#instance.pic.name="images/{}.png".format(instance.id)
				#instance.save()
				form.save()
				return render(request, 'ou.html', {'memo':'کاربر ساخته شد', 'var1' : 1 })
			else:
			    return render(request, 'ou.html', {'memo':'خطا در ساخت کاربر', 'var1': 1 })
		else:
				form = User1form()
				return render(request, 'ou.html', {'form': form ,  'dest' : 'signup' ,'idx' : 1 , 'var1' : 2  })
	except:
		pass
	return redirect("/ecard")
####################################################################
def changepass(request):
	if not request.user.is_authenticated:
		return render (request,'login.html' )
	#try:
	if request.method == 'POST':
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			#instance=form.save(commit=False)
			#instance.pic.name="images/{}.png".format(instance.id)
			#instance.save()
			form.save()
			update_session_auth_hash(request, form.user)
			return render(request, 'ou.html', {'memo':'گذرواژه شما با موفقیت تغییر یافت', 'var1' : 1 })
		else:
		    return render(request, 'ou.html', {'memo':'خطا در تغییر گذرواژه', 'var1': 1 })
	else:
			form = PasswordChangeForm(request.user)
			return render(request, 'ou.html', {'form': form ,  'dest' : 'changepass' ,'idx' : 1 , 'var1' : 2  })
	#except:
	#	pass
	return redirect("/ecard")
####################################################################
def printcard(request):
	if not request.user.is_authenticated:
		return render (request,'login.html' )
	try:
		doc = DocxTemplate("1.docx")
		user = User1.objects.all()
		pic = {}
		for u in user:
			if u.pic.name != '' :
				pic[u.id] = InlineImage(doc, image_descriptor = u.pic.path , width=Mm(30), height=Mm(40))
		context = {"user" : user  , "pic" : pic }
		doc.render(context)
		doc.save(os.path.join(settings.BASE_DIR, "aa.docx"))
		del doc
		if platform.system() == "Windows":
			os.system("docx2pdf {}".format('aa.docx'))
		if platform.system() == "Linux":
			os.system("lowriter --convert-to pdf  {}".format(os.path.join(settings.BASE_DIR, "aa.docx")))
		f = open(os.path.join(settings.BASE_DIR,"aa.pdf"), 'rb')
		pdf_contents = f.read()
		f.close()
		response = HttpResponse(pdf_contents, content_type='application/pdf')
		return response
	except:
		pass
	return redirect("/ecard")
####################################################################
def printcard2(request):
	if not request.user.is_authenticated:
		return render (request,'login.html' )
	try:
		doc = DocxTemplate("1.docx")
		user = User1.objects.all()
		if request.GET['fromprn'] == '' and request.GET['toprn'] == '' :
			user = User1.objects.all()
		if request.GET['fromprn'] != '' or request.GET['toprn'] != '' :
			user = User1.objects.filter(number=request.GET['fromprn'])
		if request.GET['fromprn'] != '' and request.GET['toprn'] != '' :
			user = User1.objects.filter(number__gte=request.GET['fromprn'],number__lte=request.GET['toprn'])
		pic = {}
		for u in user:
			if u.pic.name != '' :
				pic[u.id] = InlineImage(doc, image_descriptor = u.pic.path , width=Mm(30), height=Mm(40))
		context = {"user" : user  , "pic" : pic }
		doc.render(context)
		doc.save(os.path.join(settings.BASE_DIR, "aa.docx"))
		del doc
		if platform.system() == "Windows":
			os.system("docx2pdf {}".format('aa.docx'))
		if platform.system() == "Linux":
			os.system("lowriter --convert-to pdf  {}".format(os.path.join(settings.BASE_DIR, "aa.docx")))
		chk=request.GET["ftype"]
		if chk == "1" :
			f = open(os.path.join(settings.BASE_DIR,"aa.pdf"), 'rb')
		if chk == "2" :
			f = open(os.path.join(settings.BASE_DIR,"aa.docx"), 'rb')
		pdf_contents = f.read()
		f.close()
		if chk == "1" :
			response = HttpResponse(pdf_contents, content_type='application/pdf')
			return response
		if chk == "2" :
			response = HttpResponse(pdf_contents, content_type='application/docx')
			response['Content-Disposition'] = 'inline;filename=cardprn.docx'
			return response
		return redirect("/ecard")
	except:
		pass
	return redirect("/ecard")
####################################################################
def userlist(request):
	if not request.user.is_authenticated:
		return render (request,'login.html' )
	try:
	    if request.method == 'POST':
	        data = request.POST['idnum']
	        userlist=User1.objects.filter(name__contains = data ).order_by('number')
	        return render(request, 'ou.html', {'data': data , 'userlist' : userlist , 'var1' : 3 })
	    else:
	        data = ""
	        userlist=User1.objects.all().order_by('number')
	        return render(request, 'ou.html', {'data': data , 'userlist' : userlist , 'var1' : 3 })
	except:
		pass
	return redirect("/ecard")
####################################################################
def edituser(request):
	if not request.user.is_authenticated:
		return render (request,'login.html' )
	try:
		if request.method == 'POST':
			idx = request.POST['idnum']
			ins1=User1.objects.get(id = idx)
			form =User1form(request.POST , request.FILES ,  instance = ins1)
			if form.is_valid():
				form.save()
				return render(request, 'ou.html', {'memo': 'ویرایش انجام شد' , 'var1' : 1 })
			else:
			    return render(request, 'ou.html', {'memo': 'خطا در ویرایش کاربر', 'var1': 1 })
		else:
				idx = request.GET['id']
				ins1=User1.objects.get(id = idx)
				form =User1form(instance = ins1)
				return render(request, 'ou.html', {'form': form ,  'dest' : 'edituser' ,'idx' : idx , 'var1' : 2  })
	except:
	    return redirect("/ecard")
	return redirect("/ecard")
####################################################################
def deluser(request):
	if not request.user.is_authenticated:
		return render (request,'login.html' )
	try:
		if request.method == 'GET':
			idx = request.GET['id']
			User1.objects.get(id = idx).delete()
	except:
		pass
	return redirect("/ecard/userlist")
####################################################################
def uploadtpl(request):
	if not request.user.is_authenticated:
		return render (request,'login.html')
	try:
		if request.method == 'POST':
			f=request.FILES['file']
			f2=request.FILES['file2']
			with open("1.docx", 'wb') as destination:
				for chunk in f.chunks():
				    destination.write(chunk)
			with open("2.docx", 'wb') as destination:
				for chunk in f2.chunks():
				    destination.write(chunk)
			return render(request, 'ou.html',{'memo' : 'فایل آپلود شد!' , 'var1' : 1 })
		else:
			return render(request, 'ou.html', {'var1' : 7 })
	except:
		pass
	return render(request, 'ou.html', {'memo': 'خطا در سرور' , 'var1' : 1 })
###################################################################
def printalluser(request):
	if not request.user.is_authenticated:
		return render (request,'login.html' )
	try:
		doc = DocxTemplate("2.docx")
		user = User1.objects.all().order_by('number')
		context = {"user" : user }
		doc.render(context)
		doc.save(os.path.join(settings.BASE_DIR, "aa.docx"))
		del doc
		if platform.system() == "Windows":
			os.system("docx2pdf {}".format('aa.docx'))
		if platform.system() == "Linux":
			os.system("lowriter --convert-to pdf  {}".format(os.path.join(settings.BASE_DIR, "aa.docx")))
		#f = open(os.path.join(Path(__file__).resolve().parent.parent,"aa.pdf"), 'rb')
		f = open(os.path.join(settings.BASE_DIR,"aa.pdf"), 'rb')
		pdf_contents = f.read()
		f.close()
		response = HttpResponse(pdf_contents, content_type='application/pdf')
		return response
	except:
		pass
	return redirect("/ecard")
