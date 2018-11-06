from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from blog.models import BlogAuthor, Blog, BlogComment
import datetime

class BlogAuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        BlogAuthor.objects.create(user=test_user1, bio='This is a bio')
        
    def test_get_absolute_url(self):
        author=BlogAuthor.objects.get(id=1)       
        self.assertEquals(author.get_absolute_url(),'/blogger/1')
           
    def test_user_label(self):
        author=BlogAuthor.objects.get(id=1)
        field_label = author._meta.get_field('user').verbose_name
        self.assertEquals(field_label,'user')
        
    def test_bio_label(self):
        author=BlogAuthor.objects.get(id=1)
        field_label = author._meta.get_field('bio').verbose_name
        self.assertEquals(field_label,'bio')

    def test_bio_max_length(self):
        author=BlogAuthor.objects.get(id=1)
        max_length = author._meta.get_field('bio').max_length
        self.assertEquals(max_length,400)
        
    def test_object_name(self):
        author=BlogAuthor.objects.get(id=1)
        expected_object_name = author.user.username
        self.assertEquals(expected_object_name,str(author))
        

class BlogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        blog_author = BlogAuthor.objects.create(user=test_user1, bio='This is a bio')
        blog = Blog.objects.create(name='Test Blog 1',author=blog_author,description='Test Blog 1 Description')
        
    def test_get_absolute_url(self):
        blog=Blog.objects.get(id=1)       
        self.assertEquals(blog.get_absolute_url(),'/blog/1')
           
    def test_name_label(self):
        blog=Blog.objects.get(id=1)
        field_label = blog._meta.get_field('name').verbose_name
        self.assertEquals(field_label,'name')
        
    def test_name_max_length(self):
        blog=Blog.objects.get(id=1)
        max_length = blog._meta.get_field('name').max_length
        self.assertEquals(max_length,200)
        
    def test_description_label(self):
        blog=Blog.objects.get(id=1)
        field_label = blog._meta.get_field('description').verbose_name
        self.assertEquals(field_label,'description')
        
    def test_description_max_length(self):
        blog=Blog.objects.get(id=1)
        max_length = blog._meta.get_field('description').max_length
        self.assertEquals(max_length,2000)

    def test_date_label(self):
        blog=Blog.objects.get(id=1)
        field_label = blog._meta.get_field('post_date').verbose_name
        self.assertEquals(field_label,'post date')
        
    def test_date(self):
        blog=Blog.objects.get(id=1)
        the_date = blog.post_date
        self.assertEquals(the_date,datetime.date.today())

    def test_object_name(self):
        blog=Blog.objects.get(id=1)
        expected_object_name = blog.name
        self.assertEquals(expected_object_name,str(blog))