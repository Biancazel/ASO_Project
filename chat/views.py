from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from .forms import UploadFileForm
from .models import Message


# Create your views here.
def chatPage(request, *args, **kwargs):
    global form, file_url
    form = UploadFileForm()
    file_url = None
    if not request.user.is_authenticated:
        return redirect("login-user")
    latest_messages_list = Message.objects.order_by("-timestamp")[:10]
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            file_url = "media/" + str(request.FILES['file'])

    context = {"latest_messages_list": reversed(latest_messages_list), "image": file_url, "form": form}
    file_url = None
    return render(request, "ChatPage.html", context=context)


def handle_uploaded_file(f):
    with open('media/' + str(f), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
