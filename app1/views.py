from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import Allitems, Description
from .form import AddItems, AddDescription, FeedbackForm
from app1.serializers import ClassSerializer
from .middleware import authenticateRequired

class ViewSerializer(viewsets.ModelViewSet):
    queryset = Allitems.objects.all()
    serializer_class = ClassSerializer

@authenticateRequired
def home(request):
    datas = Allitems.objects.all()
    context = {'datas':datas}
    return render(request, 'app1/index.html', context)


def itemForm(request):
    if request.method == "POST":
        item_form = AddItems(request.POST, request.FILES or None)
        if(item_form.is_valid()):
            item_form.save()
            return redirect('app1:index')
    else:
        item_form = AddItems()
    context = {'itemform':item_form}
    return render(request, 'app1/itemForm.html', context)


def updateItems(request, item_id):
    itemID = Allitems.objects.get(pk=item_id)
    descID = Description.objects.filter(pk=item_id).first()
    update_itemform = AddItems(request.POST or None, instance=itemID)
    update_descform = AddDescription(request.POST or None, instance=descID)
    if request.method == 'POST':
        if update_itemform.is_valid() and update_descform.is_valid():
            update_itemform.save()
            update_desc = update_descform.save(commit=False)
            if not descID:
                update_desc.pk = itemID.pk
            update_desc.save()
            return redirect('app1:index')
    context = {
        'updateitem': update_itemform,
        'updatedesc': update_descform
    }
    return render(request, 'app1/updateitem.html', context)


def deleteItems(request, item_id):
    delete_item = Allitems.objects.get(pk=item_id)
    delete_desc = Description.objects.filter(pk=item_id).first()
    if delete_desc:
        delete_desc.delete()
    delete_item.delete()
    return redirect('app1:index')


def descForm(request):
    descform = AddDescription(request.POST or None)
    if request.method == 'POST':
        if (descform.is_valid()):
            descform.save()
            return redirect('app1:itemForm')
    content = {'desform':descform}
    return render(request, 'app1/descriptionForm.html', content)


def additems(request):
    item_form = AddItems(request.POST or None)
    if request.method == 'POST':
        if (item_form.is_valid()):
            item_form.save()
            return redirect('app1:index')
    content = {'itemform':item_form}
    return render(request, 'app1/itemForm.html', content)


def aboutUs(request):
    return render(request, 'app1/about.html')

def contact(request):
    if request.method == "POST":
        feedback_form = FeedbackForm(request.POST)
        if(feedback_form.is_valid()):
            feedback_form.save()
        return redirect('app1:index')
    else:
        feedback_form = FeedbackForm()
    context = {'Feedbackform':feedback_form}
    return render(request, 'app1/contact.html', context)



def food(request):
    datas = Allitems.objects.filter(field='food')
    context = {'datas':datas}
    return render(request, 'app1/index.html', context)


def dairy(request):
    datas = Allitems.objects.filter(field='dairy')
    context = {'datas':datas}
    return render(request, 'app1/index.html', context)


def meat(request):
    datas = Allitems.objects.filter(field='meat')
    context = {'datas':datas}
    return render(request, 'app1/index.html', context)


def vegetable(request):
    datas = Allitems.objects.filter(field='vegetable')
    context = {'datas':datas}
    return render(request, 'app1/index.html', context)


def mens(request):
    datas = Allitems.objects.filter(field='mens')
    context = {'datas':datas}
    return render(request, 'app1/index.html', context)


def womens(request):
    datas = Allitems.objects.filter(field='womens')
    context = {'datas':datas}
    return render(request, 'app1/index.html', context)


def kids(request):
    datas = Allitems.objects.filter(field='kids')
    context = {'datas':datas}
    return render(request, 'app1/index.html', context)
