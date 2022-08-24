'''
Views are where we write the logic of our application. 

They will request information from the model we've created, and pass it to a template.  
'''

from django.shortcuts import render

# Create your views here.
def post_list(request):
    '''
    Takes a request and returns the value it gets from calling the 'render' function.  It then renders it using our template, blog/post_list.html. 
    '''
    return render(request, 'blog/post_list.html', {})