import json
import numpy as np
import quaternion

# -*- coding: utf-8 -*-
import numpy as np

def rotate_x(deg):
    # degree to radian
    r = np.radians(deg)
    C = np.cos(r)
    S = np.sin(r)
    # rotate x
    R_x = np.matrix((
        (1, 0, 0),
        (0, C, -S),
        (0, S, C)
    ))
    return R_x

def rotate_y(deg):
    # degree to radian
    r = np.radians(deg)
    C = np.cos(r)
    S = np.sin(r)
    # rotate y
    R_y = np.matrix((
        (C, 0, S),
        (0, 1, 0),
        (-S, 0, 1)
    ))
    return R_y

def rotate_z(deg):
     # degree to radian
    r = np.radians(deg)
    C = np.cos(r)
    S = np.sin(r)
     # rotate z
    R_z = np.matrix((
        (C, -S, 0),
        (S, C, 0),
        (0, 0, 1)
    ))

    return R_z

# read json file
f = open('test10.json', 'r')
json_dict = json.load(f)
#print('json_dict:{}'.format(type(json_dict)))
n = 0
val0 = []
val1 = []
scale = []
pos   = []
rotate = []
for v in json_dict.values():
    
    if n == 0:
        val0 = v
    if n == 1:
        val1 = v

    n += 1
n = 0
for vals in val0:
    #print(vals[1], '-->scale')
    scale.append(vals[1].replace('Vector3(','vec3('))
    j = 0
    for vv in val1[n]:
        if j == 1:
            k = 0
            for vvv in vv:
                if k == 0:
                   rotate.append(vvv[2])
                k += 1
        if j == 2:
           #print(vv,'-->pos')
           pos.append(vv.replace('Vector3(','vec3('))
        j += 1
    n += 1
    #print("-----")
#rot = rotate_x(0.)*rotate_y(0.)*rotate_z(10.)
#e = np.linalg.inv(rot)
#print(scale)
#print(pos)
print ('#')
bl = []
i = 0
for r in rotate:
     t = r.replace('Vector3(','')
     t = t.replace(')','')
     u = t.split(',')
     # rotation
     v0 = float(u[0])
     v1 = float(u[1])
     v2 = float(u[2])
     rot = rotate_x(v0)*rotate_y(v1)*rotate_z(v2)
     qt = quaternion.from_rotation_matrix(rot, nonorthogonal=True)
     axis = quaternion.as_rotation_vector(qt)
     angle = np.degrees(qt.angle())
     blob = 'blob'+str(i)
     blob.replace(' ','')
     bl.append(blob)
     if angle == 0:
         axis[2] = 1.0
     print('float',blob,'= sdEllipsoid(Rotate(pos -',pos[i],', vec3(',axis[0],',',axis[1],',',axis[2],'),', -angle,'),',scale[i],');')
     i += 1
i = 0
body = 'float body = '
for blb in bl:

    if i < len(bl)-1:
        body = body + 'smin(' + blb + ','
    else:
        body = body + blb
    i += 1
i = 0
for blb in bl:
    if i < len(bl)-1:
        body = body +',s)'
    i += 1
body = body + ';'        
print (body) 
print ('#')
    