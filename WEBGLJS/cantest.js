
window.onload = function () {

    // //顶点着色器程序
    // var VSHADER_SOURCE =
    //     "void main() {" +
    //         //设置坐标
    //     "gl_Position = vec4(0.0, 0.0, 0.0, 1.0); " +
    //         //设置尺寸
    //     "gl_PointSize = 10.0; " +
    //     "} ";

    // //片元着色器
    // var FSHADER_SOURCE =
    //     "void main() {" +
    //         //设置颜色
    //     "gl_FragColor = vec4(1.0, 0.0, 0.0, 1.0);" +
    //     "}";
    // //获取canvas元素
    // var canvas = document.getElementById('canvas');
    // //获取绘制二维上下文
    // var gl = canvas.getContext('webgl');
    // if (!gl) {
    //     console.log("Failed");
    //     return;
    // }
    // //编译着色器
    // var vertShader = gl.createShader(gl.VERTEX_SHADER);
    // gl.shaderSource(vertShader, VSHADER_SOURCE);
    // gl.compileShader(vertShader);

    // var fragShader = gl.createShader(gl.FRAGMENT_SHADER);
    // gl.shaderSource(fragShader, FSHADER_SOURCE);
    // gl.compileShader(fragShader);
    // //合并程序
    // var shaderProgram = gl.createProgram();
    // gl.attachShader(shaderProgram, vertShader);
    // gl.attachShader(shaderProgram, fragShader);
    // gl.linkProgram(shaderProgram);
    // gl.useProgram(shaderProgram);

    // //绘制一个点
    // gl.drawArrays(gl.POINTS, 0, 1);

    // var canvas = document.getElementById('canvas');
    // var ctx = canvas.getContext("2d");
    // ctx.font = '25pt Calibri';
    // ctx.fillStyle = 'green';
    // ctx.fillText("Hello world!", 20, 100);


    var canvas = document.getElementById('canvas');
    var ctx = canvas.getContext("webgl");
    ctx.clearColor(0.9,0.9,0.8,1);
    ctx.clear(ctx.COLOR_BUFFER_BIT);
}