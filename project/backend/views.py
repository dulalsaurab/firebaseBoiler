from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
# following are renders created for front end test purpose
# will be deleted once the haldler for each request will be created

#index.html file is obtained from template directory

from .forms import editorForms
from authentication import views
import pyrebase

def editor(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("I reached here")
        # create a form instance and populate it with data from the request:
        form = editorForms(request.POST)
        auth = firebase.auth()
        # check whether it's valid:
        if form:
            try:
                if request.session['email']:
                    title = request.POST['title']
                    description = request.POST['shortInfo']
                    article = request.POST['text']
                    tags = request.POST['tags']
                    db = views.firebase.database()
                    data = {
                        "content": article
                    }
                    results = db.child("posts").push(data, user[request.session['token']])

                    print(request.session['token'])
                    return HttpResponse("You are logged in")
            except Exception as e:
                print(e)
                return HttpResponse("You are not logged in")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = editorForms()
        try:
            if request.session['email']:
                user = {'userNmae':request.POST['email'], 'email': request.POST['email']}
                context = {'userData': user}
                data = {'userData': 'session found', 'form':form }
        except:
            data = {'form': form}

    return render(request, 'editor.html', data)


def articleHandler(request):
    pass


def home_page(request):
    # check if a user is passed in get request, and if user is passed, check if its cookies or seession exist
    # if exist send user
    try:
        if request.session['email']:
            print(request.session['email'])
            a = request.session['email']
            data = {'userData': a }
            user = {'userNmae':request.session['email'], 'email': request.session['email']}
            context = {'userData': user}
    except Exception as e:
        context = None
    return render(request, 'index.html', context)

def login_page(request):
    print("I reached login_page")
    return render(request, 'login.html')

def post_page(request):

    # get database content
    # Get a reference to the database service
    db = views.firebase.database()
    dbArticle = db.child('posts').get()
    articleJson = {'article': dict(dbArticle.val())} #convert into dictonary
    # print(users.val())
    # this prints content from the data base
    return render(request, 'post.html', articleJson)

def author_profile(request):
    return render(request, 'author.html')
