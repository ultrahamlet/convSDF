import json
from scipy.spatial.transform import Rotation
import numpy as np

def hierarchy(mf):
    global gcount
    global pcount
    prm = []
    if len(mf) > 1:
         if not isinstance(mf[0], list):
            if mf[0] == 'ref':
                prHead = prim[mf[1]][0]
                prVal  = prim[mf[1]][1]

                

                if(prHead == 'pEllipsoid'):
                    spos = prVal.replace('Vector3(','')
                    spos = spos.replace(')','')
                    sval = spos.split(',')
                    spos = 'vec3(' + str(float(sval[0]))  + ' ,' + str(float(sval[1])) + ' ,' + str(float(sval[2])) + ')'
                    prm.append('vec3 ElRa_' + str(gcount) + ' = ' + spos + ';')
                    gcount += 1
                if prHead == 'pBox':
                    spos = prVal.replace('Vector3(','')
                    spos = spos.replace(')','')
                    sval = spos.split(',')
                    spos = 'vec3(' + str(float(sval[0]))  + ' ,' + str(float(sval[1])) + ' ,' + str(float(sval[2])) + ')'
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
                if prHead == 'pSphere':
                   val = str(float(prVal))
                   prm.append('float SpRa_' + str(gcount) + ' = ' + val + ';')
                   gcount += 1
                if prHead == 'pCone':
                    val = str(float(prVal))
                    prm.append('vec2 CoGe_' + str(gcount)  + ' = vec2(' + val + ' ,' + val +');')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float CoHe_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pCappedTorus':
                    fval = float(np.radians(prVal))
                    si = np.sin(fval)
                    co = np.cos(fval)
                    prm.append('vec2 CaGe_' + str(gcount)  + ' = vec2(' + str(si) + ' ,' + str(co) +');')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float CaRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][3]))
                    prm.append('float CaRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pCappedCone':
                    val = str(float(prVal))
                    prm.append('float CaHe_' + str(gcount)  + ' = '+ val + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float CaRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                    prm.append('float CaRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pCapsule':
                    val = str(float(prVal))
                    prm.append('float CaRa_' + str(gcount)  + ' = '+ val + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float CaHe_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pRoundCone':
                    val = str(float(prVal))
                    prm.append('float RoRa_' + str(gcount)  + ' = ' + str(val) + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float RoRa_' + str(gcount) + ' = ' + val + ';')
                    val = str(float(prim[mf[1]][3]))
                    gcount += 1
                    prm.append('float RoHe_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pPlane':
                    val = str(prVal)
                    val = val.replace('Vector3','vec3')
                    #val1 = str(float(prVal))
                    prm.append('vec3 PlNo_' + str(gcount)  + ' = ' + str(val) + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float PlDi_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pFrame':
                    val = str((prVal))
                    val = val.replace('Vector3','vec3')
                    #val1 = str(float(prVal))
                    prm.append('vec3 FrSi_' + str(gcount)  + ' = ' + str(val) + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float FrTh_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pSolidAngle':
                    fval = float(np.radians(prVal))
                    si = np.sin(fval)
                    co = np.cos(fval)
                    prm.append('vec2 SoGe_' + str(gcount)  + ' = vec2(' + str(si) + ' ,' + str(co) +');')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float SoRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pLink':
                    val = str(float(prVal))
                    prm.append('float LiLe_' + str(gcount)  + ' = ' + str(val) + ';')
                    gcount += 1
                    val = str(float(prim[mf[1]][2]))
                    prm.append('float LiRa_' + str(gcount) + ' = ' + val + ';')
                    val = str(float(prim[mf[1]][3]))
                    gcount += 1
                    prm.append('float LiRa_' + str(gcount) + ' = ' + val + ';')
                    gcount += 1
                if prHead == 'pOctahedron':
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
                    gcount += 1
               

                for pm in prm:
                    print(pm)
            #------------------------------------------------------
            if(mf[0] == 'mRepLim'):
                    #print(mf,'-- ',mf[3])
                    spos = mf[2].replace('Vector3(','')
                    spos = spos.replace(')','')
                    sval = spos.split(',')
                    spos = 'vec3(' + str(float(sval[0]))  + ' ,' + str(float(sval[1])) + ' ,' + str(float(sval[2])) + ');'
                    hd = 'vec3 ReCe_'+ str(gcount)
                    print(hd,' = ',spos)
                    gcount += 1   
                    spos = mf[3].replace('Vector3(','')
                    spos = spos.replace(')','')
                    sval = spos.split(',')
                    spos = 'vec3(' + str(float(sval[0]))  + ' ,' + str(float(sval[1])) + ' ,' + str(float(sval[2])) + ');'
                    hd = 'vec3 ReGr_'+ str(gcount)
                    print(hd,' = ',spos)
                    gcount += 1   
            if(mf[0] == 'mRepInf'):
                    #print(mf,'-- ',mf[2])
                    spos = mf[2].replace('Vector3(','')
                    spos = spos.replace(')','')
                    sval = spos.split(',')
                    spos = 'vec3(' + str(float(sval[0]))  + ' ,' + str(float(sval[1])) + ' ,' + str(float(sval[2])) + ');'
                    hd = 'vec3 ReCe_'+ str(gcount)
                    print(hd,' = ',spos)
                    gcount += 1   
            if(mf[0] == 'mMirror'):
                    #print(mf,'-- ',mf[3])    
                    spos = mf[2].replace('Vector3(','')
                    spos = spos.replace(')','')
                    sval = spos.split(',')
                    spos = 'vec3(' + str(float(sval[0]))  + ' ,' + str(float(sval[1])) + ' ,' + str(float(sval[2])) + ');'
                    hd = 'vec3 MiNo_'+ str(gcount)
                    print(hd,' = ',spos)
                    gcount += 1
                    hd = 'float MiDi_'+str(gcount)
                    print(hd,' = ' ,str(float(mf[3])),';')
                    gcount += 1
            if mf[0] == 'mTranslation':
            # get vector float value
                spos = mf[len(mf)-1].replace('Vector3(','') 
                spos = spos.replace(')','')
                u = spos.split(',')
                v0 = -float(u[0])
                v1 = -float(u[1])
                v2 = -float(u[2])
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
                
                rotvec = np.array([np.radians(v0), np.radians(v1), np.radians(v2)])
                rot = Rotation.from_rotvec(rotvec)
                
                e = np.linalg.inv(rot.as_matrix()) #inverse matrix
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
                        hierarchy(mm)
            return
    else:
        return
    
# analyze operator_tree
def hierarchy2(mf):
    global gcount
    if len(mf) > 1:
        if not isinstance(mf[0], list):
                #print('===',mf)
                if(mf[0] == 'oThicken'):
                    print('float ThTh_' + str(gcount) + ' = ' + str(mf[2]) + ';')
                    gcount += 1
                if(mf[0] == 'oSmoothUnion'):
                    print('float SmTr_' + str(gcount) + ' = ' + str(mf[2]) + ';')
                    gcount += 1
                if(mf[0] == 'oSmoothSubtraction'):
                    print('float SmTr_' + str(gcount) + ' = ' + str(mf[2]) + ';')
                    gcount += 1
                #if(mf[0] == 'oSubtraction'):
                if(mf[0] == 'oOnion'):
                    print('float OnTh_' + str(gcount) + ' = ' + str(mf[2]) + ';')
                #    print('float SpRa_' + str(gcount) + ' = ' + str(mf[2]) + ';')
                #    gcount += 1
                    gcount += 1
                if(mf[0] == 'oSmoothIntersection'):
                    print('float SmTr_' + str(gcount) + ' = ' + str(mf[2]) + ';')
                    gcount += 1

        for mem in mf:
            if isinstance(mem, list):
                hierarchy2(mem)

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
modi = json_dict['modifiers']
print('//----------------------------------------------------------------')
for md in  modi:
    hierarchy(md)
opt = json_dict['operator_tree']
###    hierarchy2(a[0])

for op in  opt:
    #print('----',len(opt),'  ',opt)
    hierarchy2(op)
print('//----------------------------------------------------------------')





