
function ck(){
  var ul=document.URL;                                                      //ul = 'https://webhacking.kr/challenge/js-1/'
  ul=ul.indexOf(".kr");                                                     //u1 = 18
  ul=ul*30;                                                                 //u1 = 540
  if(ul==pw.input_pwd.value) { location.href="?"+ul*pw.input_pwd.value; }   //input_pwd.value = u1 = 540
  else { alert("Wrong"); }
}
