from django.db import models
from django.contrib.auth.models import User

def userRegister(request):   
	curtime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime());  #temps de s'inscrire
    if request.user.is_authenticated():
	return HttpResponseRedirect("/user") # /user est le lien apres login 
    try:  
        if request.method=='POST':  
            username=request.POST.get('username','')  
            password1=request.POST.get('password1','')  
            password2=request.POST.get('password2','')  
            email=request.POST.get('email','')  
            nom=request.POST.get('nom','')
            prenom=request.POST.get('prenom','')
            annee=request.POST.get('annee','')
            departement=request.POST.get('departement','')
            style=request.POST.get('style','')
            certificat=request.POST.get('certificat','')
            photo=request.POST.get('photo','')
            errors=[]  
   
            registerForm=RegisterForm({'username':username,'password1':password1,'password2':password2,'email':email}) 
            if not registerForm.is_valid():  
                errors.extend(registerForm.errors.values())  
                return render_to_response("blog/userregister.html",RequestContext(request,{'curtime':curtime,'username':username,'email':email,'errors':errors}))  
            if password1!=password2:  
                errors.append("Passwords are different")  
                return render_to_response("blog/userregister.html",RequestContext(request,{'curtime':curtime,'username':username,'email':email,'errors':errors}))  
                      
            filterResult=User.objects.filter(username=username) 
            if len(filterResult)>0:  
                errors.append("User exist")  
                return render_to_response("blog/userregister.html",RequestContext(request,{'curtime':curtime,'username':username,'email':email,'errors':errors}))  
                  
            user=User() 
            user.username=username  
            user.set_password(password1)  
            user.email=email  
            user.save()  
            
            utilisateurs=utilisateurs() 
            utilisateurs.user_id=user.id  
            utilisateurs.nom=nom
            utilisateurs.prenom=prenom  
            utilisateurs.annee=annee  
            utilisateurs.departement=departement 
            utilisateurs.style=style  
            utilisateurs.certificat=certificat  
            utilisateurs.photo=photo    
            utilisateurs.save()  

            newUser=auth.authenticate(username=username,password=password1) 
            if newUser is not None:  
                auth.login(request, newUser) 
                return HttpResponseRedirect("/user")  # /user est le lien apres login
    except Exception,e:  
        errors.append(str(e))  
        return render_to_response("blog/userregister.html",RequestContext(request,{'curtime':curtime,'username':username,'email':email,'errors':errors}))  
          
    return render_to_response("blog/userregister.html",RequestContext(request,{'curtime':curtime}))  
