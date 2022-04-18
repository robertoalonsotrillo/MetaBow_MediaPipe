var Data=0;
document.getElementsByClassName("input-form")[0].onsubmit = function() {everyTime()};

function updateRecVal() {
  var model=document.getElementById("model-input").innerHTML
  var videoInputType=document.getElementById("video-input").innerHTML
  if(videoInputType=="" || model==""){
    // console.log("null")
    videoInputType="file-input"
    model="first"
  }
  var temp=Data
  document.getElementById("resultLine").innerHTML="Results of "+model.toUpperCase()+" Model";
  
  // var rowsC3=document.getElementsByClassName("c3")
  var rowsC2=document.getElementsByClassName("c2")
  var rows=document.getElementsByClassName("row")
  // var rowsC4=document.getElementsByClassName("c4")
  if(model=="first" && rows[4].style.display!="none"){
    for (let  i = 4;  i < 11;  i++)
    {
      rows[i].style.display="none"
    }
  }
  else if(model=="second" && rows[4].style.display=="none")
  {
    for (let  i = 4;  i < 11;  i++)
    {
      rows[i].style.display="block"
    }
  }


  keys=Object.keys(temp)
  if(model=="first"){
    var lenn=4
  }
  else{
    var lenn=11
  }
  for (let  i = 0;  i < lenn;  i++) {
    var value=temp[keys[i]].angle
    
      rowsC2[i].innerHTML=`${value}`
     }
}

function everyTime() {

  fetch("http://localhost:5000/read")
  // fetch("./variables.json")
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    Data=data;
    updateRecVal();
  })
  .catch(function (err) {
    console.log(err);
  });
}

var myInterval = setInterval(everyTime, 1000);