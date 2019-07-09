# Simple Blog Django

## Main aim
To demonstarate user logging in and out with django authentication, preventing anonymous users from reaching unaccessible areas and allowing users to add blog content.

The model is rather basic however in the future I can will add category field and image uploading to blog article. I will create another model for comments and make it a Fk relationship. 

Very basic tests where included:
- Used selenium to open browser to test login.
- Used unit test to check routes
- Used django tests to check template is correct

Views
- blog
- blog/<int:blog_id>/
- blog/create/'
- blog/logout

The reason route "/" does not lead to any page is due to the fact in the future I will add a landing page.

## styling
- normalize
- custom bootstrap-3
- main.css: which has custom styling


## installation
Create Python ENV
pip install django

cd into environment
in terminal type
source bin/activate
cd into SimpleBlog

python manage.py runserver



# super user login: Naive
I would not do this in real practice it is only for tutorial purposes to allow uses to add or remove models.
As they may like to add more fields and alter the models structure

username: admin
password: Password12

# fake users
username1
password: a

username2:
password: b



