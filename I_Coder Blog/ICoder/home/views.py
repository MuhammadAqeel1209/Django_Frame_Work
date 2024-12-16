from django.shortcuts import render,HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request): 
    posts = Post.objects.all()
    
    return render(request,"home/index.html",{'posts': posts})

def contact(request):
        if request.method == "POST":
                name = request.POST['name']
                email = request.POST['email']
                phone = request.POST['phone']
                content = request.POST['content']

                if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
                        messages.error(request, "Please fill the form correctly")
                else:
                        contact = Contact(name=name, email=email, phone=phone, content=content)
                        contact.save()
                        messages.success(request, "Your message has been successfully sent")
        return render(request,"home/contact.html")

def about(request): 
        return render(request,"home/about.html")

def Search(request):
    query = request.GET['search']
    poststitle = Post.objects.filter(title__icontains=query)
    allPostsAuthor = Post.objects.filter(author__icontains=query)
    allPostsContent =Post.objects.filter(content__icontains=query)
    posts =  poststitle.union(allPostsContent, allPostsAuthor)
    params = {'posts': posts,'query': query}
    return render(request, 'home/search.html', params)

def HandleSingnUp(request):
       if request.method == "POST":      
                username = request.POST['username']
                email = request.POST['email']
                fname = request.POST['fname']
                lname = request.POST['lname']
                pass1 = request.POST['pass1']
                pass2 = request.POST['pass2']

                if len(username)<10:
                        messages.error(request, " Your user name must be under 10 characters")
                        return redirect('home')

                if not username.isalnum():
                        messages.error(request, " User name should only contain letters and numbers")
                        return redirect('home')
                if (pass1!= pass2):
                        messages.error(request, " Passwords do not match")
                        return redirect('home')

                myUser = User.objects.create_user(username,email,pass1)
                myUser.first_name = fname
                myUser.last_name = lname
                myUser.save()
                messages.success(request,"Your ICoder account has been created successfuly")  
                return redirect('home')       

       else:
              return HttpResponse("404 - Not Found Not Allowed")

def handeLogin(request):
        if request.method == "POST":      
                loginusername = request.POST['loginusername']
                loginpassword = request.POST['loginpass']

                user = authenticate(username = loginusername, password = loginpassword)
                print(user)
                if user is not None:
                       login(request,user)
                       messages.success(request,"Successfulyy Logged In")
                       return redirect('home')
                else:
                       messages.error(request,"Invalid UserName or Password, Plz try again")
                       return redirect('home')

def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
