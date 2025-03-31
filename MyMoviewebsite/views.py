from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from app.models import Detail
from app.models import Movie
from app.models import Crausallink
from app.models import Code
from app.models import TCode

def home(request):
    s3=Movie.objects.all()
    s4 = reversed(s3)
    data = list(s4)[:3]
    idunique=1
    
    ss=Crausallink.objects.get(idunique=idunique)

    dict2={
         'data':data,
         'dat':ss,
     
         }
    
    return render(request,'home.html',dict2)

def movie(request,unique):
    movie=Movie.objects.get(unique=unique)
    return render(request,'movie.html',{'movie':movie})

def english(request):
    s3=Movie.objects.all()
    dict1={
        'data':s3
    }
    return render(request,'english.html',dict1)
def marathi(request):
    s3=Movie.objects.all()
    dict1={
        'data':s3
    }
    return render(request,'marathi.html',dict1)
def hindi(request):
    s3=Movie.objects.all()
    dict1={
        'data':s3
    }
    return render(request,'hindi.html',dict1)
def south(request):
    s3=Movie.objects.all()
    dict1={
        'data':s3
    }
    return render(request,'south.html',dict1)
def allmovies(request):
    s3=Movie.objects.all()
    dict1={
        'data':s3
    }
    return render(request,'allmovies.html',dict1)
def adminmain(request):
    return render(request,'admin.html')
def movielist(request):
    s3=Movie.objects.all()
    dict1={
        'data':s3
    }
    return render(request,'movielist.html',dict1)
def addmovies(request):
    if request.method == 'POST':
        unique=request.POST['unique']
        movieimagelink=request.POST['movieimagelink']
        moviename=request.POST['moviename']
        moviedate=request.POST['moviedate']
        description=request.POST['description']
        rating=request.POST['rating']
        director=request.POST['director']
        actors=request.POST['actors']

        english=request.POST['english']
        hindi=request.POST['hindi']
        south=request.POST['south']
        marathi=request.POST['marathi']
        action=request.POST['action']
        comedy=request.POST['comedy']
        drama=request.POST['drama']
        advanture=request.POST['advanture']
        romantic=request.POST['romantic']
        link1=request.POST['link1']
        link2=request.POST['link2']
        link4=request.POST['link4']
   
        if english=='yes':
            english='English'
        else:
            english=''

        if hindi=='yes':
            hindi='Hindi'
        else:
            hindi=''

        if south=='yes':
            south='South'
        else:
            south=''

        if marathi=='yes':
            marathi='Marathi'
        else:
            marathi=''

        if action=='yes':
            action='Action'
        else:
            action=''
        if comedy=='yes':
            comedy='Comedy'
        else:
            comedy=''

        if drama=='yes':
            drama='Drama'
        else:
            drama=''

        if advanture=='yes':
            advanture='Advanture'
        else:
            advanture=''

        if romantic=='yes':
            romantic='Romantic'
        else:
            romantic=''

        md=Movie(unique=unique,movieimagelink=movieimagelink,moviename=moviename,moviedate=moviedate,description=description,rating=rating,director=director,actors=actors,english=english,hindi=hindi,south=south,marathi=marathi,action=action,comedy=comedy,drama=drama,advanture=advanture,romantic=romantic,link1=link1,link2=link2,link4=link4)
        md.save()
        return HttpResponseRedirect('/movielist')
    return render(request,'addmovies.html')
def trending(request):
     if request.method == 'POST':
          code1=request.POST['code1']
          code2=request.POST['code2']
          code3=request.POST['code3']
          code4=request.POST['code4']
          uid=1
          dd=TCode.objects.filter(uid=uid).first()
          dd.code1 = code1
          dd.code2 = code2
          dd.code3 = code3
          dd.code4 = code4
          dd.save()
          return HttpResponseRedirect('/adminmain')
     return render(request,'trending.html')
def crausal(request):
    if request.method == 'POST':
        crausal1=request.POST['crausal1']
        crausal2=request.POST['crausal2']
        crausal3=request.POST['crausal3']
        crausal4=request.POST['crausal4']
        crausal5=request.POST['crausal5']
        idunique=1
        dd=Crausallink.objects.filter(idunique=idunique).first()
        dd.crausal1 = crausal1
        dd.crausal2 = crausal2
        dd.crausal3 = crausal3
        dd.crausal4 = crausal4
        dd.crausal5 = crausal5
        dd.save()
        return HttpResponseRedirect('/adminmain')
    return render(request, 'crausal.html',)

