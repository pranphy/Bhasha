import datetime

from django.views.generic import View

from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone


from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404

from django.template import RequestContext
from django.template import loader

from .models import BaseWord
from .models import Pos
from .models import SubWord
from .models import Meaning


from .forms import CommentForm

class KoshIndex(View):
    def get(self,request):
        #allposts = BlogPost.objects.all()
        template = loader.get_template('kosh/index.html')
        allbwords = BaseWord.objects.all()
        allswords = SubWord.objects.all()
        allwords = [word for word in allbwords] + [word for word in allswords]
        print('allwords is ')
        print(allwords)
        context = {
            'allwords':allwords
        }
        return HttpResponse(template.render(context,request))


class WordMeaning(View):
    def get(self,request,pslug):
        template = loader.get_template('kosh/meaning.html')
        word = BaseWord.objects.filter(word=pslug)
        form = CommentForm()
        context = {
            'word':word,
            'form':form
        }
        
        return HttpResponse(template.render(context,request))

'''class BlogDetail(View):
    def get(self,request,pslug):
        currentpost = get_object_or_404(BlogPost,slug=pslug) 
        comments = Comment.objects.filter(blogpost=currentpost)
        template = loader.get_template('blog/details.html')
        form = CommentForm()
        context = {
            'post' : currentpost,
            'form' : form,
            'comments' : comments,
        }
        return HttpResponse(template.render(context,request))

    def post(self,request,pslug):
        currentpost = get_object_or_404(BlogPost,slug=pslug) 
        name = request.POST.get('commenter')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        CommentObject = Comment(
            commenter=name,
            comment=comment,
            blogpost=currentpost
        )
        CommentObject.save()
        return HttpResponseRedirect('/blog/detail/'+pslug)
'''
    
class BlogDownload(View):
    def get(self,request):
        template = loader.get_template('kosh/download.html')
        context = {}
        return HttpResponse(template.render(context,request))

def handler404(request):
    response = render_to_response('404.html',{},context_instance=RequestContext(request))
    response.status_code = 404
    return response

