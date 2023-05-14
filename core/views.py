from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Entries as Profile,Files
import pandas as pd
from payroll_management.settings import STATIC_URL
from datetime import date
import inflect

from django.contrib.auth.forms import UserCreationForm

# import io
# from django.http import FileResponse
# from reportlab.pdfgen import canvas
# from reportlab.lib.units import inch
# from reportlab.lib.pagesizes import letter
from xhtml2pdf import pisa
from io import BytesIO
import os
from django.http import HttpResponse
from django.template.loader import get_template

from . form import ProfileForm,CreateUserForm
month_list=['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

@login_required(login_url='login')
def create_user(request):
    if not request.user.is_staff:
        return redirect('home')
    
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        form.save()
    
    form=CreateUserForm()

    return render(request,'core/user_creation.html',{'form':form})

def loginUser(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.object.get(username=username)
        except:
            print('username Does Not Exist !!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect(request.GET['next'] if 'next' in request.GET else 'dashboard_admin')
            return redirect(request.GET['next'] if 'next' in request.GET else 'home')
        else:
            messages.error(request,'User Name or password is incorrect')
    context = {'page': 'Login'}
    return render(request, 'core/login_register.html', context)



@login_required(login_url='login')
def dashboard_admin(request):
    if not request.user.is_staff:
        return redirect('home')
    file=Files.objects.all()
    return render(request, 'core/dashboard_admin.html',{'files':file})

@login_required(login_url='login')
def convert_to(request,pk):
    if not request.user.is_staff:
        return redirect('home')
    file=Files.objects.get(id=pk)
    if file.is_converted:
        return redirect('dashboard_admin1',pk=pk)
    month=file.month
    year=file.year
    file.is_converted=True
    file.save()
    upload=str(file.upload)
    loc=STATIC_URL+'files/'+upload
    df=pd.read_excel(loc)
    df=df.iloc[3:,:]
    x,y=df.shape
    for i in range(x):
        # for j in range(y):
        #     print(df.iloc[i,j])
        
            Profile(
                employ_code=df.iloc[i,1] if str(df.iloc[i,1])!='nan' else -1,
                name =df.iloc[i,2] if str(df.iloc[i,2])!='nan' else -1,
                pay_scale =df.iloc[i,3] if str(df.iloc[i,3])!='nan' else -1,
                designation = df.iloc[i,4] if str(df.iloc[i,4])!='nan' else -1,
                no_of_days =df.iloc[i,5] if str(df.iloc[i,5])!='nan' else -1,
                month =month_list.index(month.lower())+1,
                year=year,
                basic_pay=df.iloc[i,6] if str(df.iloc[i,6])!='nan' else -1,
                da_34=df.iloc[i,7] if str(df.iloc[i,7])!='nan' else -1,
                Npa=df.iloc[i,8] if str(df.iloc[i,8])!='nan' else -1,
                da_203=df.iloc[i,9] if str(df.iloc[i,9])!='nan' else -1,
                aca=df.iloc[i,10] if str(df.iloc[i,10])!='nan' else -1,
                hra=df.iloc[i,11] if str(df.iloc[i,11])!='nan' else -1,
                mta=df.iloc[i,12] if str(df.iloc[i,12])!='nan' else -1,
                nps_14=df.iloc[i,13] if str(df.iloc[i,13])!='nan' else -1,
                adj_amt_1=df.iloc[i,14] if str(df.iloc[i,14])!='nan' else -1,
                gross_salary =df.iloc[i,15] if str(df.iloc[i,15])!='nan' else -1,
                total_deduction=df.iloc[i,16] if str(df.iloc[i,16])!='nan' else -1,
                net_payable=df.iloc[i,17] if str(df.iloc[i,17])!='nan' else -1,
                n_p_s_10 =df.iloc[i,18] if str(df.iloc[i,18])!='nan' else -1,
                n_p_s_14 =df.iloc[i,19] if str(df.iloc[i,19])!='nan' else -1,
                n_p_s =df.iloc[i,20] if str(df.iloc[i,20])!='nan' else -1,
                IT =df.iloc[i,21] if str(df.iloc[i,21])!='nan' else -1,
                PT =df.iloc[i,22] if str(df.iloc[i,22])!='nan' else -1,
                HR =df.iloc[i,23] if str(df.iloc[i,23])!='nan' else -1,
                HR_rec =df.iloc[i,24] if str(df.iloc[i,24])!='nan' else -1,
                adj_amt_2=df.iloc[i,25] if str(df.iloc[i,25])!='nan' else -1,
                other=df.iloc[i,26] if str(df.iloc[i,26])!='nan' else -1,
                net_deduction=df.iloc[i,27] if str(df.iloc[i,27])!='nan' else -1,
                        ).save()
    print(upload)
    return redirect('dashboard_admin')
    # return render(request, 'core/dashboard_admin.html',{'files':file})

@login_required(login_url='login')
def dashboard_admin1(request,pk):
    if not request.user.is_staff:
        return redirect('home')
    file=Files.objects.get(id=pk)
    mon=month_list.index(file.month)+1
    year=file.year
    profile=Profile.objects.filter(month=mon,year=year)
    return render(request, 'core/dashboard_admin1.html',{'profiles':profile})

@login_required(login_url='login')
def file_home(request):
    if not request.user.is_staff:
        return redirect('home')
    return render(request, 'core/file_home.html')

@login_required(login_url='login')
def home(request):
    year=Profile.objects.filter(employ_code=request.user.username).values_list('year', flat=True)
    
    if request.method == "POST":
        year = request.POST["year"]

        month = request.POST.getlist("chk[]")
        month=','.join(month)

        # try:
        #     user = User.object.get(username=username)
        # except:
        #     print('username Does Not Exist !!')

        # user = authenticate(request, username=username, password=password)

        # if user is not None:
        #     login(request, user)
        #     return redirect(request.GET['next'] if 'next' in request.GET else 'home')
        # else:
        #     messages.error(request,'User Name or password is incorrect').
        temp=year+'-'+month
        # print(year+'-'+month)
        return redirect('print_slip',pk=temp)
        
        # return redirect('login')
    

    context={'years':list(set(year))}
    return render(request, 'core/home.html', context)

def forget_password(request):
    if request.user.is_authenticated:
        return redirect('home')
    context={}
    return render(request, 'core/home.html', context)

@login_required(login_url='login')
def logoutUser(req):
    logout(req)
    # messages.info(req, 'user Was logged out')
    return redirect('login')

@login_required(login_url='login')
def load_month(request):
    year_id=request.GET.get('year_id')
    month=Profile.objects.filter(employ_code=request.user.username,year=year_id).values_list('month', flat=True).order_by('month')
    temp=[]
    for i in month:
        temp.append(month_list[i-1])
    print(temp)
    context={'months':temp}
    return render(request, 'core/month_dropdown.html', context)

def render_to_pdf(temp_src,context):
    temp = get_template(temp_src)
    html = temp.render(context)
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    

@login_required(login_url='login')
def print_slip(request,pk):
    dat = date.today()
    mon=[]
    year,month=pk.split('-')
    
    # print('nishank1',month)
    for i in(month.lower().split(',')):
        mon.append(month_list.index(i)+1)
    # month=month_list.index(month.split(',')[0])+1
    # print('nishank',month)
    temp=[]
    try:
        for i in mon:
            profile = Profile.objects.filter(employ_code=request.user.username,month=i)[0]
            temp.append(profile)

    except:
        return HttpResponse("505 Not found")
    # context={
    #     'name':profile.name,
    # 'employ_code':profile.employ_code,
    # 'designation':profile.designation, 
    # 'month':profile.month, 
    # 'year':profile.year,
    # 'basic_pay':profile.basic_pay,
    # 'grade_pay':profile.grade_pay,
    # 'd_a':profile.d_a,
    # 'house_rent':profile.house_rent,
    # 'washing_allowance':profile.washing_allowance, 
    # 'conveyance_allowance':profile.conveyance_allowance, 
    # 'gross_salary':profile.gross_salary, 
    # 'n_p_s':profile.n_p_s, 
    # 'g_i_s':profile.g_i_s, 
    # 'l_i_c':profile.l_i_c, 
    # 'house_rent_d':profile.house_rent_d,
    # 'income_tax':profile.income_tax,
    # 'professional_tax':profile.professional_tax,
    # 'total_deduction':profile.total_deduction,
    # 'net_payable':profile.net_payable,
    # }
    p=inflect.engine()
    word=p.number_to_words(profile.net_payable)
    context={'profiles':temp,'month':mon,'date':dat,'word':word.upper()}
    # return render(request,'core/download.html',context)
    pdf = render_to_pdf('core/download.html',context)
    return HttpResponse(pdf,content_type='application/pdf')
    
    # return redirect('home')

@login_required(login_url='login')
def edit_entry(request,pk):
    if not request.user.is_staff:
        return redirect('home')
       
    profile=Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)
    print(profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('dashboard_admin')
    return render(request, 'core/edit_entry.html',{'form':form})

@login_required(login_url='login')
def home_admin(request):
    if not request.user.is_staff:
        return redirect('home')
       
    
    if request.method == 'POST' and request.FILES['input_file']:
        month=request.POST.get('month')
        year=request.POST.get('year')
        file=request.FILES.getlist('input_file')
        if Files.objects.filter(month=month,year=year):
            messages.info(request,'File already exist')
            return render(request, 'core/home_admin.html', {})
        else:

            for f in file:
                Files(month=month,year=year,upload=f).save()
        
        print(month,year,file)

        return redirect('dashboard_admin')
    context={}
    return render(request, 'core/home_admin.html', context)
