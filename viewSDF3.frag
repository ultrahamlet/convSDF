//
// Adapted from original shader: https://www.shadertoy.com/view/ldcyW4
// modeled by https://joetech.itch.io/sdf-editor
// converted by cnvSDF3

//
mat3 RoIn_1 = mat3( 1.,0.,0.,0.,0.81915204,-0.57357644,0.,0.57357644,0.81915204);
vec3 TrIn_2 = vec3(-0.0 ,-0.0 ,-0.0);
float ToRa_3 = 1.0;
float ToRa_4 = 0.25;
vec3 TrIn_5 = vec3(-0.0 ,4.0 ,-0.0);
vec3 PlNo_6 = vec3( 0, 1, 0 );
float PlDi_7 = 0.0;
float LiLe_8 = 1.;
float LiRa_9 = 1.0;
float LiRa_10 = 0.25;
//----------------------------------------------------------------
vec3 TrIn_1 = vec3(1.5 ,-0.0 ,-0.0);
float CyRa_2 = 1.0;
float CyHe_3 = 1.0;
vec3 TrIn_4 = vec3(-0.0 ,-1.0 ,-0.0);
vec3 ElRa_5 = vec3( 1, 0.5, 0.2 );
vec3 TrIn_6 = vec3(-2.0 ,-0.0 ,-0.0);
vec2 CoGe_7 = vec2(30.0 ,30.0);
float CoHe_8 = 1.0;
mat3 RoIn_9 = mat3( 0.70710678,-0.70710678,0.,0.70710678,0.70710678,0.,0.,0.,1.);
vec3 ElRa_10 = vec3( 1, 0.5, 0.2 );
vec3 TrIn_11 = vec3(4.2 ,-0.0 ,-0.0);
mat3 RoIn_12 = mat3( 0.86550523,-0.1797403,0.47112159,0.23191143,0.97138674,-0.05353717,-0.44801848,0.13474938,0.76420172);
vec3 BoSi_13 = vec3( 1, 1, 1 );
vec3 TrIn_14 = vec3(4.5 ,-2.0 ,-0.0);
vec3 ElRa_15 = vec3( 1, 0.9, 0.5 );
float SmTr_16 = 0.1;
float SmTr_17 = 0.1;
float SmTr_18 = 0.8;
//----------------------------------------------------------------
const float epsilon = 0.01;
const float pi = 3.14159265359;
const float halfpi = 1.57079632679;
const float twopi = 6.28318530718;

// rotate
vec3 rotate(vec3 p, float angle, vec3 axis){
    vec3 a = normalize(axis);
    float s = sin(angle);
    float c = cos(angle);
    float r = 1.0 - c;
    mat3 m = mat3(
        a.x * a.x * r + c,
        a.y * a.x * r + a.z * s,
        a.z * a.x * r - a.y * s,
        a.x * a.y * r - a.z * s,
        a.y * a.y * r + c,
        a.z * a.y * r + a.x * s,
        a.x * a.z * r + a.y * s,
        a.y * a.z * r - a.x * s,
        a.z * a.z * r + c
    );
    return m * p;
}

mat3 rotateMat(vec3 p, float angle, vec3 axis){
    vec3 a = normalize(axis);
    float s = sin(angle);
    float c = cos(angle);
    float r = 1.0 - c;
    mat3 m = mat3(
        a.x * a.x * r + c,
        a.y * a.x * r + a.z * s,
        a.z * a.x * r - a.y * s,
        a.x * a.y * r - a.z * s,
        a.y * a.y * r + c,
        a.z * a.y * r + a.x * s,
        a.x * a.z * r + a.y * s,
        a.y * a.z * r - a.x * s,
        a.z * a.z * r + c
    );
    return m;
}

#define LIGHT normalize(vec3(1.0, 1.0, 0.0))


//----------------------------------------------------------------------------------
float pSphere(float r, vec3 p)
{
     return length(p) - r;
}

float pBox(vec3 b, vec3 p)
{
     vec3 q = abs(p) - b;
     return length(max(q, 0.0)) + min(max(q.x, max(q.y, q.z)), 0.0);
}

