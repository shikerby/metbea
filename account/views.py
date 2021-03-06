from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages

from .forms import MyAuthForm, UserRegisterForm, UserEditForm, ProfileEditForm, UserWritePostForm, SetPostPublishTimeForm
from .models import Profile

from django.contrib.auth.models import User
from blog.models import Post

@login_required
def home(request):
    # 在对象筛选器中过滤查询集, 筛选出在一天之内发布的信息
    # 在home页的综合排序选项中筛选出一周内 综合评分在8分以上的信息,按时间先后排序
    lasted_posts = Post.published.all()[:15]
    return render(request, 'account/home.html', {'lasted_posts': lasted_posts})
    

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            # messages.success(request, 'Profile updated successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form, 'section': 'editprofile'})


@login_required
def write_post(request):
    new_post = None
    if request.method == 'POST':
        write_form = UserWritePostForm(data=request.POST)
        if write_form.is_valid():
            new_post = write_form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('set_pubtime', args=(new_post.id,)))
    else:
        write_form = UserWritePostForm()
    return render(request, 'account/writing.html', {'write_form': write_form})


@login_required
def setpubtime(request, id):
    current_post = Post.objects.get(author=request.user, id=id)
    if request.method == 'POST':
        setform = SetPostPublishTimeForm(request.POST)
        if setform.is_valid():
            current_post.publish = setform.cleaned_data['pub_time']
            current_post.status = 'waiting'
            current_post.save(update_fields=['publish', 'status'])
        return render(request, 'account/finish_setting.html', {'current_post': current_post})
    else:
        setform = SetPostPublishTimeForm()
    return render(request, 'account/set_pubtime.html', {'current_post': current_post, 'setform': setform})


@login_required
def visit_homepage(request, id):
    blogger = User.objects.get(pk=id)
    all_blogger_posts = Post.objects.filter(author=blogger)
    published_posts = all_blogger_posts.filter(status='published').order_by('status', '-publish')
    blogger_latest_post = published_posts[:1]
    the_best_of_posts = published_posts.order_by('-pv')[:3]
    return render(request, 'account/hisspace.html', {'blogger': blogger,
                                                     'all_blogger_posts': all_blogger_posts,
                                                     'blogger_latest_post': blogger_latest_post,
                                                     'the_best_of_posts': the_best_of_posts})


def register(request):
    where = 'register'
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegisterForm()
    return render(request, 'registration/register.html', {'section': where, 'user_form': user_form})


class MyLoginView(LoginView):
    form_class = MyAuthForm
    template_name = 'account/index.html'
    redirect_authenticated_user = 'home'
