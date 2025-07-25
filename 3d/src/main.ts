import { initWebGL } from './renderer'

const canvas = document.getElementById('glcanvas') as HTMLCanvasElement;
const gl = canvas.getContent('webgl');

if (gl) {
	initWebGL(gl);
} else {
	console.error("unable to create glcanvas");
}
