from django.shortcuts import render, redirect
from django.contrib import messages
from .models import graph
from gallery.models import category, snippet

# Create your views here.

def home(request):
    graphs = graph.objects.all()
    ctx = {'graphs': graphs}
    return render(request, 'graph/graphs.html', ctx)

def add_graph(request):
    pass
 
def view_graph(request, id):
    g = graph.objects.get(id=id)
    categories =  category.objects.filter(graph=g)
    ctx = {'graph': g, 'categories': categories}
    return render(request, 'graph/view.html', ctx)

def edit_graph(request, id):
    graph = graph.objects.get(id=id)
    form = graph(request.POST or None, request.FILES or None, instance=graph)
    if request.method == 'POST':
        if form.is_valid():
            form.save() # save the form data to model
            messages.success(request, 'Your details added successfully')
            return redirect('home')
        else:
            messages.error(request, 'Error adding your details')
    ctx = {'form': form}
    return render(request, 'graph/graph.html', ctx)

def delete_graph(request, id):
    graph = graph.objects.get(id=id)
    graph.delete()
    messages.success(request, 'Your details added successfully')
    return redirect('home')

