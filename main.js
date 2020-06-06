var timer = document.getElementById('timer');
var toggleBtn = document.getElementById('toggle');
var resetBtn = document.getElementById('reset');
var watch = new Stopwatch(timer);


var beeeep = new Audio();
var state = 'LEFT'
var timer = 0
function start(num){
  if ((Math.random() > 0.5)) {
    state = 'RIGHT'
    beeeep.src = 'Right_decay.wav';
  } else {
    state = 'LEFT'
    beeeep.src = 'Left_decay.wav';
  }
  watch.reset();
  beeeep.play();
  watch.start();
}

function left(){
  watch.stop();
  if (state == 'LEFT') {
    div1.innerHTML = "CORRECT";
  } else {
    div1.innerHTML = "WRONG";
  }
}

function right(){
  watch.stop();
  if (state == 'RIGHT') {
    div1.innerHTML = "CORRECT";
  } else {
    div1.innerHTML = "WRONG";
  }
}
