from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from crowdsourcing.models import Survey

@login_required(login_url='login/')
def home(request):
    latest_survey = None
    surveys = Survey.live.order_by('-survey_date')
    if surveys:
        latest_survey = surveys[0]
    return render_to_response(
        "home.html",
        {"latest_survey": latest_survey},
        RequestContext(request))

