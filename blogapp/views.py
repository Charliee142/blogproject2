from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


def index(request):
	recent_post = Post.objects.filter(section='Recent').order_by('-id')[0:4]
	main_post = Post.objects.filter(main_post=True)[0:1]
	categories = Category.objects.all()
	tags = Tag.objects.all()
	archives = Archive.objects.all()
	posts = Post.objects.all().filter(is_published=True).order_by('-created_on')

	
    # Add Paginator
	paginator = Paginator(posts, 1) 
	page = request.GET.get('page')
	
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	

	context = {
        'main_post':main_post,
        'recent_post':recent_post,
        'categories':categories,
        'posts': posts,
        'tags': tags,
		'archives': archives,
    }
	return render(request, "blog_home.html", context)	


@login_required
def post(request, slug):
	requested_post = Post.objects.get(slug=slug)
	categories = Category.objects.all()
	tags = Tag.objects.all()
	archives = Archive.objects.all()

	# Related Posts
 	## Get all the tags related to this article
	post_tags = requested_post.tags.all()
	## Filter all posts that contain tags which are related to the current post, and exclude the current post
	related_posts_ids = (Post.objects.all().filter(tags__in=post_tags).exclude(id=requested_post.id) .values_list("id"))
	related_posts = Post.objects.filter(pk__in=related_posts_ids)

	form = CommentForm()
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(author=form.cleaned_data["author"],body=form.cleaned_data["body"],post=requested_post,)
			comment.save()
			return HttpResponseRedirect(request.path_info)
	comments = Comment.objects.filter(post=requested_post)


	context={
        'categories':categories,
        'tags': tags,
		'archives': archives,
		'post': requested_post,
		'related_posts': related_posts,
		'comments': comments,
		'form': CommentForm(),
	}

	return render(request, "blog_single.html", context)


def category(request, slug):
	posts = Post.objects.filter(categories__slug=slug).filter(is_published=True)
	requested_category = Category.objects.get(slug=slug)
	categories = Category.objects.all()
	recent_post = Post.objects.filter(section='Recent').order_by('-id')[0:4]
	main_post = Post.objects.filter(main_post=True)[0:1]
	tags = Tag.objects.all()

	 # Add Paginator
	paginator = Paginator(posts, 1) 
	page = request.GET.get('page')
	
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	

	context = {
		'tags': tags,
		'posts': posts,
		'main_post':main_post,
		'recent_post':recent_post,
		'category': requested_category,
		'categories': categories,
		
	}
	return render(request, "category.html", context)


def tag(request, slug):
	posts = Post.objects.filter(tags__slug=slug).filter(is_published=True)
	categories = Category.objects.all()
	tags = Tag.objects.all()
	requested_tag = Tag.objects.get(slug=slug)

	 # Add Paginator
	paginator = Paginator(posts, 1) 
	page = request.GET.get('page')
	
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {
		'tags': tags,
		'category': requested_tag,
		'categories': categories,
		'posts': posts,
	}
	return render(request, "tag.html", context) 

def search(request):
	categories = Category.objects.all()
	tags = Tag.objects.all()

	""" search function  """
	query = request.POST.get("search")
	if query:
		posts = Post.objects.filter(is_published=True).filter(title__icontains=query)
	else:
		posts = []

	context = {
		'categories':categories,
		'tags':tags,
		'posts':posts,
		'query': query,
	}
	return render(request, "search.html", context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact = Contact(
            name = name,
            email = email,
            message = message,    
        )
        contact.save()
        return redirect('index')
    return render(request, "contact.html")


def about(request):
   return render(request, "about.html")


def profile(request):
    return render(request, "account/profile.html")

