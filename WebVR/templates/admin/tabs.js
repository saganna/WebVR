$(#titlelink).addEventlistener("click", fuction(){
  var i, tabcontent, tablinks;

  tabcontent = $(".tabcontent");
  for(i=0;i<tabcontent.length;i++){
    tabcontent[i].style.display = "none";
  }

  tablinks = $(".tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  document.getElementById("title").style.display = "block";
  document.getElementById("titlelink").className+=" active";

})
$(#contentlink).addEventlistener("click", fuction(){
  var i, tabcontent, tablinks;

  tabcontent = $(".tabcontent");
  for(i=0;i<tabcontent.length;i++){
    tabcontent[i].style.display = "none";
  }

  tablinks = $(".tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  document.getElementById("content").style.display = "block";
  document.getElementById("contentlink").className+=" active";

})
