from django.http import HttpResponse
from django.shortcuts import redirect, render, reverse
from post.models import Post, Comment
from user.models import PostUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



@login_required(login_url='user:login')
def home(request):
    print('print in post page')
    print('username:'+request.user.username)
    token = request.session.get('token')
    print(token)
    # print(request.user.username)
    return render(request,'home.html')

@login_required(login_url='user:login')
def create_post(request):
    return render(request,'createpost.html')


def get_posts(username):
    user = PostUser.objects.filter(username=username)
    posts = None
    if len(user) != 0:
        user=user[0]
        posts = user.posts.all()    
    return posts      


@login_required(login_url='user:login')
def view_my_post(request):
    print('post:'+request.session.get('username','None'))
    print('user:'+request.user.username)
    user = PostUser.objects.filter(username=request.user.username)
    posts = get_posts(request.user.username)
    return render(request,'viewmypost.html',{
        'posts': posts
    })

@login_required(login_url='user:login')
def view_all_post(request): 
    
    posts=Post.objects.all()

    return render(request,'viewallpost.html',{
        'posts':posts
    })

@login_required(login_url='user:login')
def submit_post(request, method = 'POST'):
    try:
        data = request.POST.dict()
        print(data)
        slug=data.get('slug')
        title=data.get('title')
        desc = data.get('description')
        post = Post(slug=slug, title=title, description=desc)
        user = PostUser.objects.get(username=request.user.username)
        print(user)
        post.user=user
        post.save()
        print('Post saved successfully')
        return redirect(reverse('post:view_my_post'))
    except Exception as ex:
        print('Exception occured!!')
        print(ex)
        return HttpResponse('Exception!!')


@login_required(login_url='user:login')
def add_comment(request):
    data = request.POST.dict()
    print('In Add comment view')
    comment = data.get('comment')
    post_id = data.get('post_id')
    user_id = data.get('user_id')
    page = data.get('page')
    print(user_id)
    # print("In add comment"+user_id)
    print(comment)
    print(post_id)
    comment = Comment.objects.create(comment=comment,post_id=post_id)


    comment.user.add(PostUser.objects.get(id=user_id))
    comment.save()
    if page == 'mypost':
        return redirect(reverse('post:view_my_post'))
    return redirect(reverse('post:view_all_post'))


@login_required(login_url='user:login')
def logout_view(request):
    logout(request)
    return redirect(reverse('user:login'))

@login_required(login_url='user:login')
def like(request, method = 'POST'):
    data = request.POST.dict()
    post_id = data.get('post_id')
    page = data.get('page')
    post = Post.objects.get(pk = post_id)
    user_id = post.user.id
    user = PostUser.objects.get(id = user_id)
    
    if not post.like.filter(id = request.user.id).exists():
        post.like.add(request.user)
    
    if post.dislike.filter(id = request.user.id).exists():
        post.dislike.remove(request.user)
    
    if page == 'allpage':
        return redirect(reverse('post:view_all_post'))
    return redirect(reverse('post:view_my_post'))

@login_required(login_url='user:login')
def dislike(request, method = 'POST'):
    data = request.POST.dict()
    post_id = data.get('post_id')
    page = data.get('page')
    post = Post.objects.get(id = post_id)
    user_id = post.user.id
    user = PostUser.objects.get(id = user_id)

    if  post.like.filter(id = request.user.id).exists():
        post.like.remove(request.user)
    
    if not post.dislike.filter(id = request.user.id).exists():
        post.dislike.add(request.user)
    
    if page == 'allpage':
        return redirect(reverse('post:view_all_post'))
    return redirect(reverse('post:view_my_post'))