float pFrame(vec3 size, float thickness, vec3 p)
{
     p = abs(p) - size;
     vec3 q = abs(p + thickness) - thickness;
     float a = length(max(vec3(p.x,q.y,q.z), 0.0)) + min(max(p.x, max(q.y, q.z)), 0.0);
     float b = length(max(vec3(q.x,p.y,q.z), 0.0)) + min(max(q.x, max(p.y, q.z)), 0.0);
     float c = length(max(vec3(q.x,q.y,p.z), 0.0)) + min(max(q.x, max(q.y, p.z)), 0.0);
     return min(min(a, b), c);
}

float pTorus(float r1, float r2, vec3 p)
{
     vec2 q = vec2(length(p.xz) - r1, p.y);
     return length(q) - r2;
}

float pCappedTorus(vec2 sc, float ra, float rb, vec3 p)
{
     p.x = abs(p.x);
     float k = (sc.y*p.x > sc.x*p.y) ? dot(p.xy, sc) : length(p.xy);
     return sqrt(dot(p,p) + ra*ra - 2.0*ra*k) - rb;
}

float pLink(float le, float r1, float r2, vec3 p)
{
     vec3 q = vec3(p.x, max(abs(p.y) - le, 0.0), p.z);
     return length(vec2(length(q.xy) - r1, q.z)) - r2;
}

float pInfCylinder(float r, vec3 p)
{
     return length(p.xz) - r;
}

float pCone(vec2 c, float h, vec3 p)
{
    // c is the sin/cos of the angle
     vec2 q = h*vec2(c.x/c.y, -1.0);

     vec2 w = vec2(length(p.xz), p.y);
     vec2 a = w - q*clamp(dot(w,q) / dot(q,q), 0.0, 1.0);
     vec2 b = w - q*vec2(clamp(w.x/q.x, 0.0, 1.0 ), 1.0);
     float k = sign(q.y);
     float d = min(dot(a,a), dot(b, b));
     float s = max(k * (w.x*q.y-w.y*q.x), k * (w.y-q.y));
     return sqrt(d) * sign(s);

     // bound:
     // float q = length(p.xz);
     // return max(dot(c.xy,vec2(q,p.y)),-h-p.y);
}

float pInfCone(vec2 c, vec3 p)
{
    // c is the sin/cos of the angle
    vec2 q = vec2( length(p.xz), -p.y );
    float d = length(q-c*max(dot(q,c), 0.0));
    return d * ((q.x*c.y-q.y*c.x<0.0)?-1.0:1.0);
}

float pPlane(vec3 normal, float dist, vec3 p)
{
     return dot(normal, p) - dist;
}

float pHexPrism(float h, float r, vec3 p)
{
    const vec3 k = vec3(-0.8660254, 0.5, 0.57735);
    p = abs(p);
    p.xy -= 2.0*min(dot(k.xy, p.xy), 0.0)*k.xy;
    vec2 d = vec2(
            length(p.xy-vec2(clamp(p.x,-k.z*r,k.z*r), r))*sign(p.y-r),
            p.z-h);
    return min(max(d.x,d.y),0.0) + length(max(d,0.0));
}

// bound
float pTriPrism(float h, float r, vec3 p)
{
    vec3 q = abs(p);
    return max(q.z-h,max(q.x*0.866025+p.y*0.5,-p.y)-r*0.5);
}

float pCapsule(float r, float h, vec3 p)
{
    p.y -= clamp( p.y, 0.0, h );
    return length( p ) - r;
}

float pCylinder(float r, float h, vec3 p)
{
    vec2 d = abs(vec2(length(p.xz), p.y)) - vec2(r, h);
    return min(max(d.x, d.y), 0.0) + length(max(d, 0.0));
}

