from django.utils import timezone
from blog.models import Post
from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import CommentForm
# Create your views here.
import logging
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

logger = logging.getLogger(__name__)

def logger_examples():

	username = "mafparra"
	email = "mafernandezparra@gmail.com"

	logger.debug("This is a debug message")
	logger.info("This is an info message")
	logger.warning("This is a warning message")
	logger.error("This is an error message")
	logger.critical("This is a critical message")

	logger.debug("Created user %s with email %s" % (username,
	email))
	logger.debug("Created user %s with email %s", username, email)

	logger.log(logging.DEBUG, "Created user %s with email %s",username, email)
	
	try:
		answer = 9 / 0
		print(f"The answer is: {answer}")
		raise_exception()
	except ZeroDivisionError:
		logger.exception("A divide by zero exception occured")
		

def security_psw():
	import hashlib
	print(hashlib.sha256(b"password").hexdigest())
	print(hashlib.sha256(b"hello wold").hexdigest())
	print(hashlib.sha256(b"password123").hexdigest())
	print("")
	print(hashlib.sha256(b"abc123" + b"password123").hexdigest())
	print("re-hashing")
	
	hash = hashlib.sha256(b"abc123" + b"password123").hexdigest()
	for i in range(1000):
		hash = hashlib.sha256(b"abc123" + hash.encode('ascii')).hexdigest()
	print(hash)



def index(request):
	posts = Post.objects.filter(published_at__lte=timezone.now())
	logger.debug("Got %d posts", len(posts))
	return render(request, "blog/index.html", {"posts": posts})




'''
@cache_page(300)
@vary_on_cookie	
def index(request):
	from django.http import HttpResponse
	logger.debug("Index function is called!")
	return HttpResponse(str(request.user).encode("ascii"))
	posts = Post.objects.filter(published_at__lte=timezone.now())
	logger_examples()
	print("")
	security_psw()
	print("")
	logger.debug("Got %d posts", len(posts))
	return render(request, "blog/index.html", {"posts": posts})


'''

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    

    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                logger.info("Created comment on Post %d for user %s", post.pk,request.user)
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None

    return render(
        request, "blog/post-detail.html", {"post": post, "comment_form": comment_form}
    )
    
    
   
def get_ip(request):
	from django.http import HttpResponse
	return HttpResponse(request.META['REMOTE_ADDR'])
	    
	    
	    
	    
