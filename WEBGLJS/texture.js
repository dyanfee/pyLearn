/**  将纹理加载到webgl */
window.onload = function () {

    // var gl = document.createElement('canvas').getContext('webgl');
    var canvas = document.getElementById('canvas');
    gl = canvas.getContext('webgl');

    var vertCode =
        'attribute vec4 a_Position;' +
        'attribute vec2 a_TexCoord;' +
        'varying vec2 v_TexCoord;' +
        'void main() {' +
        'gl_Position = a_Position;' +
        'v_TexCoord = a_TexCoord;' +
        '}';
    // "attribute vec4 a_Position;\n" +//

    // "attribute vec2 a_TexCoord;\n" +//

    // "varying vec2 v_TexCoord;\n" +//

    // "void main(){\n" +

    // "   gl_Position = a_Position;\n" +

    // "   v_TexCoord = a_TexCoord;\n" +//

    // "}\n";


    var fragCode =
        // 'precision mediump float;' +
        'uniform sampler2D u_Sampler;' +
        'varying vec2 v_TexCoord;' +
        'void main() {' +
        'gl.FragColor = texture2D(u_Sampler,v_TexCoord);' +
        '}';


    var vertices = new Float32Array([
        -0.5, 0.5, 0.0, 1.0,
        -0.5, -0.5, 0.0, 0.0,
        0.5, 0.5, 1.0, 1.0,
        0.5, -0.5, 1.0, 0.0
    ])
    var vert_buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, vert_buffer);
    gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);
    // gl.bindBuffer(gl.ARRAY_BUFFER, null);
    var fsize = vertices.BYTES_PER_ELEMENT;

    var vertShader = gl.createShader(gl.VERTEX_SHADER);
    gl.shaderSource(vertShader, vertCode);
    gl.compileShader(vertShader);

    var fragShader = gl.createShader(gl.FRAGMENT_SHADER);
    gl.shaderSource(fragShader, fragCode);
    gl.compileShader(fragShader);

    // var program = gl.createProgram();
    // gl.attachShader(program, vertShader);
    // gl.attachShader(program, fragShader);
    // gl.linkProgram(program);
    // gl.useProgram(program);

    var a_Position = gl.getAttribLocation(gl.program, "a_Position");
    gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, fsize * 4, 0);
    gl.enableVertexAttribArray(a_Position);

    var a_TexCoord = gl.getAttribLocation(gl.program, 'a_TexCoord');
    if (a_TexCoord < 0) {

        console.log("无法获取到存储位置");

        return;

    }
    gl.vertexAttribPointer(a_TexCoord, 2, gl.FLOAT, false, fsize * 4, fsize * 2);
    gl.enableVertexAttribArray(a_TexCoord);

    var texture = gl.createTexture();
    var u_Sampler = gl.getUniformLocation(gl.program, 'u_Sampler');
    var imgage = new Image();
    // imgage.crossOrigin = '';
    imgage.onload = function () {
        console.log(texture,u_Sampler)
        gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, 1);
        gl.activeTexture(gl.TEXTURE0);
        gl.bindTexture(gl.TEXTURE_2D, texture);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
        gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB, gl.RGB, gl.UNSIGNED_BYTE, imgage);
        gl.uniform1i(u_Sampler, 0);
        gl.clear(gl.COLOR_BUFFER_BIT);
        gl.drawArrays(gl.TRIANGLE_STRIP, 0, 4);
    };
    imgage.src = './texture.jpg';


}