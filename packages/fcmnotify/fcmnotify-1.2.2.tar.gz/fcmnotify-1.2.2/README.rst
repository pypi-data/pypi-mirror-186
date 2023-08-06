
fcmnotify is a simple Django app to conduct Web-based fcmnotify. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------
1. Add "fcmnotify" to your INSTALLED_APPS setting like this::

    pip install fcmnotify


2. Add "fcmnotify" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'fcmnotify',
    ]

3. Include the fcmnotify URLconf in your project urls.py like this::

    path('', include('fcmnotify.urls')),
     or
    # url(r'^', include('fcmnotify.urls')),

4. Run `python manage.py migrate` to create the polls models.

5. Start the development server and visit http://127.0.0.1:8000/admin/
   to create Firebase information.

   Go into Fcmnotify > fcmsettings
   Add Firebase information .
   visit http://127.0.0.1:8000/fcm-settings/ To download HTML SETTINGS file
   include download HTML file into base html file {% include 'fcm_settings.html' %}


6. To send Notifications .
    Call "from fcmnotify.sender import fcm_notify"
    send notification using fcm_notify
    fcm_notify(sender, recipient, message, title="DK", dataObject=None)
    
7. NOTE: 
    Make sure you have jQuery, Your Browser should have notification permission
