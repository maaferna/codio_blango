from blog.models import Post, Comment

comments = []

for post in Post.objects.all():
	comments.append(Comment(creator=post.author, content="Thank you for reading my post!", content_object=post)

Comment.objects.bulk_create(comments)
