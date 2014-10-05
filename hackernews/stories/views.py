import datetime
from django.shortcuts import render_to_response
from django.utils.timezone import utc
from django.template import RequestContext

from future_builtins import  ascii
from .models import Story


def score(story, gravity=1.8, timebase=120):
    points = (story.points - 1)**0.8
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    age = int((now - story.created_at).total_seconds())/60
    return  points/(age*timebase)**1.8

def top_stories(top=180, consider=1000):
    latest_stoties = Story.objects.all().order_by('-created_at')[:consider]
    ranked_stories = sorted([(score(story), story) for story in latest_stoties], reverse=True)
    return [story for _, story in ranked_stories[: top]]

def index(request):
    stories = top_stories(top=30)
    context = RequestContext(request, {
        'stories': stories
    }
                             )
    return render_to_response('stories/index.html', context)