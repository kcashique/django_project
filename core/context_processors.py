import datetime


def main_context(request):
    datetime.date.today()

    return {
        "domain": request.META["HTTP_HOST"],
        "current_path": request.get_full_path(),
        "site_title": "Project Portal",
    }
