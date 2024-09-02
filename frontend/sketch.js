function preload() {
}

function setup() {
  createCanvas(windowWidth, windowHeight);
  textFont("Merriweather")
  textSize(22)
}

function heart(x) {
  let a = frameCount * 0.001;

  let root3_of_square = pow(x * x, 1 / 3)
  let sine_term = sin(a * 2 * PI * x)
  let scaling = sqrt(125 - x * x) * 0.75;

  return -(root3_of_square + sine_term * scaling);
}

function draw() {
  colorMode(HSB, 360, 100, 100, 100);
  background(0, 4);
  stroke(255);
  translate(width / 2 - 16 / 9 * 120, height / 2);
  scale(15);
  noStroke()
  fill(270, 75, 100, 100);
  text("I", -16 / 9 * 12, 16 / 9 * 4)
  text("K8s", 16 / 9 * 7, 16 / 9 * 4)
  let oldX = -12;
  let oldY = heart(oldX);
  strokeWeight(0.05);
  stroke(270, 75, 100, 100);
  for (let x = -12.01; x <= 12; x += 0.1) {
    let y = heart(x);
    line(oldX, oldY, x, y);
    oldX = x;
    oldY = y;
  }
}