float pCappedCone(float h, float r1, float r2, vec3 p)
{
    vec2 q = vec2( length(p.xz), p.y );
    vec2 k1 = vec2(r2,h);
    vec2 k2 = vec2(r2-r1,2.0*h);
    vec2 ca = vec2(q.x-min(q.x,(q.y<0.0)?r1:r2), abs(q.y)-h);
    vec2 cb = q - k1 + k2*clamp( dot(k1-q,k2)/dot(k2,k2), 0.0, 1.0 );
    float s = (cb.x<0.0 && ca.y<0.0) ? -1.0 : 1.0;
    return s*sqrt( min(dot(ca,ca),dot(cb,cb)) );
}

float pSolidAngle(vec2 c, float r, vec3 p)
{
    // c is the sin/cos of the angle
    vec2 q = vec2( length(p.xz), p.y );
    float l = length(q) - r;
    float m = length(q - c*clamp(dot(q,c),0.0,r) );
    return max(l,m*sign(c.y*q.x-c.x*q.y));
}

float pRoundCone(float r1, float r2, float h, vec3 p)
{
    vec2 q = vec2( length(p.xz), p.y );

    float b = (r1-r2)/h;
    float a = sqrt(1.0-b*b);
    float k = dot(q,vec2(-b,a));

    if( k < 0.0 ) return length(q) - r1;
    if( k > a*h ) return length(q-vec2(0.0,h)) - r2;

    return dot(q, vec2(a,b) ) - r1;
}

// bound
float pEllipsoid(vec3 r, vec3 p)
{
    float k0 = length(p/r);
    float k1 = length(p/(r*r));
    return k0*(k0-1.0)/k1;
}

float pOctahedron(float s, vec3 p)
{
    p = abs(p);
    float m = p.x+p.y+p.z-s;
    vec3 q;
            if( 3.0*p.x < m ) q = p.xyz;
    else if( 3.0*p.y < m ) q = p.yzx;
    else if( 3.0*p.z < m ) q = p.zxy;
    else return m*0.57735027;

    float k = clamp(0.5*(q.z-q.y+s),0.0,s);
    return length(vec3(q.x,q.y-s+k,q.z-k));

    // bound
    // p = abs(p);
    // return (p.x+p.y+p.z-s)*0.57735027;
}

float pPyramid(float h, vec3 p)
{
    float m2 = h*h + 0.25;

    p.xz = abs(p.xz);
    p.xz = (p.z>p.x) ? p.zx : p.xz;
    p.xz -= 0.5;

    vec3 q = vec3( p.z, h*p.y - 0.5*p.x, h*p.x + 0.5*p.y);

    float s = max(-q.x,0.0);
    float t = clamp( (q.y-0.5*p.z)/(m2+0.25), 0.0, 1.0 );

    float a = m2*(q.x+s)*(q.x+s) + q.y*q.y;
    float b = m2*(q.x+0.5*t)*(q.x+0.5*t) + (q.y-m2*t)*(q.y-m2*t);

    float d2 = min(q.y,-q.x*m2-q.y*0.5) > 0.0 ? 0.0 : min(a,b);

    return sqrt( (d2+q.z*q.z)/m2 ) * sign(max(q.z,-p.y));
}

vec3 mTranslation(vec3 inv_translation, vec3 p)
{
    return p + inv_translation;
}

vec3 mRotation(mat3 inv_rotation, vec3 p)
{
    return inv_rotation * p;
}

vec3 mMirror(vec3 normal, float dist, vec3 p)
{
    float d = max(0.0, dot(normal, p) - dist);
    return p - 2.0 * d * normal;
}

vec3 mRepInf(vec3 cell_size, vec3 p)
{
    vec3 inv_cell_size = vec3(greaterThan(cell_size, vec3(0.0))) * 1.0 / cell_size;
    return p - cell_size * round(p * inv_cell_size);
}

vec3 mRepLim(vec3 cell_size, vec3 grid_size, vec3 p)
{
    return p - cell_size * clamp(round(p / cell_size), -grid_size, grid_size);
}

vec3 mElongation(vec3 elongation, vec3 p)
{
    return p - clamp(p, -elongation, elongation);
}

float oUnion(float d1, float d2)
{
    return min(d1, d2);
}

float oSubtraction(float d1, float d2)
{
    return max(d1, -d2);
}

