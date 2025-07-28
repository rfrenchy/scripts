import { initWebGL } from './renderer'

const canvas = document.getElementById('glcanvas') as HTMLCanvasElement;
const gl = canvas.getContext('webgl');

const x = fetch("http://localhost:3000/data");

console.log(x);

x.then(response => {
	console.log(response);
})

if (gl) {
	initWebGL(gl);
} else {
	console.error("unable to create glcanvas");
}
