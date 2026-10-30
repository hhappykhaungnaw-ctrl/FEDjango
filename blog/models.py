from django.db import models

class User(models.Model):
    user_id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=225, null=True, blank=True)
    password =models.CharField(max_length=225, null=True, blank=True)
    role =models.CharField(max_length=100, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'user'
        
    def __str__(self):
        return str(self.name)
    
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=225, null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table ='category'
    
    def __str__(self):
        return str(self.name)

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    
    class Meta:
        db_table ='post'
        
    def __str__(self):
        return str(self.title)
    
class Comment(models.Model):
    STATUS_CHOICES = (
        ('approved', 'Approved'),
        ('pending', 'Pending'),
        ('rejected', 'Rejected'),
    )
    comment_id = models.AutoField(primary_key=True)
    content = models.TextField()
    status = models.CharField(max_length=100, null=True, blank=True, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    class Meta:
        db_table ='comment'
        
    def __str__(self):
        return str(self.content)
    
class UserProfile(models.Model):
    VISIBILITY_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    profile_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='public')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'user_profile'
    
    def __str__(self):
        return str(self.user_id)

class Tag (models.Model):
    tag_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    TAG_CHOICES = [
        ('programming', 'Programming'),
        ('design', 'Design'),
        ('business', 'Business'),
        ('other', 'Other')]
    
    tag_type = models.CharField(max_length=50, choices=TAG_CHOICES, default='programming')
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        db_table = 'Tag'
    def __str__(self):
        return str(self.name)
    
class PostTag(models.Model):
    post_tag_id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'post_tag'
    def __str__(self):
        return f"Post: {self.post_id.title}, Tag: {self.tag_id.name}"
    
class PostLike(models.Model):
    like_id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'post_like'
    
    def __str__(self):
        return f"User: {self.user_id.name}, Post: {self.post_id.title}"
    