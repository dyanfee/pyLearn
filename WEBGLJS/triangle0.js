window.onload = function () {
    // 获取画布
    var canvas = document.getElementById("canvas");
    var gl = canvas.getContext('webgl');
    // 定义顶点
    var vertices = [-0.5, 0.5, -0.5, -0.5, 0.0, -0.5,];
    // 创建缓存对象
    var vertex_buffer = gl.createBuffer()
    // 绑定空数组到缓冲对象
    gl.bindBuffer(gl.ARRAY_BUFFER, vertex_buffer)
    // 将顶点数据存入
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(vertices), gl.STATIC_DRAW);
    // 释放缓存
    gl.bindBuffer(gl.ARRAY_BUFFER, null);


    var vertCode = 'attribute vec2 coordinates;\n' +
        'void main(void) {\n' +
        ' gl_Position = vec4(coordinates,0.0,1.0);\n' +
        '}'
    // 创建顶点着色器对象
    var vertShader = gl.createShader(gl.VERTEX_SHADER);
    // 加入顶点着色器
    gl.shaderSource(vertShader, vertCode);

    gl.compileShader(vertShader);


    var fragCode =
        // '#ifdef GL_ES\n' +
        // 'precision mediump float;\n' +
        // '#endif\n' +
        'void main(void) {\n' +
        'gl_FragColor = vec4(0.0,0.0,0.0,0.1);\n' +
        '}';
    var fragShader = gl.createShader(gl.FRAGMENT_SHADER);
    gl.shaderSource(fragShader, fragCode);
    gl.compileShader(fragShader);

    var shaderProgram = gl.createProgram();
    gl.attachShader(shaderProgram, vertShader);
    gl.attachShader(shaderProgram, fragShader);

    // if (!gl.getProgramParameter(shaderProgram, gl.LINK_STATUS)) {
    //     alert("Could not initialise shaders");
    // }

    gl.linkProgram(shaderProgram);
    gl.useProgram(shaderProgram);

    //Bind vertex buffer object
    gl.bindBuffer(gl.ARRAY_BUFFER, vertex_buffer);

    //Get the attribute location
    var coord = gl.getAttribLocation(shaderProgram, "coordinates");

    //point an attribute to the currently bound VBO
    gl.vertexAttribPointer(coord, 2, gl.FLOAT, false, 0, 0);


   /*
        void vertexAttribPointer(location, int size, enum type, bool normalized, long stride, long offset)
		此方法接受六个参数，它们讨论下面。
				Location − 它指定一个属性变量的存储位置。根据这个方案，必须通过由getAttribLocation()方法返回的值
				Size − 它指定在缓冲对象每顶点部件的数量
				Type − 它指定数据的类型
				Normalized − 这是一个布尔值。如果为真，非浮动数据被归一化到[0,1]。否则，它被归一化到[-1,1]。
				Stride − 它指定不同顶点数据元素之间的字节数，或默认为零步幅。
				Offset − 它指定在缓冲器对象，以指示数据从顶点的哪个存储字节偏移(字节)。如果数据是从开始(beginning)存储的，偏移量(offset)为0。原文出自【易百教程】，商业转载请联系作者获得授权，非商业请保留原文链接：https://www.yiibai.com/webgl/associating_attributes_buffer_objects.html#article-start
 */





    //Enable the attribute
    gl.enableVertexAttribArray(coord);

    // Clear the canvas
    gl.clearColor(0.5, 0.5, 0.5, 0.9);

    // Enable the depth test
    gl.enable(gl.DEPTH_TEST);

    // Clear the color buffer bit
    gl.clear(gl.COLOR_BUFFER_BIT);

    // Set the view port
    gl.viewport(0, 0, canvas.width, canvas.height);

    // Draw the triangle
    gl.drawArrays(gl.TRIANGLES, 0, 3);




}