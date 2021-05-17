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




# showSDF.frag

This code is based on bwlow ocde
GLSL Sandbox
http://glslsandbox.com/e#45332.0

Shadertoy --- original ---
https://www.shadertoy.com/view/ldcyW4

"showSDF.frag" shows above modeling with Visual Studio Code and so on  with Shadertoy plugin.
replace below line with ouput of cnvSDF


                   "put output of convSDF here"                                  

