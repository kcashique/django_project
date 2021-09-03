import datetime


def main_context(request):
    today = datetime.date.today()
    return {
        'domain' : request.META['HTTP_HOST'],
    }