def header(request):
    return render(request,'header.html')
def footer(request):
    return render(request,'footer.html')

def loginlist(request):
    s3=Detail.objects.all()
    dict1={
        'data':s3
    }
    return render(request,'loginlist.html',dict1)
def sign(request):
        
    if request.method == 'POST':
        name=request.POST['name']
        gender=request.POST['gender']
        phone=request.POST['phone']
        otp=request.POST['otp']
        mail=request.POST['mail']
        passw=request.POST['passw']
        rpass=request.POST['rpass']
        d1=Detail(name=name,gender=gender,phone=phone,otp=otp,mail=mail,passw=passw,rpass=rpass)
        if passw == rpass:
            d1.save()
        else:
            return HttpResponseRedirect('/sign')
        
        return HttpResponseRedirect('/login')
    return render(request,'sign.html')

def login(request):
    if request.method == 'POST':
        em=request.POST['mail']
        ps=request.POST['pass']
        s1=Detail.objects.filter(mail=em,passw=ps).exists()
        if s1 == True:
            if em=='admin@gmail.com':
                return HttpResponseRedirect('/adminmain')
            else:
                return HttpResponseRedirect('/')
        return HttpResponseRedirect('/login')
    return render(request,'login.html')

def MyUpdate(request):
    unique=request.GET['unique']
    movieimagelink=request.GET['movieimagelink']
    moviename=request.GET['moviename']
    moviedate=request.GET['moviedate']
    description=request.GET['description']
    rating=request.GET['rating']
    director=request.GET['director']
    actors=request.GET['actors']

    english=request.GET['english']
    hindi=request.GET['hindi']
    south=request.GET['south']
    marathi=request.GET['marathi']
    action=request.GET['action']
    comedy=request.GET['comedy']
    drama=request.GET['drama']
    advanture=request.GET['advanture']
    romantic=request.GET['romantic']
    link1=request.GET['link1']
    link2=request.GET['link2']
    link4=request.GET['link4']
    dict1={
        'unique':unique,
        'movieimagelink':movieimagelink,
        'moviename':moviename,
        'moviedate':moviedate,
        'description':description,
        'rating':rating,
        'director':director,
        'actors':actors,
        'english':english,
        'hindi':hindi,
        'south':south,
        'marathi':marathi,
        'action':action,
        'comedy':comedy,
        'drama':drama,
        'advanture':advanture,
        'romantic':romantic,
        'link1':link1,
        'link2':link2,
        'link4':link4,
        
    }
    return render(request,'MyUpdate.html',dict1)

def Update(request):
    if request.method == 'POST':
        unique=request.POST['unique']
        movieimagelink=request.POST['movieimagelink']
        moviename=request.POST['moviename']
        moviedate=request.POST['moviedate']
        description=request.POST['description']
        rating=request.POST['rating']
        director=request.POST['director']
        actors=request.POST['actors']

        english=request.POST['english']
        hindi=request.POST['hindi']
        south=request.POST['south']
        marathi=request.POST['marathi']
        action=request.POST['action']
        comedy=request.POST['comedy']
        drama=request.POST['drama']
        advanture=request.POST['advanture']
        romantic=request.POST['romantic']
        link1=request.POST['link1']
        link2=request.POST['link2']
        link4=request.POST['link4']

        s1=Movie.objects.get(unique=unique)
        s1.movieimagelink=movieimagelink
        s1.moviename=moviename
        s1.moviedate=moviedate
        s1.description=description
        s1.rating=rating
        s1.director=director
        s1.actors=actors
        s1.english=english
        s1.hindi=hindi
        s1.south=south
        s1.marathi=marathi
        s1.action=action
        s1.comedy=comedy
        s1.drama=drama
        s1.advanture=advanture
        s1.romantic=romantic
        s1.link1=link1
        s1.link2=link2
        s1.link4=link4
        s1.save()
        return HttpResponseRedirect('/movielist')
    
def MyDelete(request):
    uniq=request.GET['unique']
    s1=Movie.objects.get(unique=uniq)
    s1.delete()
    return HttpResponseRedirect('/movielist')