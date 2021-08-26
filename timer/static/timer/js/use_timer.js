setfig=function(num) {
    // 桁数が1桁だったら先頭に0を加えて2桁に調整する
    var result;
    if(num==0){
      result="00";
    }else if( num < 10 && String(num).length==1) {
      result = "0" + num; 
    }else {
      result = num; 
    }
    return result;
  }
  
  function Repeat(){
    var blank=document.getElementById("centering").value;
    var num=60;
    var sum="";
    for(let i=0;i<num;i++){
      sum+=blank;
    }
    document.getElementById("centering").innerHTML=sum;
  }
  
  
  function repeatText(){
  
  }
  
  const titles=1;
  const sets=2;

  document.forms[titles].elements[1].disabled=true;
  document.forms[titles].elements[2].disabled=true;
  document.forms[titles].elements[3].disabled=true;
  document.forms[titles].elements[4].disabled=true;
  document.forms[titles].elements[5].disabled=true;
  var timer1; //タイマーを格納する変数（タイマーID）の宣言
  //カウントダウン関数を1000ミリ秒毎に呼び出す関数
  var blank="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;";
  const ti=2;
  const h=ti+1;
  const m=h+1;
  const s=m+1;
  const so=s+1;
  const n=so+1;
  const p=n+1;
  const ch=p+1;
  const cir=7;
  UpdateChange(0);
  TitleUpdate();
  const start_sound=document.getElementById("start_sound");
  const stop_sound=document.getElementById("stop_sound");
  const mute_sound=document.getElementById("mute_sound");
  Volume();
  
  function UpdateChange(present){
    document.forms[sets].elements[ti+cir*present].addEventListener('change', Change);
    document.forms[sets].elements[h+cir*present].addEventListener('change', Change);
    document.forms[sets].elements[m+cir*present].addEventListener('change', Change);
    document.forms[sets].elements[s+cir*present].addEventListener('change', Change);
  }
  function RemoveChange(present){
    document.forms[sets].elements[ti+cir*present].removeEventListener('change', Change);
    document.forms[sets].elements[h+cir*present].removeEventListener('change', Change);
    document.forms[sets].elements[m+cir*present].removeEventListener('change', Change);
    document.forms[sets].elements[s+cir*present].removeEventListener('change', Change);
  }
  
  document.forms[sets].elements[ti].addEventListener('change', TitleUpdate);
  document.forms[sets].elements[h].addEventListener('change', TitleUpdate);
  document.forms[sets].elements[m].addEventListener('change', TitleUpdate);
  document.forms[sets].elements[s].addEventListener('change', TitleUpdate);
  
  function TitleUpdate(){
    var sethour=document.forms[sets].elements[h].value;
    var setmin=document.forms[sets].elements[m].value;
    var setsec=document.forms[sets].elements[s].value;
    var settitle=document.forms[sets].elements[ti].value;
    document.getElementById("sethour").innerHTML=sethour;
    document.getElementById("setmin").innerHTML=setmin;
    document.getElementById("setsec").innerHTML=setsec;
    document.getElementById("settitle").innerHTML=settitle;
    var msg = setfig(sethour)+":"+setfig(setmin) + ":" + setfig(setsec);
    document.getElementById("Timer").innerHTML = settitle+blank+msg;
  }
  
  var all=document.getElementById("number").innerHTML;
  all=Number(all)
  for(let i=0;i<p+cir*(all-1)+1;i++){
    document.forms[sets].elements[i].addEventListener('keydown', function (event) {
      if (event.keyCode === 13) {
        // エンターキーが押されたときの動作
          // submitボタン以外の場合はイベントをキャンセル
          return false;
        
      }
    });
  }
  
  
  var recent_change=true;
  function Change()
  {
    recent_change=true;
  }
  
  document.getElementById("volume").addEventListener('change', Volume);
  document.getElementById("volume").addEventListener('input', Volume);
  
  function Volume(){
    var vol=Number(document.getElementById("volume").value);
    start_sound.volume=vol;
    stop_sound.volume=vol;
  }
  
  function Mute(){
    document.getElementById("volume").value="0";
    Volume();
  }
  function ResetSound(){
    mute_sound.pause();
    mute_sound.currentTime=0;
    start_sound.pause();
    start_sound.currentTime=0;
    stop_sound.pause();
    stop_sound.currentTime=0;
  }
  function Stop_Sound_Test(){
    mute_sound.play();
    stop_sound.load();
    start_sound.load();
    ResetSound();
    stop_sound.play();
    Confirm_Sound();
  }
  function Start_Sound_Test(){
    mute_sound.play();
    start_sound.load();
    stop_sound.load();
    ResetSound();
    start_sound.play();
    Confirm_Sound();
  }
  function Confirm_Sound(){
    var vol=Number(document.getElementById("volume").value);
    if(vol==0){
      alert("音声がミュートされています");
    }
  }
  
  function Start()
  {
    mute_sound.play();
    ResetSound();
    start_sound.load();
    stop_sound.load();
  
    document.getElementById("reset").disabled = true;
    document.getElementById("allreset").disabled = true;
    var cur=document.getElementById("current").innerHTML;
    var qua=document.getElementById("number").innerHTML;
    qua=Number(qua);
  
    var flag=0;
  
    document.getElementById("start").disabled = true;
    
    for(let i=0; i < qua ; i++){
      j=Number(i)
      //alert("計測時間が00:00:00であるタイマーがあります");
      var hour=setfig(Math.floor(document.forms[sets].elements[h+cir*j].value));
      var min=setfig(Math.floor(document.forms[sets].elements[m+cir*j].value));
      var sec=setfig(Math.floor(document.forms[sets].elements[s+cir*j].value));
      
      if(hour=="00"){
        document.forms[sets].elements[h+cir*j].value="00";
      }
      if(min=="00"){
        document.forms[sets].elements[m+cir*j].value="00";
      }
      if(sec=="00"){
        document.forms[sets].elements[s+cir*j].value="00";
      }
      if( (hour=="00") && (min=="00") && (sec=="00") )
      {
        flag=1;
      }
      var nummin=Number(min);
      var numsec=Number(sec);
      if(nummin>59||numsec>59){
        //flag=2;
      }
      
      
    }
    
    if(flag==1){
      alert("計測時間が00:00:00または未設定であるタイマーがあります");
      document.getElementById("start").disabled=false;
    }else{
      for(let i=0;i<qua;i++){
        j=Number(i);
      }
      TimerStart(cur,qua);
    }
    
  }
  
  
  function TimerStart(i,qua)
  {
    UpdateChange(Number(i));
    
    var idname="point_"+String(Number(i)+1);
    document.getElementById(idname).style.color="skyblue";
    var sethour,setmin,setsec;
    if(recent_change){
      sethour=Math.floor(document.forms[sets].elements[h+cir*i].value);
      setmin=Math.floor(document.forms[sets].elements[m+cir*i].value);
      setsec=Math.floor(document.forms[sets].elements[s+cir*i].value);
      document.getElementById("sethour").innerHTML=sethour;
      document.getElementById("setmin").innerHTML=setmin;
      document.getElementById("setsec").innerHTML=setsec;
    }
    sethour=document.getElementById("sethour").innerHTML;
    setmin=document.getElementById("setmin").innerHTML;
    setsec=document.getElementById("setsec").innerHTML;
    recent_change=false;
    var msg = setfig(sethour)+":"+setfig(setmin) + ":" + setfig(setsec);
    var settitle=document.forms[sets].elements[ti+cir*i].value;
    document.getElementById("settitle").innerHTML=settitle;
    document.getElementById("Timer").innerHTML = settitle+blank+msg;
    timer1=setInterval(function(){countDown(i,qua)},1000);
  }
  
  //タイマー停止関数
  function Stop()
  {
    document.getElementById("reset").disabled = false;
    document.getElementById("allreset").disabled = false;
    document.getElementById("start").disabled=false;
    clearInterval(timer1);
  }
  
  //カウントダウン関数
  
  function countDown(i,qua)
  {
    var hour=document.getElementById("sethour").innerHTML;
    var min=document.getElementById("setmin").innerHTML;
    var sec=document.getElementById("setsec").innerHTML;
    var all=(Number(hour)*3600)+(Number(min)*60)+Number(sec);
    Update_Char(all);
    timeUpdate(i,qua,all-1);
  }
  
  
  
  //残り時間を書き出す関数
  function timeUpdate(i,qua,num)
  {
    num=parseInt(num);
    
    if (num<=0)
    {      
       
      clearInterval(timer1);
      numberReset();
      Update_Char(num);
      var cur=document.getElementById("current").innerHTML;
      cur=Number(cur);
      chart.data.datasets[0].data = [1,0];
      chart.update();
      RemoveChange(cur);
      document.getElementById("start").disabled=false;
      var flag=Number(document.forms[sets].elements[so+cir*cur].value);
      
      Volume();
      
      if(flag==0){
        ResetSound();
        stop_sound.play();
      }else if(flag==1){
        ResetSound();
        start_sound.play();
      }
      
      if(qua>cur+1){
        var idname="point_"+String(cur+1);
        document.getElementById(idname).style.color="black";
        recent_change=true;
        var next=Number(cur)+1;
        
        document.getElementById("current").innerHTML=next;
        TimerStart(next,qua);
      }else{
        document.getElementById("current").innerHTML="0";
        
        document.getElementById("reset").disabled = false;
        document.getElementById("allreset").disabled = false;
        var settitle=document.getElementById("settitle").innerHTML;
        var msg = "00:00:00";
        document.getElementById("Timer").innerHTML = settitle+blank+msg;

        
        UpdateChange(0);
        Reset();
        Reset_Char();
        //alert("全てのタイマーが終了しました");
  
      }
    }
    else
    {
      var rem=num%3600;
      var nowhour=setfig(Math.floor(num/3600));
      var nowmin=setfig(Math.floor(rem/60));
      var nowsec=setfig(rem % 60);
      Update_Char(num);
      //console.log(util.add(1,1));
      document.getElementById("sethour").innerHTML=setfig(Math.floor(num/3600));
      document.getElementById("setmin").innerHTML=setfig(Math.floor(rem/60));
      document.getElementById("setsec").innerHTML=setfig(rem % 60);
      var settitle=document.getElementById("settitle").innerHTML;
      var msg = nowhour+":"+nowmin + ":" + nowsec;
      document.getElementById("Timer").innerHTML = settitle+blank+msg;
    }
  }
  
  //フォームを初期状態に戻す（リセット）関数
  function allReset()
  {
    var cur=document.getElementById("current").innerHTML;
    RemoveChange(cur)
    cur=Number(cur);
    var idname="point_"+String(cur+1);
    document.getElementById(idname).style.color="black";
    document.getElementById("current").innerHTML=0;
    Reset();
    UpdateChange(0);
  }
  
  function Reset()
  {
    var cur=document.getElementById("current").innerHTML;
    if (cur==0){
      var qua=document.getElementById("number").innerHTML;
      Number(qua);
      for(let i=0;i<qua;i++){
        j=Number(i);
      }
    }
    Reset_Char();
    numberReset();
  }
  
  function numberReset(){
    
    recent_change=true;
    var cur=document.getElementById("current").innerHTML;
    var sethour=document.forms[sets].elements[h+cir*cur].value;
    var setmin=document.forms[sets].elements[m+cir*cur].value;
    var setsec=document.forms[sets].elements[s+cir*cur].value;
    var settitle=document.forms[sets].elements[ti+cir*cur].value;
    document.getElementById("sethour").innerHTML=sethour;
    document.getElementById("setmin").innerHTML=setmin;
    document.getElementById("setsec").innerHTML=setsec;
    document.getElementById("settitle").innerHTML=settitle;
    cur=Number(cur);
    var msg = setfig(sethour)+":"+setfig(setmin) + ":" + setfig(setsec);
    document.getElementById("Timer").innerHTML = settitle+blank+msg;
  }
  
  function Update_Char(num){
    cur=Number(document.getElementById("current").innerHTML);
    var sethour=Number(document.forms[sets].elements[h+cir*cur].value);
    var setmin=Number(document.forms[sets].elements[m+cir*cur].value);
    var setsec=Number(document.forms[sets].elements[s+cir*cur].value);
    var all=3600*sethour+60*setmin+setsec;
    document.getElementById("test").innerHTML = String(all);
    num=Number(num);
    chart.data.datasets[0].data = [all-num,num];
    chart.update();
  }
  function Reset_Char(){
    chart.data.datasets[0].data = [0,1];
    chart.update();
  }
  
  function Login_home(){
    location.href = "../../timer/";
  }
  
  function Logout(){
    location.href = "../timer/logout";
  }
  
  function Clear()
  {
    if(window.confirm('このページに入力している値はすべて削除されます。よろしいですか？')){
        location.href = "../timer";
      }
  }
  
  function Clear_home()
  {
    if(window.confirm('このページに入力している値はすべて削除されます。よろしいですか？')){
      location.href = "../timer/main";
    }
  }  


  var ctx = document.getElementById("PieChart");
    var chart = new Chart(ctx, {
      type: 'pie',
      data: {
        datasets: [{
            backgroundColor: [
                "#7777FF",
                "#DDDDDD",
            ],
            data: [0, 1]
        }]
      },
      options: {
        animation: false
      }
    });
  
  