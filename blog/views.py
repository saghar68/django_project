from django.shortcuts import render,redirect
from .models import Post
from django.shortcuts import get_object_or_404
#from django.contrib.auth.models import User
from .forms import New_Post,Search_form
from django.db.models import Q
from django.views import generic
from django.urls import reverse_lazy



# class Post_List(generic.ListView):
#     model=Post
#     template_name='blog/home.html'
#     context_object_name='posts'



def Post_list(request):
    posts=Post.objects.filter(status='pub').order_by('-date_modified')
    form_search=Search_form()
    if 'search' in request.GET:
        form_search=Search_form(request.GET)
        if form_search.is_valid():
            s=form_search.cleaned_data['search']
            posts=posts.filter(Q(title__contains=s)|Q(text__contains=s))
            
    return render(request,'blog/home.html',{'posts':posts,'form_search':form_search})



class Post_Detail(generic.DetailView):#pk
    model=Post
    template_name='blog/detail.html'
    context_object_name='posts'
    

# def detail(request,post_id):
#     #return HttpResponse(f'id:{post_id}')
#     posts=get_object_or_404(Post,id=post_id)
#     return render(request,"blog/detail.html",{'posts':posts})
    
# def page_not_found(request,exception):
#     return render(request,'blog/error.html')

class Post_Create(generic.CreateView):
    form_class=New_Post
    #model=Post
    #fields=['title','text']
    template_name='blog/add.html'
 
    
# def create(request): 
#      if request.method=='POST':
#         forms=New_Post(request.POST) 
#         if forms.is_valid():
#             forms.save()
#             return redirect('home')
            
        
#      else:
#          forms=New_Post()

#      return render(request,"blog/add.html",{'forms':forms})


class Post_Update(generic.UpdateView):
    form_class=New_Post
    template_name='blog/add.html'
    model=Post
    
    
    
    
     
# def Edit(request,post_id):
#     posts=get_object_or_404(Post,id=post_id)
#     forms=New_Post(request.POST or None,instance=posts)
#     if forms.is_valid():
#         forms.save()
#         return redirect('home')
#     return render(request,"blog/add.html",{'forms':forms})



class Post_Delete(generic.DeleteView):
    model=Post
    template_name='blog/delete.html'
    success_url=reverse_lazy('home')
    
    
    
    
    
# def delete(request,post_id):
#     posts=get_object_or_404(Post,id=post_id)
#     posts.delete()
#     return redirect('home')



#crud 