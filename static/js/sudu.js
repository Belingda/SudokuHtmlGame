var suduLst=[]
function initView(){
  getSuduData()
}
function sendRecord(){
    var request=new XMLHttpRequest();
   request.onreadystatechange = function () {
    if (request.readyState === 4) {
        if (request.status === 200) {
             console.log("添加记录成功")
        } else {
            console.log("服务器错误,添加记录失败："+request.status)
        }
    } else {
        //在此添加请求进度条
    }
}
request.open('GET', '/recordJoin');
request.send();
}
function getSuduData(){
   var request=new XMLHttpRequest();
   request.onreadystatechange = function () {
    if (request.readyState === 4) {
        if (request.status === 200) {
             console.log(request.responseText)
             if(request.responseText.length<81){
                 alert("请稍后重试")
                 return
             }
             suduLst=eval(request.responseText)
             addInputNumTag('rect',suduLst)
        } else {
             alert("服务器错误："+request.status)
        }
    } else {
        //在此添加请求进度条
    }
}
request.open('GET', '/getSuduRect');
request.send();

}
var suduLen=81;

var pointDefaultLst=[10,11,12 , 13 , 16 , 19 , 20 , 21 , 22 , 25 , 34 ,  43 , 45 , 46 , 49 , 50 , 52 , 54 , 55 , 58 , 59 , 61 , 63 , 64 , 67 , 68 , 70]
function addInputNumTag(parentId,suduLst){
    var parent = document.getElementById(parentId);

    for(var i=0;i<81;i++){　
     var input = document.createElement("input"); 　　　　
     input.setAttribute("type", "number");
     input.setAttribute("min",0);
     input.setAttribute("max",9);
     input.setAttribute("oninput","if(value.length>1)value=value.slice(0,1)");//限制只能输入一位
     input.setAttribute("id", i);
     if(pointDefaultLst.indexOf(i)<0){
      input.setAttribute("readonly","readonly");
      input.setAttribute("value",suduLst[i]);
      input.setAttribute("class", "block");
     }else{
      input.setAttribute("class", "inputBlank");
     }
     parent.appendChild(input);
     if ((i+1)%9==0){
      var br = document.createElement("br");
      parent.appendChild(br);
      }
    }
}
function  finish(){
     success=true;
     for(var i=0;i<suduLen;i++){
          var num=document.getElementById(i).value;
          if(num!=suduLst[i]){
             alert("挑战失败啦")
             success=false;
             break;
          }
     }
     if(success){
          alert("挑战成功")
          getSuccessSurprise()
     }else{
         sendRecord()
     }
}
function getSuccessSurprise(){
       sendRecord()
       document.getElementById('fastFinishBtn').style.display="none";
       document.getElementById('finishBtn').style.display="none";

       for(var i=0;i<suduLen;i++){
           document.getElementById(i).value=suduLst[i];
     }
       window.setTimeout("changeBlockColor()", 1000);

}
function changeBlockColor(){
         for(var i=0;i<suduLen;i++){
       if(pointDefaultLst.indexOf(i)<0){
         document.getElementById(i).className='pink';
       }else{
          document.getElementById(i).className='black';
       }
          if((i+1)%3==0){
             document.getElementById(i).className+=' border';
          }

     }
}
