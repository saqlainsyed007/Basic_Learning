from django.conf.urls import include, url
from django.contrib import admin
from . import views

# specify List of URL patterns
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^login/', views.login_form, name='login'),
    url(r'^login_authenticate/', views.login_authenticate,
        name='login_authenticate'),
    url(r'^logout/', views.logout_view, name='logout')
]

"""
This is project's URLs. When you type a URL, Django will discard
localhost:8000/ and bring the rest of the string here to match.
Matching is done using regular expressions.
The 1st arguement indicates url pattern to match. Here r indicates regular
  expression followed by the expression to match in ''. Note that ^ indicates
  begins with and $ indicates ends with. Eg: r'^[0-9]/$' indicates begins with
  a single digit and ends with /. Fix value we use r^value$ as in r^admin/$.
The 2nd arguement indicates the action to be taken either it can be redirect to
  another urls.py or to call a view. If the action is to redirect, the matched
  pattern is discarded and only the remainder is redirected. The urls.py to
  redirect to is specified using include(). Eg: If localhost:8000/admin/polls/
  is our URL, initially, localhost:8000/ is removed. Now remaining admin/polls/
  is matched with patterns in each URL. It begins with admin/ hence first url
  in the list is the match. Now discard the matched pattern admin/. You are
  left with polls/. The action is to include polls.urls. Hence polls/ is given
  to polls/urls.py and the matching is done again in that file as done here.
  If the action is for a view is to be called, we use views.view_name. If
  pattern matches, view is called.
The 3rd arguement is just to give a name to the url
"""

handler404 = 'mysite.views.error404'
handler500 = 'mysite.views.error500'

"""
Django will render default error pages when some problem occurs. If we want to
customize them we must specify handler<error_code> = '<handler_view>' as shown
above. Note that django will look for custom handlers only in the urls.py file
specified in the ROOT_URLCONF variable in settings.py and no where else.
Also if you want to see the effects of the custom handlers you must set
DEBUG = False in your settings.py otherwise django renders the errors in your
code rather than error pages.
"""
