from .models import WebRequest


class WebRequestMiddleware(object):
        def process_request(self, request):
            if (request.path != '/get_new_requests/'):
                if request.method == "POST":
                    # just for example
                    WebRequest(request=request.path, priority=2).save()
                else:
                    WebRequest(request=request.path).save()
            return None
