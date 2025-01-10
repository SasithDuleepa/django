# middleware.py
from django.utils.timezone import now

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        self.excluded_paths = ['/playground/api/']
        # Code executed for each request before the view is called
        print(f"Request received at {now()} - Path: {request.path}")

        response = self.get_response(request)

        # Code executed for each response after the view is called
        print(f"Response sent at {now()} - Status: {response.status_code}")
        return response
