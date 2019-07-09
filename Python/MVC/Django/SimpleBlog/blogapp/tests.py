# Python testing dependencies
import unittest

# DJANGO testing dependencies
from django.test import Client, TestCase, SimpleTestCase
from django.urls import resolve
from django.http import HttpRequest

# Selenium browser testing dependencies
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time

# Local dependencies views and models
from blogapp.models import BlogArticle
from blogapp.views import index, create_blog, single_blog, logout_view

""" Simple Tests"""

class RouteTest(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_index(self):
        # Issue a GET request.
        response = self.client.get('/blog/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/blog/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        request.user = None  
        response = index(request)  

        html = response.content.decode('utf8')  
        
        self.assertTrue(html.startswith('<!DOCTYPE html>'))  
        self.assertIn('<title>DailiesTech</title>', html)  
        self.assertTrue(html.endswith('</html>')) 

    def test_single_blog(self):
        # Issue a GET request.
        response = self.client.get('/blog/2/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)
    
    def test_blogid_resolves_to_single_blog_page_view(self):
        found = resolve('/blog/2/')
        self.assertEqual(found.func, single_blog)
    

class LoginRequiredRoutes(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_create_blog(self):
        # Issue a GET request.
        response = self.client.get('/createblog/')

        # Check that the response is 302 requires user to be logged in
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        # Issue a GET request.
        response = self.client.get('/logout/')

        # Check that the response is 302 requires user to be logged in
        self.assertEqual(response.status_code, 302)

class UserLogin(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_login(self):
        response = self.client.post('/blog/', {'username': 'admin', 'password': 'Password12'})
        self.assertEqual(response.status_code, 200)



class MySeleniumTests(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('myuser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()


### run coverage coverage run --source='.' manage.py test blogapp