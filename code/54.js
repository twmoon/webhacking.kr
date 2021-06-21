
function run(){
  if(window.ActiveXObject){
   try {
    return new ActiveXObject('Msxml2.XMLHTTP');
   } catch (e) {
    try {
     return new ActiveXObject('Microsoft.XMLHTTP');
    } catch (e) {
     return null;
    }
   }
  }else if(window.XMLHttpRequest){
   return new XMLHttpRequest();
 
  }else{
   return null;
  }
 }
x=run();
function answer(i){
  x.open('GET','?m='+i,false);
  x.send(null);
  aview.innerHTML+=x.responseText; // + 추가로 사라지지않고 저장
  i++;
  if(x.responseText) setTimeout("answer("+i+")",20);
  //if(x.responseText=="") aview.innerHTML="?";  //이 친구가 있으면 플래그가 다 끝나고 ?로 초기화 그래서 지움
}
setTimeout("answer(0)",1000);
