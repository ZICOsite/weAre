from django.shortcuts import render,redirect
from .forms import ContactForm
from .bot import get_contact


def index(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email= request.POST.get('email')
        phone = request.POST.get('phone')
        text_message=request.POST.get('text_message')
        x = str("name : " + name + "\n"
                                   'surname : ' + surname + "\n" 'email : ' + email + "\n"
                                                            'phone : ' + phone + "\n" 'text_message : ' + text_message + "\n")
        get_contact(x)
        if form.is_valid():
            form.save()
            return redirect("index")
    context = {'form': form,}
    return render(request, "index.html", context)