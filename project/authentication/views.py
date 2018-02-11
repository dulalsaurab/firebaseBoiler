from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from backend.forms import editorForms
from django.utils.datastructures import MultiValueDict as MVD

import pyrebase
import pprint


config = {
    # 'apiKey': "AIzaSyBYcvoauRk13X-4BKUBjY6CO742n6TIJdw",
    # 'authDomain': "shadhan-sahitya-f3a20.firebaseapp.com",
    # 'databaseURL': "https://shadhan-sahitya-f3a20.firebaseio.com",
    # 'projectId': "shadhan-sahitya-f3a20",
    # 'storageBucket': "shadhan-sahitya-f3a20.appspot.com",
    # 'messagingSenderId': "955788043451"
    'apiKey': "AIzaSyC-ibHMnKKUp9YxPondIp9stGqmiAboKsU",
    'authDomain': "shadhan-sahitya.firebaseapp.com",
    'databaseURL': "https://shadhan-sahitya.firebaseio.com",
    'projectId': "shadhan-sahitya",
    'storageBucket': "shadhan-sahitya.appspot.com",
    'messagingSenderId': "860167893486"
    }
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def postSingin(request):
    if request.method == 'POST':
        print("Didnt reached here")
        try:
            if (request.POST['googleAwth']):
                print("I reached inside googleAwth")
                # got user data here, now lets get user credentials
                idToken = request.POST['token']
                request.session['email'] = request.POST['email']
                request.session['token'] = idToken
                # request.sessions["email"] = user['idToken']
                user = {'userNmae':request.POST['email'], 'email': request.POST['email']}
                context = {'userData': user}
                return render(request, "index.html", context)
                # return HttpResponseRedirect('https://www.stackoverflow.com', context)
        except:
            pass
        email = request.POST['email']
        password = request.POST['password']
        #this is to check if request came from sign in to write article
        is_private = request.POST.get("loginForWrite", "notreceived")
        # try:
        #     singInToWrite = request.POST['loginForWrite']
        # except:
        #     pass

        user = auth.sign_in_with_email_and_password(email, password)
        request.session['email'] = email
        request.session['token'] = user['idToken']
        # request.sessions["email"] = user['idToken']
        form = editorForms()
        context = {'userData': user, 'form': form}
        # return HttpResponse(template.render(context, request))

        if is_private == "notreceived":
            return render(request, "index.html", context)
        else:
            return render(request, "editor.html", context)


def editProfile(request):
    return render(request, "authorProfile.html")


def logout(request):
    print("I reached in logout page")
    try:
        del request.session['email']
        del request.session['token']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('home_page'))


# Create your views here.
def login_page(request):
    #lets get what we got through this form
    return render(request, 'login.html', {'registerOn':''})
    try:
        if (request.GET['q']):
            if (request.GET['q'] == "registerOn"):
                return render(request, 'login.html', {'registerOn':'T'})
            else:
                return render(request, 'login.html', {'registerOn':''})
    except:
        return render(request, 'login.html', {'registerOn':''})

def register_page(request):
    print("I reached login_page")
    return render(request, 'register.html')
