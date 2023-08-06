# import os module
import os
# DJANGO IMPORTS
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Import mimetypes module
import mimetypes
# PROJECT IMPORTS
from fcmnotify.models import UserFcmToken, FCMSettings


@csrf_exempt
def save_user_fcm_token(request):
    try:
        token = request.POST.get('token')
        user, created = UserFcmToken.objects.get_or_create(user=request.user)
        if created:
            print("Token object created", user)
        user.fcm_token = token
        user.save()
        return HttpResponse("TOKEN SAVED")
    except Exception as e:
        print("user-not found", e)
        return HttpResponse("UNABLE TO SAVED TOKEN")


def showFirebaseJS(request):
    fcm = get_object_or_404(FCMSettings, is_active=True)
    fcm_config = 'var firebaseConfig = { apiKey: "' + f"{fcm.api_key}" + '",authDomain:"' + f"{fcm.auth_domain}" + '",databaseURL: "' + f"{fcm.database_URL}" + '",projectId:"' + f"{fcm.project_id}"+'" ,storageBucket:"' + f"{fcm.storage_bucket}"+'",messagingSenderId:"' + f"{fcm.messaging_sender_id}"+'",appId:"' + f"{fcm.app_id}"+'",measurementId:"' + f"{fcm.measurement_id}"+'"};' # noqa

    data = \
        'importScripts(' \
        '"https://www.gstatic.com/firebasejs/7.14.6/firebase-app.js");' \
        'importScripts(' \
        '"https://www.gstatic.com/firebasejs/7.14.6/firebase-messaging.js");' \
        f'{fcm_config}' \
        'firebase.initializeApp(firebaseConfig);' \
        'const messaging=firebase.messaging();' \
        'messaging.setBackgroundMessageHandler(function (payload) {' \
        '    console.log(payload);' \
        '    const notification=JSON.parse(payload);' \
        '    const notificationOption={' \
        '        body:notification.body,' \
        '        icon:notification.icon' \
        '    };' \
        '    return ' \
        'self.registration.showNotification(payload.notification.' \
        'title,notificationOption);' \
        '});'

    return HttpResponse(data, content_type="text/javascript")


def download_file(request):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = 'fcm_settings.html'
    
    filepath = os.path.join(BASE_DIR + "download") + filename
    path = open(filepath, 'w')
    fcm = get_object_or_404(FCMSettings, is_active=True)
    fcm_config = 'var firebaseConfig = { apiKey: "' + f"{fcm.api_key}" + '",authDomain:"' + f"{fcm.auth_domain}" + '",databaseURL: "' + f"{fcm.database_URL}" + '",projectId:"' + f"{fcm.project_id}"+'" ,storageBucket:"' + f"{fcm.storage_bucket}"+'",messagingSenderId:"' + f"{fcm.messaging_sender_id}"+'",appId:"' + f"{fcm.app_id}"+'",measurementId:"' + f"{fcm.measurement_id}"+'",usePublicVapidKey:"' + f"{fcm.use_public_vapid_key}"+'" };' # noqa

    write_contain = '<script src="https://www.gstatic.com/firebasejs/7.14.6/firebase-app.js"></script> ' \
                    '<script src="https://www.gstatic.com/firebasejs/7.14.6/firebase-messaging.js"></script>' \
                    '<script>'\
                    + fcm_config + '' \
                    'firebase.initializeApp(firebaseConfig);' \
                    'const messaging=firebase.messaging();' \
                    'function IntitalizeFireBaseMessaging() {' \
                    'messaging.requestPermission().then(function () {' \
                    'console.log("Notification Permission");' \
                    'return messaging.getToken();' \
                    '})' \
                    '.then(function (token) {' \
                    'console.log("Token : "+token);' \
                    'sendToServer(token);' \
                    '}).catch(function (reason) {' \
                    'console.log(reason);' \
                    '});}' \
                    'messaging.onMessage(function (payload) {' \
                    'console.log(payload);' \
                    'const notificationOption={' \
                    'body:payload.notification.body,' \
                    'icon:payload.notification.icon' \
                    '};' \
                    'if(Notification.permission==="granted"){' \
                    'var notification=new Notification(payload.notification.title,notificationOption);' \
                    'notification.onclick=function (ev) {' \
                    'ev.preventDefault();' \
                    ' window.open(payload.notification.click_action,"_blank");' \
                    ' notification.close();' \
                    '}' \
                    '}' \
                    '});' \
                    'messaging.onTokenRefresh(function () {' \
                    'messaging.getToken()' \
                    '.then(function (newtoken) {' \
                    'console.log("New Token : "+ newtoken);' \
                    'sendToServer(newtoken);' \
                    '}).catch(function (reason) {console.log(reason);}) });' \
                    'function sendToServer(token){' \
                    '$.ajax({' \
                    'url:"/save_fcm_token/",' \
                    'type:"POST",' \
                    'data:{token:token},' \
                    '})' \
                    '.done(function(response){' \
                    'if(response=="TOKEN SAVED"){' \
                    'console.log("Save")' \
                    '}' \
                    'else{' \
                    ' console.log("Error in Token Save")' \
                    '}' \
                    '});' \
                    '}' \
                    'IntitalizeFireBaseMessaging();' \
                    '</script>'
    path.write(write_contain)
    path = open(filepath, 'r')
    mime_type, _ = mimetypes.guess_type(filepath)
    response = HttpResponse(path, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response



