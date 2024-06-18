from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

grade_db = [
  {
    "_id": "4e354683-776b-4584-C827-9d45550f9643",
    "index": "1",
    "teacher": "호리아",
    "phone": "010-3147-7752",
    "grade": "1",
    "num": "3",
    "contants": "별과 잔디가 밤을 바이며 자유를 동력은 위하거나 조직·권한. 우리의 연임할"
  },
  {
    "_id": "047a88a7-3340-4267-C377-e7d4b549296e",
    "index": "2",
    "teacher": "현강현",
    "phone": "010-9407-5329",
    "grade": "2",
    "num": "6",
    "contants": "만물은 너무나 발할 선거권자 정치에 형사상 다 원질이. 임명하고 거친"
  },
  {
    "_id": "dd02dfa8-1ea9-4eae-Aef4-c04ebdc52049",
    "index": "3",
    "teacher": "채태혁",
    "phone": "010-8072-4482",
    "grade": "2",
    "num": "5",
    "contants": "뛰노는 개인과 공포한다 구성하지 내용과 별에도 탄핵의 더운지라. 창달에 어머니"
  },
  {
    "_id": "f59bb2cd-b219-480a-C49c-46ad99da5cd8",
    "index": "4",
    "teacher": "탄연아",
    "phone": "010-9165-2464",
    "grade": "2",
    "num": "1",
    "contants": "두손을 만료되는 자문에 몸이 중요정책을 찬미를 강아지 합리적인. 밝은 이는"
  },
  {
    "_id": "36d71b58-a31b-40a5-B010-ef39e509a7f8",
    "index": "5",
    "teacher": "풍효준",
    "phone": "010-2822-3309",
    "grade": "1",
    "num": "6",
    "contants": "선거에 사항과 국민투표의 찬성으로 힘차게 후가 의결을 대통령·국무총리와. 하나 아니면"
  }
]

def index(request):
    return render(request, 'main/index.html')

def jejuohyun(request):
    return render(request, 'main/jejuohtun.html')

def high_1st(request):
    return render(request, 'main/high_1st.html')

def high_2nd(request):
    return render(request, 'main/high_2nd.html')

def high_3rd(request):
    return render(request, 'main/high_3rd.html')

def my_page(request):
    return render(request, 'main/my_page.html')

def grade(request):
    return render(request, 'main/grade.html')
