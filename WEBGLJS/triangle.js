window.onload = function () {
    // 获取画布
    var canvas = document.getElementById("canvas");
    var gl = canvas.getContext('webgl');


    // 定义顶点
    var vertices = [-0.0, 0.5, -0.25, -0.5, 0.25, -0.5,];
    var indices = [0, 1, 2];
    // 创建缓存对象
    var vertex_buffer = gl.createBuffer()
    // 绑定空数组到缓冲对象
    gl.bindBuffer(gl.ARRAY_BUFFER, vertex_buffer)
    // 将顶点数据存入
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);
    // 释放缓存
    gl.bindBuffer(gl.ARRAY_BUFFER, null);


    var indices_buffer = gl.createBuffer()
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indices_buffer)
    gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(indices), gl.STATIC_DRAW);
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, null);



    var vertCode = 'attribute vec2 coordinates;\n' +
        'void main(void) {\n' +
        ' gl_Position = vec4(coordinates,0.0,1.0);\n' +
        '}'
    var vertShader = gl.createShader(gl.VERTEX_SHADER);
    gl.shaderSource(vertShader, vertCode);
    gl.compileShader(vertShader);


    var fragCode =
        // '#ifdef GL_ES\n' +
        // 'precision mediump float;\n' +
        // '#endif\n' +
        'void main(void) {\n' +
        'gl_FragColor = vec4(0.0,1.0,0.0,0.7);\n' +
        '}';
    var fragShader = gl.createShader(gl.FRAGMENT_SHADER);
    gl.shaderSource(fragShader, fragCode);
    gl.compileShader(fragShader);



    var shaderProgram = gl.createProgram();
    gl.attachShader(shaderProgram, vertShader);
    gl.attachShader(shaderProgram, fragShader);
    gl.linkProgram(shaderProgram);
    gl.useProgram(shaderProgram);


    gl.bindBuffer(gl.ARRAY_BUFFER, vertex_buffer);
    gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, indices_buffer);
    var coord = gl.getAttribLocation(shaderProgram, "coordinates");
    gl.vertexAttribPointer(coord, 2, gl.FLOAT, false, 0, 0);





    //Enable the attribute
    gl.enableVertexAttribArray(coord);

    // Clear the canvas
    gl.clearColor(0.5, 0.5, 1.0, 0.9);

    // Enable the depth test
    gl.enable(gl.DEPTH_TEST);

    // Clear the color buffer bit
    gl.clear(gl.COLOR_BUFFER_BIT);

    // Set the view port
    gl.viewport(0, 0, canvas.width, canvas.height);

    // Draw the triangle
    // gl.drawArrays(gl.TRIANGLES, 0, 3);
    gl.drawElements(gl.TRIANGLES, indices.length, gl.UNSIGNED_SHORT, 0);




}