window.onload = function () {

    var canvas = document.getElementById('canvas');
    var gl = canvas.getContext('webgl');


    /*======= Defining and storing the geometry ======*/

    var vertices = [
        -0.7, -0.1, 0,
        -0.3, 0.6, 0,
        -0.3, -0.3, 0,
        0.2, 0.6, 0,
        0.3, -0.3, 0,
        0.7, 0.6, 0
    ]
    // var vertices = [
    //     -0.5, 0.5, 0.0,
    //     -0.5, -0.5, 0.0,
    //     0.5, -0.5, 0.0,
    //     0.5, 0.5, 0.0
    // ]

    var indices = [0,1,2,1,3,4,3,4,5]

    var colors = [
        0, 0, 1,
        0, 0, 1,
        0, 0, 1,
        // 1, 0, 0,
        // 0, 1, 0,
        1, 0, 0,
        0, 1, 0,
        1, 0, 1,]

    var vertex_buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vertex_buffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);
    gl.bindBuffer(gl.ARRAY_BUFFER, null);


    var index_buffer = gl.createBuffer();
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, index_buffer);
    gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(indices), gl.STATIC_DRAW);
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, null);


    var color_buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, color_buffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(colors), gl.STATIC_DRAW);

    // Vertex shader source code
    var vertCode =
        'attribute vec3 coordinates;' +
        'attribute vec3 color;' +
        'uniform mat4 u_xformMatrix;' +
        'varying vec3 vColor;' +
        'void main(void) {' +
        ' gl_Position =u_xformMatrix * vec4(coordinates, 1.0);' +
        'vColor = color;' +
        '}';


    var vertShader = gl.createShader(gl.VERTEX_SHADER);
    gl.shaderSource(vertShader, vertCode);
    gl.compileShader(vertShader);



    // Fragment shader source code
    var fragCode =
        'precision mediump float;' +
        'varying vec3 vColor;' +
        'void main(void) {' +
        'gl_FragColor = vec4(vColor, 1.);' +
        '}';


    // Create fragment shader object
    var fragShader = gl.createShader(gl.FRAGMENT_SHADER);

    // Attach fragment shader source code
    gl.shaderSource(fragShader, fragCode);

    // Compile the fragmentt shader
    gl.compileShader(fragShader);

    // Create a shader program object to store
    // the combined shader program
    var shaderProgram = gl.createProgram();

    // Attach a vertex shader
    gl.attachShader(shaderProgram, vertShader);

    // Attach a fragment shader
    gl.attachShader(shaderProgram, fragShader);

    // Link both the programs
    gl.linkProgram(shaderProgram);

    // Use the combined shader program object
    gl.useProgram(shaderProgram);



    var Sx = 1.0, Sy = 1.5, Sz = 1.0;
    var xformMatrix = new Float32Array([
        Sx, 0.0, 0.0, 0.0,
        0.0, Sy, 0.0, 0.0,
        0.0, 0.0, Sz, 0.0,
        0.0, 0.0, 0.0, 1.0
    ]);

    var u_xformMatrix = gl.getUniformLocation(shaderProgram, 'u_xformMatrix');
    gl.uniformMatrix4fv(u_xformMatrix, false, xformMatrix);






    // Bind vertex buffer object
    gl.bindBuffer(gl.ARRAY_BUFFER, vertex_buffer);
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, index_buffer);

    // Get the attribute location
    var coord = gl.getAttribLocation(shaderProgram, "coordinates");

    // Point an attribute to the currently bound VBO
    gl.vertexAttribPointer(coord, 3, gl.FLOAT, false, 0, 0);

    // Enable the attribute
    gl.enableVertexAttribArray(coord);
    gl.bindBuffer(gl.ARRAY_BUFFER, color_buffer);

    var color = gl.getAttribLocation(shaderProgram, 'color');
    gl.vertexAttribPointer(color, 3, gl.FLOAT, false, 0, 0);
    gl.enableVertexAttribArray(color);

    // Clear the canvas
    gl.clearColor(0.5, 0.5, 0.5, 0.9);

    // Enable the depth test
    gl.enable(gl.DEPTH_TEST);

    // Clear the color and depth buffer
    gl.clear(gl.COLOR_BUFFER_BIT);

    // Set the view port
    gl.viewport(0, 0, canvas.width, canvas.height);

    // Draw the triangle
    // gl.drawArrays(gl.LINES, 0, 6);
    // gl.drawArrays(gl.LINE_LOOP, 0, 6);
    // gl.drawArrays(gl.LINE_STRIP, 0, 6);
    // gl.drawArrays(gl.TRIANGLES, 0, 6);
    // gl.drawArrays(gl.TRIANGLE_STRIP, 0, 5);
    // gl.drawArrays(gl.TRIANGLE_FAN, 0, 5);

    gl.drawElements(gl.TRIANGLES, indices.length, gl.UNSIGNED_SHORT, 0)

    // POINTS, LINE_STRIP, LINE_LOOP, LINES,
    // TRIANGLE_STRIP,TRIANGLE_FAN, TRIANGLES







}