float oIntersection(float d1, float d2)
{
    return max(d1, d2);
}

float oOnion(float thickness, float d)
{
    return abs(d) - thickness;
}

float oThicken(float thickness, float d)
{
    return d - thickness;
}

float oSmoothUnion(float k, float d1, float d2)
{
    float h = clamp(0.5 + 0.5*(d1 - d2) / k, 0.0, 1.0);
    return mix(d1, d2, h) - k*h*(1.0-h);
}

float oSmoothSubtraction(float k, float d1, float d2)
{
    float h = clamp(0.5 - 0.5*(d1 + d2) / k, 0.0, 1.0);
    return mix(d1, -d2, h) + k*h*(1.0-h);
}

float oSmoothIntersection(float k, float d1, float d2)
{
    float h = clamp(0.5 - 0.5*(d1 - d2) / k, 0.0, 1.0);
    return mix(d1, d2, h) + k*h*(1.0-h);
}
//-----------------------------------------------------------------

float sdf(vec3 p0)
{
	float d1;
	float d2;
	float d3;

	{
		vec3 p1 = mRotation(RoIn_1, p0);
		{
			vec3 p2 = mTranslation(TrIn_2, p1);
			d1 = pTorus(ToRa_3, ToRa_4, p2);
		}
	}
	{
		vec3 p1 = mTranslation(TrIn_5, p0);
		d2 = pPlane(PlNo_6, PlDi_7, p1);
	}
	d3 = pLink(LiLe_8, LiRa_9, LiRa_10, p0);
	return oUnion(d1, oUnion(d2, d3));
}
//-------------------------------------------------------------
//Distance Field function by iq :
//http://iquilezles.org/www/articles/distfunctions/distfunctions.htm
float sdSphere(vec3 p, float s)
{
  return length(p) - s;
}

float sdEllipsoid( in vec3 p, in vec3 r) 
{
    return (length(p/r ) - 1.) * min(min(r.x,r.y),r.z);
}

vec3 opRep( vec3 p, vec3 c )
{
    return mod(p,c)-0.5*c;
}

float smin( float a, float b, float k )
{
    float h = clamp( 0.5+0.5*(b-a)/k, 0.0, 1.0 );
    return mix( b, a, h ) - k*h*(1.0-h);
}

//taken from shane's desert canyon, originaly a modification of the smin function by iq
//https://www.shadertoy.com/view/Xs33Df
float smax(float a, float b, float s)
{   
    float h = clamp( 0.5 + 0.5*(a-b)/s, 0., 1.);
    return mix(b, a, h) + h*(1.0-h)*s;
}

mat2 Rot(float a) 
{
    vec2 s = sin(vec2(a, a + pi/2.0));
    return mat2(s.y,s.x,-s.x,s.y);
}

//float oUnion(float d1, float d2)
//{
//    return min(d1, d2);
//}

vec3 TransformPosition(vec3 pos)
{
    pos.yz *= Rot((pos.z + 2.0)*sin(iTime*0.3)*0.2);
    pos.xy *= Rot(pos.z*sin(iTime*0.1)*0.25);
    pos.y -= 0.5 + sin(iTime*0.5)*0.2; 
    
    return pos;
}


vec3 RayMarch(vec3 rayDir, vec3 cameraOrigin)
{
    const int maxItter = 128;
    const float maxDist = 30.0;
    
    float totalDist = 0.0;
    vec3 pos = cameraOrigin;
    float dist = epsilon;
    float itter = 0.0;
    
    for(int i = 0; i < maxItter; i++)
    {
        dist = sdf(pos);
        itter += 1.0;
        totalDist += dist; 
        pos += dist * rayDir;
        
        if(dist < epsilon || totalDist > maxDist)
        {
            break;
        }
    }
    
    return vec3(dist, totalDist, itter/128.0);
}

float AO(vec3 pos, vec3 n)
{
    float res = 0.0;
    vec3 aopos = pos;
    
    for( int i=0; i<3; i++ )
    {   
        aopos = pos + n*0.2*float(i);
        float d = sdf(aopos);
        res += d;
    }

    return clamp(res, 0.0, 1.0);   
}


