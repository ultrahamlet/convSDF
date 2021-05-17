# convSDF

"convSDF" convert json file from "SDF Editor" https://joetech.itch.io/sdf-editor to GLSL code.

"SDF Editor" is prototype SDF modeling tool.
![alt text](https://github.com/ultrahamlet/convSDF/blob/main/blob.jpg?raw=true)

Shadertoy showing with abobe modeling data:

![alt text](https://github.com/ultrahamlet/convSDF/blob/main/shadertoy.jpg?raw=true)

-> real time rendering example via browser http://dcf.jp/cascade.html


## This converter is limited to ellipsoid SDF so far.
Prepare ellipsoids as follows:

![alt text](https://github.com/ultrahamlet/convSDF/blob/main/menu.jpg?raw=true)

# cnvSDF.py

convert json output from "SDF Editor" to GLSL code for Shadertoy or GLSL Sandbox.

below is output lines when you type "python convSDF.py" with use "test.json", above modeling.

>float blob0 = sdEllipsoid(Rotate(pos - vec3( 0, 0, 0 ) , vec3( 0.0 , 0.0 , 1.0 ), -0.0 ), vec3( 0.3, 0.7, 0.3 ) );
>float blob1 = sdEllipsoid(Rotate(pos - vec3( 0.6, -0.1, 0 ) , vec3( -0.0 , -0.0 , -0.17453292519943292 ), -9.999999999999998 ), vec3( 0.3, 0.7, 0.3 ) );
>float blob2 = sdEllipsoid(Rotate(pos - vec3( -0.6, -0.1, 0 ) , vec3( -0.0 , -0.0 , 0.17453292519943292 ), -9.999999999999998 ), vec3( 0.3, 0.7, 0.3 ) );
>float blob3 = sdEllipsoid(Rotate(pos - vec3( -1.2, -0.3, 0 ) , vec3( 0.5299444538176428 , 0.07975984427717622 , 0.38456721096773666 ), -37.79327497049043 ), vec3( 0.53, 1.16, 0.3 ) );
>float blob4 = sdEllipsoid(Rotate(pos - vec3( 1.2, -0.3, 0 ) , vec3( 0.03870171594046606 , 0.18351114054423867 , -0.3420014972101488 ), -22.348232248236474 ), vec3( 0.3, 0.7, 0.3 ) );
>float blob5 = sdEllipsoid(Rotate(pos - vec3( 2, -1, 0.1 ) , vec3( -0.0 , -0.0 , 0.34906585039886595 ), -20.000000000000004 ), vec3( 0.4, 0.5, 0.5 ) );
>float blob6 = sdEllipsoid(Rotate(pos - vec3( -0.9, -1, 0.3 ) , vec3( 0.0 , 0.0 , 1.0 ), -0.0 ), vec3( 0.3, 0.3, 0.3 ) );
>float blob7 = sdEllipsoid(Rotate(pos - vec3( -0.5, -1, 0 ) , vec3( 0.0 , 0.0 , 1.0 ), -0.0 ), vec3( 0.3, 0.4, 0.3 ) );
>float blob8 = sdEllipsoid(Rotate(pos - vec3( -0.1, -1, 0 ) , vec3( 0.0 , 0.0 , 1.0 ), -0.0 ), vec3( 0.3, 0.4, 0.3 ) );
>float blob9 = sdEllipsoid(Rotate(pos - vec3( 0.4, -1.1, 0 ) , vec3( 0.0 , 0.0 , 1.0 ), -0.0 ), vec3( 0.3, 0.4, 0.3 ) );
>float blob10 = sdEllipsoid(Rotate(pos - vec3( 1.16, -1.2, 0 ) , vec3( 0.20868863562245224 , 0.2064328427505375 , 0.02169696607101488 ), -16.864458033998545 ), vec3( 0.71, 0.4, 0.3 ) );
>float blob11 = sdEllipsoid(Rotate(pos - vec3( -0.6, -1, 0.3 ) , vec3( 0.0 , 0.0 , 1.0 ), -0.0 ), vec3( 0.25, 0.25, 0.25 ) );
>float body = smin(blob0,smin(blob1,smin(blob2,smin(blob3,smin(blob4,smin(blob5,smin(blob6,smin(blob7,smin(blob8,smin(blob9,smin(blob10,blob11,s),s),s),s),s),s),s),s),s),s),s);

# showSDF.frag

This code is based on bwlow ocde
GLSL Sandbox
http://glslsandbox.com/e#45332.0

Shadertoy --- original ---
https://www.shadertoy.com/view/ldcyW4

"showSDF.frag" shows above modeling with Visual Studio Code and so on  with Shadertoy plugin.
replace below line with ouput of cnvSDF


                   "put output of convSDF here"                                  

