from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect  # , Http404, HttpResponse
from .models import Question, Choice
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
# from django.template import RequestContext, loader


# Each method here is a view. It does some processing and returns the output
#  in some browser recognisable format.


"""
This is the traditional way you define index i.e,
an html page with some context(variables).

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # Get the page to be displayed
    template = loader.get_template('polls/index.html')
    # Specify context. i.e, the variables to be used in the rendered page.
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))

However, Django provides a shortcut method as defined below.
"""


# request is compulsary. It carries data coming in and also some properties
def index(request):
    # Retrieve Question Objects and order by pub_date and then select first 5.
    # You may omit the ordering by using Question.objects.all()[:5].
    # You may get all objects by simply using Question.objects.all().
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    context = {'latest_question_list': latest_question_list,
               'user': request.user}  # variables to pass to html
    # respond and send polls/index.html page with the above context.
    # context is basically the set of variables that are accessed in
    # Django template. These variables are bundled in a dictionary.

    return render(request, 'polls/index.html', context)
    # Here request contains request info such as which host request came from,
    # username of requesting client etc hence helps us to respond to only that
    # host that sent the request.
    # Second arguement is the template to render.
    # Context is set of variable to pass to template.

"""
This is the traditional way you raise a 404(doesnt exist) Error.

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        # raise keyword is used to manually raise an exception.
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

However, Django provides a shortcut mechanism as defined in 'detail' below.
"""


@login_required  # Ensures that user is logged in
# question_id is a parameter collected from URL
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # get object of Question where PrimaryKey=question_id
    #   if it's not present raise 404 error
    return render(request, 'polls/detail.html', {'question': question})


@login_required
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question,
                                                  'user': request.user})


@login_required
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        context = {
            'question': p,
            'error_message': "You didn't select a choice.",
            'user': request.user
        }
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

"""
try...except...else...finally
    -> try block contains a code that might raise an exception
    -> except block is executed if an exception occurs in the try block
       except block is used to catch exception.
       1. To catch all exceptions (generic catch) use :
          except:
       2. To catch a specific exception use:
          except KeyError:
          where KeyError is a type of exception
       3. To catch multiple exceptions and handle them in the same way use:
          except (KeyError, ZeroDivisionError):
          where KeyError and ZeroDivisionError are types of Exceptions.
    -> else block contains a code that follows the try block. i.e,
       the remaining code. else block is not executed if an exception occurs.
    -> finally block contains code that must be executed irrespective of
       occurance of an exception. This block usually contains cleanup code.
"""
