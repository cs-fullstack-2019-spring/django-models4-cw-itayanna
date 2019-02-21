from django.shortcuts import render
from django.http import HttpResponse
from .models import Mom, Child
# Create your views here.

def index(request):
    return HttpResponse('index')

def children(request):
        childs = Child.objects.all()

        for kid in childs:
            print(f'{kid.child_first_name} {kid.child_last_name}')

            for mom in Mom.objects.filter(childs_mom__mom_first_name=mom.mom_first_name):
                print(f'{mom.mom_first_name} {mom.mom_last_name}')

        return HttpResponse('List Children and their Moms')

def moms(request):
        mother = Mom.objects.all()

        for mom in mother:
            print(f'{mom.mom_first_name} {mom.mom_last_name}')

            for kid in Child.objects.filter(moms_child__child_first_name=kid.child_first_name):
                print(f'{kid.child_first_name} {kid.child_last_name}')

        return HttpResponse('List Children and their Moms')
def addchild(request):


