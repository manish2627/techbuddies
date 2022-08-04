from turtle import title
from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from blog.models import Post
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout

# Create your views here.
def home(request):
    allpost = Post.objects.all()
    contaxt = {'allpost': allpost}
    return render(request, 'home/home.html' , contaxt) 
def about(request):
    return render(request, 'home/about.html') 
def contact(request):
    # messages.add_message(request, messages.INFO, 'Hello world.')
   
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content= request.POST['content']
        if len(name)<2 or len(email)<5 or len(phone) <10 or len(content) <5:
             messages.error(request, 'Please enter the correct details !!!')
             messages.error(request, 'Please enter the correct details !!!')
        else:
            contact = Contact(name=name, email=email, phone= phone, content= content)
            contact.save()
            messages.success(request, 'your massage has been sent succesfully  !!!')
        
    return render(request, 'home/contact.html') 

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    context={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', context)

def userhandler(request):
    if request.method == 'POST':
        # post the user details 
        username = request.POST['username']
        fname = request.POST['fname']
        lname= request.POST['lname']
        signupemail = request.POST['signupemail']
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

        user = User.objects.create_user(username, signupemail, pass1)
        user.first_name = fname
        user.last_name = lname
        user.save()
        messages.success(request, 'your account successfully ceated  !!!')
        

        return redirect('home')

    else:
        return HttpResponse(" 404 Page not found " )

def handlelogin(request):
    if request.method == 'POST':
        # post the user details 
        username = request.POST['username']
        password= request.POST['pass']
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        messages.success(request, " you are log in succesfully!!!")
        return redirect('home')

    else:
        # Return an 'invalid login' error message.
        messages.error(request, " your input credential are wrong . please try again!!!")
        return redirect('home')



def handlelogout(request):
    logout(request)
    messages.success(request, " you are log out succesfully!!!")
    return redirect('home')
        
    