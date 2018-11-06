# django-blog
A blog written with Django 2.1


### First create the image:
```
docker build -t django-blog .
```
Or you can use the jenkins image. Refer to  [this repo's](https://github.com/miladino43/Jenkins-django-blog) Readme for more information.
### Then run the container:
```
docker run -d -p 80:8000 django-blog
```

if you would like to add changes on the fly make sure you are in the django-blog directory, then:
```
docker run -v $(pwd)/src:/src -d -p 80:8000 django-blog
```

#### Creds
```
username: admin
password: passwordEA
```

```
Username: Tester
Password: password!@#
```
### Guide
You can create post using the admin user.

1. Navigate to localhost/admin and login using admin creds. 
2. Click on Blogs
3. Click "ADD BLOG" on top right corner.
4. Create a post using the form.