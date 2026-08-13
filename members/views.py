from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm 

# 1. 기존에 만들었던 목록 뷰
def member_list(request):
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})

# 2. 🔥 새로 추가할 등록 뷰
def member_create(request):
    if request.method == "POST":
        # 사용자가 데이터를 입력하고 [저장]을 눌렀을 때
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()  # DB에 실시간으로 저장!
            return redirect('member_list')  # 저장 후 목록 화면으로 튕겨주기
    else:
        # 처음에 주소창 치고 들어왔을 때 (빈 입력창 보여주기)
        form = MemberForm()
    
    return render(request, 'members/member_create.html', {'form': form})