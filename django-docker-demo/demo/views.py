from django.http import HttpResponse


def home(request):
    return HttpResponse("""
        <h1>Hello from Django + Docker! 🐳</h1>
        <p>This application is running inside a Docker container.</p>
    """)


def health(request):
    return HttpResponse("OK")

