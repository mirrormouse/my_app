from django.shortcuts import render
from django.http import HttpResponse
from tensorflow.keras.models import load_model
# Create your views here.
model = load_model("AIapp/model/my_model.h5")

def makedata(l):
  res=[]
  for num in l:
    data=[0]
    val=num
    for i in range(5):
      data.append(val%10)
      val=val//10
    res.append(data)
  return res


def calc(x,y):
    partx=makedata([x])
    party=makedata([y])
    train=np.array(bound(partx,party))
    ans=x+y
    z=makedata(ans)
    label=np.array(z)
    train=train.transpose(0, 2, 1)
    result=model.predict(train)
    result=result.flatten().astype(np.uint8)
    res=""
    flag=False
    for i in range(5):
        if (not flag) and (result[5-i]!=0):
            flag=True
        if flag:
            res+=str(result[5-i])
    print(res)


def index(request):
    msg=calc(3,3)
    return HttpResponse(msg)