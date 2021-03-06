from django.contrib.syndication.feeds import Feed
from speakers.models import Presentation,Status,Category

class LatestEntries(Feed):
    title = "UTOSC 2009 Latest Abstracts"
    link = "/speaker/list/all/"
    description = "Latest abstract submissions for UTOSC 2009"

    def items(self):
        return Presentation.objects.all()

class ApprovedPresentations(Feed):
    title = "UTOSC 2009 Presentations"
    link = "/presentation/schedule/"
    description = "Approved Presentations for UTOSC 2009"

    def items(self):
        status = Status.objects.get(name='Approved')
        events = Category.objects.get(name='Event')
        workshops = Category.objects.get(name='Try-It Lab Workshop')
        bofs = Category.objects.get(name='Birds of a Feather (BoF)')
        lugs = Category.objects.get(name='Local User Group')
        return Presentation.objects.filter(status=status).exclude(cat=events).exclude(cat=workshops).exclude(cat=bofs).exclude(cat=lugs).order_by('start')

class BoFList(Feed):
    title = "UTOSC 2009 Birds of a Feather Sessions"
    link = "/presentation/cat/14/"
    description = "BoFs for UTOSC 2009"

    def items(self):
        status = Status.objects.get(name='Approved')
        bofs = Category.objects.get(name='Birds of a Feather (BoF)')
        return Presentation.objects.filter(status=status).filter(cat=bofs).order_by('start')

class LUGList(Feed):
    title = "UTOSC 2009 Local User Group Meetings"
    link = "/presentation/cat/19/"
    description = "BoFs for UTOSC 2009"

    def items(self):
        status = Status.objects.get(name='Approved')
        bofs = Category.objects.get(name='Local User Group')
        return Presentation.objects.filter(status=status).filter(cat=bofs).order_by('start')

class EventList(Feed):
    title = "UTOSC 2009 Events"
    link = "/presentation/cat/16/"
    description = "Events for UTOSC 2009"

    def items(self):
        status = Status.objects.get(name='Approved')
        events = Category.objects.get(name='Event')
        return Presentation.objects.filter(status=status).filter(cat=events).order_by('start')

class WorkshopList(Feed):
    title = "UTOSC 2009 Workshops"
    link = "/presentation/cat/18/"
    description = "Workshops for UTOSC 2009"

    def items(self):
        status = Status.objects.get(name='Approved')
        events = Category.objects.get(name='Try-It Lab Workshop')
        return Presentation.objects.filter(status=status).filter(cat=events).order_by('start')

class KeynoteList(Feed):
    title = "UTOSC 2009 Keynotes"
    link = "/presentation/cat/17/"
    description = "Keynotes for UTOSC 2009"

    def items(self):
        status = Status.objects.get(name='Approved')
        events = Category.objects.get(name='Keynote')
        return Presentation.objects.filter(status=status).filter(cat=events).order_by('start')

