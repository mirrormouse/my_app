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

  var init = (function (){
    var min=0;
    var sec=0;
    var msg = min + ":" + sec;
    document.getElementById("Timer").innerHTML = msg;
  });

  var timer1; //タイマーを格納する変数（タイマーID）の宣言
  //カウントダウン関数を1000ミリ秒毎に呼び出す関数
 
  function cntStart()
  {
    document.timer.elements[2].disabled=true;
    timer1=setInterval("countDown()",1000);
  }

  //タイマー停止関数
  function cntStop()
  {
    document.timer.elements[2].disabled=false;
    clearInterval(timer1);
  }

  //カウントダウン関数
  function countDown()
  {
    var min=document.timer.elements[0].value;
    var sec=document.timer.elements[1].value;
    
    if( (min=="") && (sec=="") )
    {
      alert("時刻を設定してください！");
      reSet();
    }
    else
    {
      if (min=="") min=0;
      min=parseInt(min);
      
      if (sec=="") sec=0;
      sec=parseInt(sec);
      
      tmWrite(min*60+sec-1);
    }
  }

  //残り時間を書き出す関数
  function tmWrite(num)
  {
    num=parseInt(num);
    
    if (num<=0)
    {
      reSet();
      alert("時間です！");
    }
    else
    {
      var nowmin=setfig(Math.floor(num/60));
      var nowsec=setfig(num % 60);
      //console.log(util.add(1,1));
      document.timer.elements[0].value=Math.floor(num/60);
      document.timer.elements[1].value=num % 60;
      var msg = nowmin + ":" + nowsec;
      document.getElementById("Timer").innerHTML = msg;
    }
  }

  //フォームを初期状態に戻す（リセット）関数
  function reSet()
  {
    document.timer.elements[0].value="0";
    document.timer.elements[1].value="0";
    document.timer.elements[2].disabled=false;
    clearInterval(timer1);
  }  

  function add()
  {
    
  }  

