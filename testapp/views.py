from django.shortcuts import render
from testapp.forms import signupform
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import logout
from . import forms
import wolframalpha
import wikipedia



# Create your views here.
@login_required
def front_page_view(request):
    return render(request,'testapp/base.html')

@login_required
def home_page_view(request):
    return render(request,'testapp/home.html')


@login_required
def learn_html_view(request):
    return render(request,'testapp/learn_html.html')


@login_required
def learn_css_view(request):
    return render(request,'testapp/learn_css.html')


@login_required
def learn_javascript_view(request):
    return render(request,'testapp/learn_javascript.html')


@login_required
def bot_search(request):
    query = request.GET.get('query')

    try:
        client = wolframalpha.Client("WPY5EU-3942Y4YXJW")
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'testapp/search_page.html', {'ans': ans, 'query': query})


    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request, 'testapp/search_page.html', {'ans': ans, 'query': query})


        except Exception:
            ans = "FOUND NOTHING"
            return render(request, 'testapp/search_page.html', {'ans': ans, 'query': query})


@login_required
def thankyouview(request):
    return render(request,'testapp/thankyou.html')


@login_required
def feedbackview(request):
    if request.method=='GET':
        form=forms.feedbackform()
        return render(request, 'testapp/about.html', {'form': form})

    if request.method=='POST':
        form=forms.feedbackform(request.POST)
        if form.is_valid():
            form.save()
            print("Student Email:", form.cleaned_data['email'])
            return thankyouview(request)
        else:
            return render(request, 'testapp/about.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request,'testapp/logout.html')


def signup_view(request):
    form=signupform()
    if request.method=='POST':
        form = signupform(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})