from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Articles, Categories


def set_session(request):
    return request

def exists_session(request):
    return False


# Main : /articles/index
def main(request):
    
    if request.method == 'POST' :
        return main_post(request)

    else :
        if request.method == 'GET' :
            return main_get(request)
        else :
            return HttpResponse("404 not found error please contact administrator")


def main_get(request):
    return render(request,'articlesApp/index.html')
def main_post(request):
    if request.POST.get('category', '') :
        return redirect('articlesApp:add-category')
    
    if request.POST.get('article', '') :
        return redirect('articlesApp:add-article')
    return HttpResponse("Internal error. Please contact administrator")


# Category add page /articles/add-category
def category(request):
    if request.method == 'POST' :
        return category_post(request)
    else :
        if request.method == 'GET' :
            return category_get(request)
        else :
            return HttpResponse("65 not found error please contact administrator")


def get_next_id(a_list):
    return len(a_list)

def name_to_id(name):
    category =  Categories.objects.filter(name=name)
    _id = 0
    for query in category:
        _id = query.id
    return _id

def category_get(request):
    categories = Categories.objects.all()
    return render(request,'articlesApp/add_category.html',
                    {'categories':categories}
                 )
def category_post(request):
    name = request.POST.get('name','')
    description = request.POST.get('description','')
    bol = True
    objects = Categories.objects.all()

    if (name ):
        bol = bol & True 
    if (description) :
        bol = bol & True
    if (len(name) < 10):
        bol = bol & True
    if ( (len(name) > 10) | (len(description) > 100) ):
        bol = bol & False
    for x in Categories.objects.all() :
        if( x.name == name ):
            bol = bol & False
    if bol :
        Categories.objects.mongo_insert_one({
            'id': get_next_id(objects),
            'name':name,
            'description':description
        })
        return render(request,'articlesApp/index.html')
    else :
        return render(request,'articlesApp/add_category.html',{'categories':objects})
    


# Article add page /articles/add-article
def article(request):
    if request.method == 'POST' :
        return article_post(request)

    else :
        if request.method == 'GET' :
            return article_get(request)
        else :
            return HttpResponse("66 not found error please contact administrator")


def article_get(request):
    return render(request,'articlesApp/add_article.html', {'categories':Categories.objects.all()})


def article_post(request):
    title = request.POST.get('title','')
    contributor = request.POST.get('contributor','ANONYMOUS')
    image_link = request.POST.get('image_link','')
    source = request.POST.get('source','unapproved')
    category_name = request.POST.get('category','')
    
    category_id = name_to_id(category_name)
    
    if (category_id < 0):
        return HttpResponse('67 An error occurent please contact administrator')
    html_file = request.POST.get('html_file','')
    try :
        Articles.objects.mongo_insert_one({
                'id' : get_next_id(Articles.objects.all()),
                'title': title,
                'contributor':contributor,
                'image_link':image_link,
                'source':source,
                'html_text':html_file,
            })
    except Exception as e: 
        return HttpResponse("68 error please contact administrator")

    return article_get(request)

    

# feed front page
def feed(request):
    if request.method == 'POST' :
        return HttpResponse("FEED POST")

    else :
        if request.method == 'GET' :
            return render(request,'articlesApp/feed.html')
        else :
            return HttpResponse("69 not found error please contact administrator")


# about page
def about(request):
    if request.method == 'POST' :
        return HttpResponse("about POST")

    else :
        if request.method == 'GET' :
            return HttpResponse("ABOUT GET")
        else :
            return HttpResponse("70 not found error please contact administrator")


# profile front page
def profile(request):
    if request.method == 'POST' :
        return HttpResponse("profile POST")

    else :
        if request.method == 'GET' :
            return HttpResponse("Not developped yet")
        else :
            return HttpResponse("71 not found error please contact administrator")


# contact front page
def contact(request):
    if request.method == 'POST' :
        return HttpResponse("contact POST")

    else :
        if request.method == 'GET' :
            return HttpResponse("contact GET")
        else :
            return HttpResponse("72 not found error please contact administrator")


def post(request, num):
    # fetch post by name
    if request.method == 'POST' :
        return HttpResponse("{} POST".format(num))
    if request.method == 'GET' :
            #return HttpResponse("{} GET".format(name))
            return render(request,'articlesApp/post.html')
    else :
        return HttpResponse("73 not found error please contact administrator")
