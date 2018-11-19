from django.shortcuts import render, redirect
from facebook.models import Article
from facebook.models import Comment

# Create your views here.
def facebook(request):
    return render(request, 'facebook.html')

def play(request):
    return render(request, 'play.html')

count = 0
def play2(request):
    GooJakyoung = '구자경'
    age = 22

    global count
    count = count + 1

    if age > 19:
        status = '성인'
    else:
        status = '청소년'

    diary = ['오늘은 날씨가 맑았다. - 4월 3일', '미세먼지가 너무 심하다. (4월 2일)', '비가 온다. 4월 1일에 작성']

    return render(request, 'play2.html', {'name' : GooJakyoung, 'cnt' : count, 'age': status, 'diary' : diary, 'event' : event})

def profile(request):
    return render(request, 'profile.html')

def event(request):
    GooJakyoung = '구자경'
    age = 22

    global count
    count = count + 1

    if age > 19:
        status = '성인'
    else:
        status = '청소년'

    if count == 7:
        event = '당첨'
    else:
        event = '꽝'

    return render(request, 'event.html',
                  {'name': GooJakyoung, 'cnt': count, 'age': status, 'event': event})

def fail(request):
    return render(request, 'fail.html')

def help(request):
    return render(request, 'help.html')

def warn(request):
    return render(request, 'warn.html')

def newsfeed(request):
    articles = Article.objects.all()
    return render(request, 'newsfeed.html', {'articles' : articles})

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST': # new comment
        Comment.objects.create(
            article=article,
            author=request.POST.get('nickname'),
            text=request.POST.get('reply'),
            password=request.POST.get('password'),
        )
        return redirect(f'/feed/{article.pk}')

    return render(request, 'detail_feed.html', {'feed' : article})

def new_feed(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        new_article = Article.objects.create(
            author=request.POST['author'],
            title=request.POST['title'],
            text=request.POST['content']  + '- 추신: 감사합니다.',
            password=request.POST['password']
        )

        # 새글 등록 끝

    return render(request, 'new_feed.html')

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/') #첫페이지로 이동하기

    return render (request, 'remove_feed.html', {'feed': article})

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':

        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{article.pk}')

    return render (request, 'edit_feed.html', {'feed':article})