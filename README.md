# WebVR-project
a little experiment with WebVR and Django

<h2>Initial Installation</h2>
<ol>
  <li>You must install Django(of course python too) in your Desktop : $ pip install Django</li>
  <li>You must install <a href="https://pypi.org/project/django-colorful/">Django-colorful</a> for color object : $ pip install django-colorful</li>
  <li>You must install mysqlclient : $ pip install mysqlclient</li>
  <li>You must install django-crispy for template problem : $ pip install django-crispy</li>
  <li>You must install Pillow for Image Field : $ pip install Pillow</li>
  <li>You must install django-extra-views for create, update view : $ pip install django-extra-views
</ol>

<h2>DataBase Settings</h2>
<ol>
  <p>In this project, I used a database called MySQL with Bitnami XAMP. So, for copping the settings.py, you have to install MySQL DataBase and Set your DataBase ID and PW in Settings.py. Or, you can change the settings  for SQLite in Settings.py</p>

<h2>Running Django Server</h2>
<ol>
  <li>open cmd in your desktop</li>
  <li>go to the directory where your 'manage.py' located</li>
  <li>input 'python manage.py runserver'</li>
  <li>open your browser and browse "http://127.0.0.1:8000/"</li>
  <p>//if there is a error by the port, try to change your port like 'python manage.py runserver 8080'</p>
</ol>