//Camera Function by iq :
//https://www.shadertoy.com/view/Xds3zN
mat3 SetCamera( in vec3 ro, in vec3 ta, float cr )
{
    vec3 cw = normalize(ta-ro);
    vec3 cp = vec3(sin(cr), cos(cr), 0.0);
    vec3 cu = normalize( cross(cw,cp) );
    vec3 cv = normalize( cross(cu,cw) );
    return mat3( cu, cv, cw );
}

//Normal and Curvature Function by Nimitz;
//https://www.shadertoy.com/view/Xts3WM
vec4 NorCurv(in vec3 p)
{
    vec2 e = vec2(-epsilon, epsilon);   
    float t1 = sdf(p + e.yxx), t2 = sdf(p + e.xxy);
    float t3 = sdf(p + e.xyx), t4 = sdf(p + e.yyy);

    float curv = .25/e.y*(t1 + t2 + t3 + t4 - 4.0 * sdf(p));
    return vec4(normalize(e.yxx*t1 + e.xxy*t2 + e.xyx*t3 + e.yyy*t4), curv);
}

vec3 Lighting(vec3 n, vec3 rayDir, vec3 reflectDir, vec3 pos)
{
    float diff = max(0.0, dot(LIGHT, n));
    float spec = pow(max(0.0, dot(reflectDir, LIGHT)), 10.0);
    float rim = (1.0 - max(0.0, dot(-n, rayDir)));

    return vec3(diff, spec, rim)*0.5; 
}

float TriplanarTexture(vec3 pos, vec3 n)
{
    return 0.0; 
}

float BackGround(vec3 rayDir)
{
    float sun = smoothstep(1.0, 0.0, clamp(length(rayDir - LIGHT), 0.0, 1.0));
    
    return sun*0.5;
}

void mainImage( out vec4 fragColor, in vec2 fragCoord )
{
    vec2 uv = fragCoord.xy/iResolution.xy;
    
    vec3 cameraOrigin = vec3(0.0, 0.0, 0.0);
    
    if(iMouse.z > 0.0)
    {
        cameraOrigin.x = sin(iMouse.x*0.01) * 5.0;
        cameraOrigin.y = iMouse.y*0.05 - 10.0;
        cameraOrigin.z = cos(iMouse.x*0.01) * 5.0;  
    }
    else    
    {
        cameraOrigin.x = sin(iTime*0.25 + 2.0) * (6.0 + sin(iTime * 0.1));
        cameraOrigin.y = sin(iTime*0.3) - 0.5;
        cameraOrigin.z = cos(iTime*0.25 + 2.0) * (6.0 + sin(iTime * 0.15)) ; 
    }
    
    vec3 cameraTarget = vec3(0.0, 0.25, -1.0);
    
    vec2 screenPos = uv * 2.0 - 1.0;
    
    screenPos.x *= iResolution.x/iResolution.y;
    
    mat3 cam = SetCamera(cameraOrigin, cameraTarget, sin(iTime*0.15)*0.5);
    
    vec3 rayDir = cam*normalize(vec3(screenPos.xy,2.0));
    vec3 dist = RayMarch(rayDir, cameraOrigin);
    
    float res;
    float backGround = BackGround(rayDir);
    
    if(dist.x < epsilon)
    {
        vec3 pos = cameraOrigin + dist.y*rayDir;
        vec4 n = NorCurv(pos);
        float ao = AO(pos, n.xyz);
        vec3 r = reflect(rayDir, n.xyz);
        vec3 l = Lighting(n.xyz, rayDir, r, pos);
        
        float col = TriplanarTexture(pos, n.xyz);
        col *= n.w*0.5+0.5;
        col *= ao;
        col += ao * (l.x + l.y);
        col += l.z*0.75;
        col += BackGround(n.xyz)*0.25;

        res = col;
    }
    else
    {
        res = backGround; 
    }
    
    fragColor = vec4(vec3(res), 1.0);
}
// --------[ Original ShaderToy ends here ]---------- //
