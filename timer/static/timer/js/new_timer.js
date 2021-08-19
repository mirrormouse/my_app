setfig=function(num) {
    // 桁数が1桁だったら先頭に0を加えて2桁に調整する
    var result;
    if(num==0){
      result="00";
    }else if( num < 10 ) {
      result = "0" + num; 
    }else {
      result = num; 
    }
    return result;
  }
  document.forms[0].elements[0].disabled=true;
  document.forms[0].elements[1].disabled=true;
  document.forms[0].elements[2].disabled=true;
  document.forms[0].elements[3].disabled=true;
  
  
  var timer1; //タイマーを格納する変数（タイマーID）の宣言
  //カウントダウン関数を1000ミリ秒毎に呼び出す関数
  

  
  function Start()
  {
    var qua=document.getElementById("number").innerHTML;
    Number(qua);

    var flag=0;

    document.getElementById("start").disabled = true;
    
    for(let i=0; i < qua ; i++){
      j=Number(i)
      //alert("計測時間が00:00:00であるタイマーがあります");
      var hour=setfig(Math.floor(document.forms[1].elements[2+8*j].value));
      var min=setfig(Math.floor(document.forms[1].elements[3+8*j].value));
      var sec=setfig(Math.floor(document.forms[1].elements[4+8*j].value));
      
      if(hour=="00"){
        document.forms[1].elements[2+8*j].value="00";
      }
      if(min=="00"){
        document.forms[1].elements[3+8*j].value="00";
      }
      if(sec=="00"){
        document.forms[1].elements[4+8*j].value="00";
      }
      if( (hour=="00") && (min=="00") && (sec=="00") )
      {
        flag=1;
      }
      
      
    }
    
    if(flag==1){
      alert("計測時間が00:00:00または未設定であるタイマーがあります");
      document.getElementById("start").disabled=false;
    }else{
      TimerStart(0,qua);
    }
    
    
  }

  function TimerStart(i,qua)
  {
    var sethour=Math.floor(document.forms[1].elements[2+8*i].value);
    var setmin=Math.floor(document.forms[1].elements[3+8*i].value);
    var setsec=Math.floor(document.forms[1].elements[4+8*i].value);
    var msg = setfig(sethour)+":"+setfig(setmin) + ":" + setfig(setsec);
    document.getElementById("Timer").innerHTML = msg;
    timer1=setInterval(function(){countDown(i,qua,sethour,setmin,setsec)},1000);
  }
  
  //タイマー停止関数
  function Stop()
  {
    document.getElementById("start").disabled=false;
    clearInterval(timer1);
  }
  
  //カウントダウン関数
  
  function countDown(i,qua,sethour,setmin,setsec)
  {
    var hour=document.forms[1].elements[2+8*i].value;
    var min=document.forms[1].elements[3+8*i].value;
    var sec=document.forms[1].elements[4+8*i].value;
    timeUpdate(i,qua,hour*60+min*60+sec-1,sethour,setmin,setsec);

  }
  
  //残り時間を書き出す関数
  function timeUpdate(i,qua,num,sethour,setmin,setsec)
  {
    num=parseInt(num);
    
    if (num<=0)
    {
      document.getElementById("Timer").innerHTML = "00:00:00";
      //alert("時間です！");
      clearInterval(timer1);
      document.forms[1].elements[2+8*i].value=setfig(sethour);
      document.forms[1].elements[3+8*i].value=setfig(setmin);
      document.forms[1].elements[4+8*i].value=setfig(setsec);
      
      if(qua>i+1){
        TimerStart(i+1,qua);
      }
    }
    else
    {
      var nowhour=setfig(Math.floor(num/60));
      var nowmin=setfig(Math.floor(num/60));
      var nowsec=setfig(num % 60);
      //console.log(util.add(1,1));
      document.forms[1].elements[2+8*i].value=setfig(Math.floor(num/3600));
      var rem=num%3600;
      document.forms[1].elements[3+8*i].value=setfig(Math.floor(rem/60));
      document.forms[1].elements[4+8*i].value=setfig(rem % 60);
      var msg = nowhour+":"+nowmin + ":" + nowsec;
      document.getElementById("Timer").innerHTML = msg;
    }
  }
  
  //フォームを初期状態に戻す（リセット）関数
  function reSet()
  {

  }  
  
  function add()
  {
    
  }  
  
  