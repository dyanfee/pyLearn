window.onload = function () {

    var canvas = document.getElementById('canvas');
    var gl = canvas.getContext('webgl');


    var vertices = [
        -0.5, 0.5, 0.0,
        0.0, 0.0, 0.0,
        -0.25, 0.25, 0.0,
    ]

    var vertex_Buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vertex_Buffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);
    gl.bindBuffer(gl.ARRAY_BUFFER, null);


    var vertCode =
        'attribute vec3 coordinates;\n' +
        '\n' +
        'void main(void) {\n' +
        ' gl_Position = vec4(coordinates,1.0);\n' +
        'gl_PointSize = 30.0;\n' +
        '}';
    var fragCode =
        'void main(void) {\n' +
        'gl_FragColor = vec4(1,0.5,0.0,0.1);\n' +
        '}';
        //  // fragment shader source code
        //  var fragCode =
        //     'void main(void) {' +
        //        ' gl_FragColor = vec4(0.0, 0.0, 0.0, 0.1);' +
        //     '}';


    var vertShader = gl.createShader(gl.VERTEX_SHADER);
    gl.shaderSource(vertShader, vertCode);
    gl.compileShader(vertShader);


    var fragShader = gl.createShader(gl.FRAGMENT_SHADER);
    gl.shaderSource(fragShader, fragCode);
    gl.compileShader(fragShader);


    var program = gl.createProgram();
    gl.attachShader(program, vertShader);
    gl.attachShader(program, fragShader);
    gl.linkProgram(program);
    gl.useProgram(program);


    gl.bindBuffer(gl.ARRAY_BUFFER, vertex_Buffer);
    var coord = gl.getAttribLocation(program, 'coordinates');
    gl.vertexAttribPointer(coord, 3, gl.FLOAT, false, 0, 0);
    gl.enableVertexAttribArray(coord);



    gl.clearColor(0.6, 0.0, 0.0, 0.9);
    gl.enable(gl.DEPTH_TEST);
    gl.clear(gl.COLOR_BUFFER_BIT);
    gl.viewport(0, 0, canvas.width, canvas.height);
    gl.drawArrays(gl.POINTS, 0, 3)
}