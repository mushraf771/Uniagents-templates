var myVideo = document.getElementById("video1,video2,video3,video4,"); 
function playPause() { 
    if (myVideo.paused) 
      myVideo.play(); 
     
    else 
      myVideo.pause(); 
  } 
  
if(myVideo == video1) {
    playPause()
}
else if(myVideo==video2){
    playPause()
}
else if(myVideo==video3){
    playPause()
}
else{
    playPause()
}
