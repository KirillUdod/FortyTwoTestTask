from .models import WebRequest


class WebRequestMiddleware(object):
        def process_request(self, request):
            if (request.path != '/get_new_requests/'):
                WebRequest(request=request).save()
            else:
                return
