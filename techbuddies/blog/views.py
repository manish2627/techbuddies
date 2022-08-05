from asyncio.windows_events import NULL
from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, Blogcomment
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def blogHome(request):
    allpost = Post.objects.all()
    # comments = Post.objects.filter()
    contaxt = {'allpost': allpost}
    return render(request, 'blog/bloghome.html' , contaxt)

def blogPost(request, slug):
    
    post = Post.objects.filter(slug = slug).first()
    comments= Blogcomment.objects.filter(post=post, parent=None)
    replies= Blogcomment.objects.filter(post=post).exclude(parent = None)
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context={'post':post, 'comments': comments, 'replyDict':replyDict, 'user': request.user}
    
    return render(request, 'blog/blogpost.html', context)



def comment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postsno =request.POST.get('postsno')
        post= Post.objects.get(postid=postsno)
        parentsno= request.POST.get('replypostsno')
        print(parentsno)
        if parentsno=="":
            comment=Blogcomment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= Blogcomment.objects.get(sno=parentsno)
            comment=Blogcomment(comment=comment, user=user, post=post , parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")


       
       
    return redirect (f"/blog/blogpost{post.slug}")

        