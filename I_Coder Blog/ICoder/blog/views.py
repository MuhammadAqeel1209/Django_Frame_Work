from django.shortcuts import render,redirect
from .models import Post ,BlogComment
from django.contrib import messages


# Create your views here.
def blogHome(request): 
    posts = Post.objects.all()
    return render(request,"blog/bloghome.html" ,{'posts': posts})

def blogPost(request,slug): 
        postSlug = Post.objects.filter(slug = slug).first()
        comments = BlogComment.objects.filter(post = postSlug,parent = None)
        replies = BlogComment.objects.filter(post = postSlug).exclude(parent = None)
        replyDict = {}
        for reply in replies:
            if reply.parent.sno not in replyDict.keys():
                replyDict[reply.parent.sno] = [reply]
            else:
                replyDict[reply.parent.sno].append(reply)
        
        return render(request,"blog/blogpost.html",{'postslug':postSlug,'comments':comments,'user': request.user,'replyDict': replyDict})

def postComment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno = postSno)
        parentSno = request.POST.get('parentSno')
        
        print(comment,user,post,parentSno,postSno)

        if parentSno == "": 
            comment = BlogComment(comment = comment, user = user, post = post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent = BlogComment.objects.get(sno = parentSno)
            parentComment = BlogComment(comment = comment, user = user, post = post, parent = parent)
            parentComment.save()
            messages.success(request, "Your reply has been posted successfully")


    return redirect(f"blogpost/{post.slug}")