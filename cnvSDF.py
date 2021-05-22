import json
import numpy as np
# rotation matrix
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

def total(mf):
    #print(">>>> ",mf)
    global gcount
    global pcount
    #print('>>>> ',len(mf),mf)
    #
    prm = []
    if len(mf) > 1:
         #print('===> ', mf,len(mf))
         if not isinstance(mf[0], list):
            if mf[0] == 'ref':
                #print('>>>>  ',prim[mf[1]],' refnum = ', mf[1])
                prHead = prim[mf[1]][0]
                #prVal  = prim[mf[1]][0]
                prVal  = prim[mf[1]][1]

                if(prHead == 'pEllipsoid'):
                    spos = prVal.replace('Vector3','vec3')
                    prm.append('vec3 ElRa_' + str(gcount) + ' = ' + spos + ';')
                    gcount += 1
                if prHead == 'pBox':
                    spos = prVal.replace('Vector3','vec3')
                    prm.append('vec3 BoSi_' + str(gcount) + ' = ' + spos + ';')
                    gcount += 1
                if prHead == 'pCylinder':
                    val = str(float(prVal))
                    prm.append('float ToRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                    val  = str(float(prim[mf[1]][2]))
                    prm.append('float TOra_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pTorus':
                    val = str(float(prVal))
                    prm.append('float ToRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                    val  = str(float(prim[mf[1]][2]))
                    prm.append('float ToRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pCone':
                    val = str(float(prVal))
                    #val1 = str(float(prVal))
                    prm.append('vec2 CoGe_' + str(gcount)  + ' = vec2(' + val + ' ,' + val +');')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float CoHe_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pCappedTorus':
                    #print('====================',prim[mf[1]][1], ' ',prim[mf[1]][2])
                    #val = str(float(prVal))
                    #val1 = str(float(prVal))
                    fval = float(np.radians(prVal))
                    si = np.sin(fval)
                    co = np.cos(fval)
                    prm.append('vec2 CaGe_' + str(gcount)  + ' = vec2(' + str(si) + ' ,' + str(co) +');')
                    #prm.append('vec2 CaGe_' + str(gcount)  + ' = vec2(' + val + ' ,' + val +');')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float CaRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][3]))
                    prm.append('float CaRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pCappedCone':
                    #print('====================',prim[mf[1]][1], ' ',prim[mf[1]][2])
                    val = str(float(prVal))
                    #val1 = str(float(prVal))
                    prm.append('float CaHe_' + str(gcount)  + ' = '+ val + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float CaRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                    #val1 = str(float(prim[mf[1]][3]))
                    prm.append('float CaRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pCapsule':
                    val = str(float(prVal))
                    #val1 = str(float(prVal))
                    prm.append('float CaRa_' + str(gcount)  + ' = '+ val + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float CaHe_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pRoundCone':
                    #print('====================',prim[mf[1]][1], ' ',prim[mf[1]][2])
                    val = str(float(prVal))
                    #val1 = str(float(prVal))
                    prm.append('float RoRa_' + str(gcount)  + ' = ' + str(val) + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float RoRa_' + str(gcount) + ' = ' + val + ';')
                    val = str(float(prim[mf[1]][3]))
                    gcount += 1
                    prm.append('float RoHe_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pPlane':
                    #print('====================',prim[mf[1]][1], ' ',prim[mf[1]][2])
                    val = str(prVal)
                    val = val.replace('Vector3','vec3')
                    #val1 = str(float(prVal))
                    prm.append('vec3 PlNo_' + str(gcount)  + ' = ' + str(val) + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float PlDi_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pFrame':
                    #print('====================',prim[mf[1]][1], ' ',prim[mf[1]][2])
                    val = str((prVal))
                    val = val.replace('Vector3','vec3')
                    #val1 = str(float(prVal))
                    prm.append('vec3 FrSi_' + str(gcount)  + ' = ' + str(val) + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float FrTh_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pSolidAngle':
                   #print('====================',prim[mf[1]][1], ' ',prim[mf[1]][2])
                    fval = float(np.radians(prVal))
                    si = np.sin(fval)
                    co = np.cos(fval)
                    prm.append('vec2 SoGe_' + str(gcount)  + ' = vec2(' + str(si) + ' ,' + str(co) +');')
                    #val0 = val0.replace('Vector3','vec3')
                    #val1 = str(float(prVal))
                    #prm.append('vec2 SoGe_' + str(gcount)  + ' = vec2(' + val + ' ,' + val +');')
                    #prm.append('vec2 SoGe_' + str(gcount)  + ' = ' + val0 +  ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float SoRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pLink':
                    #print('====================',prim[mf[1]][1], ' ',prim[mf[1]][2])
                    val = str(float(prVal))
                    #val1 = str(float(prVal))
                    prm.append('float LiLe_' + str(gcount)  + ' = ' + str(val) + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float LiRa_' + str(gcount) + ' = ' + val + ';')
                    val = str(float(prim[mf[1]][3]))
                    gcount += 1
                    prm.append('float LiRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                    #pOctahedron
                if prHead == 'pOctahedron':
                    #print('====================',prim[mf[1]][1], ' ',prim[mf[1]][2])
                    val = str(float(prVal))
                    prm.append('float OcRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                    #pHexPrism
                if prHead == 'pHexPrism':
                    val = str(float(prVal))
                    prm.append('float HeHe_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float HeRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1

                if prHead == 'pTriPrism':
                    val = str(float(prVal))
                    prm.append('float TrHe_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float TrRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1

                if prHead == 'pPyramid':
                    val = str(float(prVal))
                    prm.append('float PyHe_' + str(gcount) + ' = ' + val + ';')
                    #val = str(float(prim[mf[1]][2]))
                    #prm.append('float HeRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
               

                for pm in prm:
                    print(pm)
                    #gcount += 

            #val1 = str(float(prim[1][2]))
            #prm.append('float CyHe_' + str(gcount) + ' = ' + val1 + ';')
            #gcount += 1
            if mf[0] == 'mTranslation':
            # get vector float value
                spos = mf[len(mf)-1].replace('Vector3(','') 
                spos = spos.replace(')','')
                u = spos.split(',')
                v0 = -float(u[0])
                v1 = -float(u[1])
                v2 = -float(u[2])
                # make vec3 TrIn_?? = .... format
                rt = 'vec3 TrIn_'+str(gcount) #header
                rt = rt + ' = vec3(' + str(v0) +' ,'+ str(v1) + ' ,'  + str(v2) + ');'
                print(rt)
                gcount += 1
            if mf[0] == 'mRotation':
                rv = mf[2]     #totatuon value
                rt = 'mat3 RoIn_'+str(gcount)
                #
                t = rv.replace('Vector3(','')
                t = t.replace(')','')
                u = t.split(',')
                # get float rotation value
                v0 = -float(u[0])
                v1 = -float(u[1])
                v2 = -float(u[2])
                #rot = rotate_x(v0)*rotate_z(v2)
                rot = rotate_x(v0)*rotate_y(v1)*rotate_z(v2)
                e = np.linalg.inv(rot) #inverse matrix
                # for output mat3
                strm = str(e)
                strm = strm.replace('[[' ,'mat3(')
                strm = strm.replace(']]' ,');')
                strm = strm.replace(' ' ,'_')
                strm = strm.replace('\n' ,'')
                strm = strm.replace(']_[' ,'_')
                strm = strm.replace('_' ,',')
                strm = strm.replace('(,' ,'( ')
        #
                while  ',,' in strm:
                    strm = strm.replace(',,' ,',')
                strm = strm.replace(',)' ,')')
                # print mat3
                print(rt,'=', strm)
                gcount += 1
            for mem in mf:
                if isinstance(mem, list):
                    for mm in mem:
                        #print('---> ',mm,len(mm))
                        total(mm)
            return
    else:
        return
    #print('here ---> ',mf)
    
    

    
# analyze operator_tree
def total2(mf):
    global gcount
    if len(mf) > 1:
        #print(len(mf[0]),len(mf), mf)
        if not isinstance(mf[0], list):
                #print(mf[0])
                if(mf[0] == 'oThicken'):
                    #print('float ThTh_' + str(gcount) + ' = ' + str(mf[2]) + ';')
                    gcount += 1
                if(mf[0] == 'oSmoothUnion'):
                    print('float SmTr_' + str(gcount) + ' = ' + str(mf[2]) + ';')
                    gcount += 1
                if(mf[0] == 'oSmoothSubtraction'):
                    print('float SmTr_' + str(gcount) + ' = ' + str(mf[2]) + ';')
                    gcount += 1

        for mem in mf:
            if isinstance(mem, list):
                total2(mem)

global gcount
global pcount
gcount = 1
pcount = 0
#
#  main    
# read json file
f = open('sample.json', 'r')
json_dict = json.load(f)
prim = json_dict['primitives']
#j = 0
modi = json_dict['modifiers']
print('//----------------------------------------------------------------')
for md in  modi:
    total(md)
    #j += 1
opt = json_dict['operator_tree']
###    total2(a[0])

for op in  opt:

    #print('----',len(opt),'  ',opt)
    total2(op[0])
print('//----------------------------------------------------------------')





