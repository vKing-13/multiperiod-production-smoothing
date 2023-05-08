# multiperiod-production-smoothing

Multiperiod Production Smoothing is an application for manufacturer or company to predict their production in certain range. The mathematical model that we are using are based on undisclosed company's case study. The documentation can be read on "Multiperiod Production Smoothing Problem.pdf" file. to solve the mathematic model, we ultilized the pulp algorithm from python library which can be used to solve linear programming problems.
Pitching video of FC Startup 23' event:https://www.youtube.com/watch?v=-XrytJg4_VQ&t=33s

![image](https://user-images.githubusercontent.com/63147528/215561661-d88ad63d-f5f1-4c02-a96c-9d5e61e4da8c.png)


## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Dont Forget to Tick Add to Path while installing Python)

- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :

## Install Widget Tweaks
```
pip install django-widget-tweaks
```

## Install Django Compressor
```
pip install django_compressor
```

## Install python XLWT library
```
pip install xlwt
```

## Install PuLp library
```
pip install pulp
```

## Install django-environ 0.9.0
```
pip install django-environ
```

## Run Server

```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```

- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```
