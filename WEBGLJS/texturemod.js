/**  将纹理加载到webgl */
window.onload = function () {

    // var gl = document.createElement('canvas').getContext('webgl');
    var canvas = document.getElementById('canvas');
    gl = canvas.getContext('webgl');


    /*第一部分顶点着色器接收顶点的纹理坐标，传递给片元着色器*/

    var VSHADER_SOURCE = "" +

        "attribute vec4 a_Position;\n" +//

        "attribute vec2 a_TexCoord;\n" +//

        "varying vec2 v_TexCoord;\n" +//

        "void main(){\n" +

        "   gl_Position = a_Position;\n" +

        "   v_TexCoord = a_TexCoord;\n" +//

        "}\n";



    var FSHADER_SOURCE = "" +

        "precision mediump float;\n" +//

        "uniform sampler2D u_Sampler;\n" +//

        "varying vec2 v_TexCoord;\n" +//

        "void main(){\n" +

        "   gl_FragColor = texture2D(u_Sampler,v_TexCoord);\n" +//

        "}\n";




    //设置顶点的相关信息

    var n = initVertexBuffers(gl);



    if (n < 0) {

        console.log("无法获取到点的数据");

        return;

    }



    //配置纹理

    if (!initTextures(gl, n)) {

        console.log("无法配置纹理");

        return;

    }







    /*第三部分 initVertexBuffers() 设置顶点坐标和纹理坐标 调用initTextures()进行下一步处理*/

    function initVertexBuffers(gl) {

        var verticesSizes = new Float32Array([

            //四个顶点的位置和纹理数据

            -0.5, 0.5, 0.0, 1.0,

            -0.5, -0.5, 0.0, 0.0,

            0.5, 0.5, 1.0, 1.0,

            0.5, -0.5, 1.0, 0.0

        ]);



        var n = 4;

        var vertexSizeBuffer = gl.createBuffer();

        if (!vertexSizeBuffer) {

            console.log("无法创建缓冲区");

            return -1;

        }

        gl.bindBuffer(gl.ARRAY_BUFFER, vertexSizeBuffer);

        gl.bufferData(gl.ARRAY_BUFFER, verticesSizes, gl.STATIC_DRAW);

        var a_Position = gl.getAttribLocation(gl.program, "a_Position");

        if (a_Position < 0) {

            console.log("无法获取到存储位置");

            return;

        }



        //获取数组一个值所占的字节数

        var fsize = verticesSizes.BYTES_PER_ELEMENT;



        //将顶点坐标的位置赋值

        gl.vertexAttribPointer(a_Position, 2, gl.FLOAT, false, fsize * 4, 0);

        gl.enableVertexAttribArray(a_Position);



        //将顶点的纹理坐标分配给a_TexCoord并开启它

        var a_TexCoord = gl.getAttribLocation(gl.program, "a_TexCoord");

        if (a_TexCoord < 0) {

            console.log("无法获取到存储位置");

            return;

        }



        //将纹理坐标赋值

        gl.vertexAttribPointer(a_TexCoord, 2, gl.FLOAT, false, fsize * 4, fsize * 2);

        gl.enableVertexAttribArray(a_TexCoord);

        return n;

    }



    /*第四部分 initTextures() 创建纹理对象 并调用纹理绘制方法*/

    function initTextures(gl, n) {

        var texture = gl.createTexture();//创建纹理对象

        if (!texture) {

            console.log("无法创建纹理对象");

            return;

        }



        //获取u_Sampler的存储位置

        var u_Sampler = gl.getUniformLocation(gl.program, "u_Sampler");

        if (u_Sampler < 0) {

            console.log("无法获取变量的存储位置");

            return;

        }



        //创建Image对象，并绑定加载完成事件

        var image = new Image();

        image.onload = function () {

            loadTexture(gl, n, texture, u_Sampler, image);

        };



        image.src = "/lib/textures/crate.gif";

        return true;

    }



    /*第五部分 设置纹理相关信息供WebGL使用，并进行绘制*/

    function loadTexture(gl, n, texture, u_Sampler, image) {

        //对纹理图像进行y轴反转

        gl.pixelStorei(gl.UNPACK_FLIP_Y_WEBGL, 1);

        //开启0号纹理单元

        gl.activeTexture(gl.TEXTURE0);

        //向target绑定纹理对象

        gl.bindTexture(gl.TEXTURE_2D, texture);

        //配置纹理参数

        gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);

        //配置纹理图像

        gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGB, gl.RGB, gl.UNSIGNED_BYTE, image);

        //将0号纹理传递给着色器

        gl.uniform1i(u_Sampler, 0);



        //绘制

        gl.clearColor(0.0, 0.0, 0.0, 1.0);



        gl.clear(gl.COLOR_BUFFER_BIT);



        gl.drawArrays(gl.TRIANGLE_STRIP, 0, n);

    }


}