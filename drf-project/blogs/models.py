from django.db import models

# Model to store blog posts
class Blog(models.Model):
    """
    Represents a blog post with a title and body content.
    """
    blog_title = models.CharField(max_length=100)  # Blog title with max length of 100 characters
    blog_body = models.TextField()  # Main content of the blog

    def __str__(self):
        return self.blog_title  # Returns the title when printing the object


# Model to store comments on blog posts
class Comment(models.Model):
    """
    Represents a comment related to a blog post.
    """
    blog = models.ForeignKey(
        Blog, 
        on_delete=models.CASCADE,  # Deletes comments if the associated blog is deleted
        related_name='comments'  # Enables reverse access from Blog to its comments
    )
    comment = models.TextField()  # The actual comment content

    def __str__(self):
        return self.comment[:50]  # Returns a preview (first 50 chars) of the comment
