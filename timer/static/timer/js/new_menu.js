function Active(){
    target = document.getElementById("menu_make");
    target.style.backgroundColor="#CCFFFF"
  }
Active();

/*
const save_button=document.getElementById('save');

save_button.addEventListener('click',(e)=>{
    e.preventDefault();
    var flag=SaveSend()
    if(flag==1){
        alert("計測時間が00:00:00であるタイマーがあります");
      }else if(flag==2){
        alert("分、秒に指定できるのは０以上５９以下の数字のみです");
      }else{
        document.timerset.submit()
      }
});
*/

function SaveSend(){
  var qua=document.getElementById("number").innerHTML;
  Number(qua);
  var flag=0;
  for(let i=0; i < qua ; i++){
    j=Number(i)
    //alert("計測時間が00:00:00であるタイマーがあります");
    var hour=String(setfig(Math.floor(document.forms[1].elements[h+cir*j].value)));
    var min=String(setfig(Math.floor(document.forms[1].elements[m+cir*j].value)));
    var sec=String(setfig(Math.floor(document.forms[1].elements[s+cir*j].value)));
    
    if(hour=="00"){
      document.forms[1].elements[h+cir*j].value="00";
    }
    if(min=="00"){
      document.forms[1].elements[m+cir*j].value="00";
    }
    if(sec=="00"){
      document.forms[1].elements[s+cir*j].value="00";
    }
    if( (hour=="00") && (min=="00") && (sec=="00") )
    {
      flag=1;
    }
    var nummin=Number(min);
    var numsec=Number(sec);
    if(flag==0&(nummin>59||numsec>59)){
      flag=2;
    }
  }
  return flag;

  
}