let video;
let poseNet;
let poses = [];
let x = 0
let position = 0;
let pose;
let keypoint;

function setup() {
  img = loadImage('https://ichef.bbci.co.uk/news/660/cpsprodpb/37B5/production/_89716241_thinkstockphotos-523060154.jpg');
  imageg = loadImage('https://images.vexels.com/media/users/3/153910/isolated/preview/29ccee0f62eece9599c2b3a50bdbeea2-sombrero-hat-flat-icon-by-vexels.png');
  createCanvas(640, 480);
  video = createCapture(VIDEO);
  video.size(width, height);

  // Create a new poseNet method with a single detection
  poseNet = ml5.poseNet(video);
  // This sets up an event that fills the global variable "poses"
  // with an array every time new poses are detected
  poseNet.on('pose', function(results) {
    poses = results;
  });
  // Hide the video element, and just show the canvas
  video.hide();
}

function modelReady() {
  select('#status').html('Model Loaded');
}

function draw() {
  image(video, 0, 0, width, height);
  image(imageg, position.x-100, position.y-250, 300, 300);
  if(poses.length > 0){
    position = poses[0].pose.keypoints[2].position;
  }
  try {
    image(img, keypoint.position.x, keypoint.position.y, 10, 10);
  } catch(TypeError) {

  }
}
