from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseBadRequest


def ajax_required(f):
   """
   AJAX request required decorator
   use it in your views:

   @ajax_required
   def my_view(request):
       ....

   """

   def wrap(request, *args, **kwargs):
       if not request.is_ajax():
           return HttpResponseBadRequest()
       return f(request, *args, **kwargs)

   wrap.__doc__=f.__doc__
   wrap.__name__=f.__name__
   return wrap


def group_required(*group_names):
   """Requires user membership in at least one of the groups passed in."""

   def in_groups(u):
       if u.is_authenticated:
           if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
               return True
       return False
   return user_passes_test(in_groups)


def anonymous_required(function=None, redirect_url=None):

   if not redirect_url:
       redirect_url = settings.LOGIN_REDIRECT_URL

   actual_decorator = user_passes_test(
       lambda u: u.is_anonymous(),
       login_url=redirect_url
   )

   if function:
       return actual_decorator(function)
   return actual_decorator


def superuser_only(function):
  """Limit view to superusers only."""

   def _inner(request, *args, **kwargs):
       if not request.user.is_superuser:
           raise PermissionDenied
       return function(request, *args, **kwargs)
   return _inner


def timeit(method):

   def timed(*args, **kw):
       ts = time.time()
       result = method(*args, **kw)
       te = time.time()
       print('%r (%r, %r) %2.2f sec' % (method.__name__, args, kw, te - ts))
       return result

   return timed
