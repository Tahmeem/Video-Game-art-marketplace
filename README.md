# What is this?

A web based marketplace for video game related art. 
All users can make one account and upload art without being labelled creator. 
Users can access art based on what's new or popular. Made with django.

# Installation

Use the package manager pip to install these tools
```bash
pip install django
pip install django-crispy-forms
pip install django-template-maths

```
# Tech Stack
Website uses vanilla html,css, and some javascript for the frontend. In addition bootstrap is used.

Django is used mainly for the backend.

# Sign in/Login 
Works similar to most sign in login pages. All forms on the site are made with crispy forms.
Only after logging in, you can access uploading, editing and deleting your own art. 
Suggestions and reports can only be made after logging in.

# Users Experience
Purchasing art can be done by clicking on buy under the art work. No payment method is set up but there is a checkout page where you can see how much it costs.

![Users Experience](/readmeAssets/5gtwa0.gif)

# Creator's Experience
Creators are able to upload,update and delete art after clicking upload on top right corner. This is only allowed after logging in. 

# Other Features
![Users Experience](/readmeAssets/OtherFeatures.gif)

# Resources
Django: https://docs.djangoproject.com/en/3.2/

Bootstrap: https://getbootstrap.com/docs/5.0/getting-started/introduction/