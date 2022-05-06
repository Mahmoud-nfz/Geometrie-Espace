#espace
def vecteur(A,B) :
    return [B[0]-A[0],B[1]-A[1],B[2]-A[2]]
def scalaire(A,B,C,D):
    A_B=vecteur(A, B)
    C_D=vecteur(C,D)
    A_BxC_D = (A_B[0]*C_D[0]) + (A_B[1]*C_D[1]) + (A_B[2]*C_D[2])
    return A_BxC_D
def scalaire_vec(u,v):
    return (u[0]*v[0]) + (u[1]*v[1]) + (u[2]*v[2])
def vectoriel_vec(u,v):
    return [u[1]*v[2]-u[2]*v[1],-(u[0]*v[2]-u[2]*v[0]),u[0]*v[1]-u[1]*v[0]]
def vectoriel(A,B,C,D):
    A_B=vecteur(A,B)
    C_D=vecteur(C,D)
    u=[]
    u.append(A_B[1]*C_D[2]-A_B[2]*C_D[1])
    u.append(-(A_B[0]*C_D[2]-A_B[2]*C_D[0]))
    u.append(A_B[0]*C_D[1]-A_B[1]*C_D[0])
    return u
def norme(A,B):
    from math import sqrt
    A_B=vecteur(A,B)
    return sqrt(A_B[0]**2+A_B[1]**2+A_B[2]**2)
def determinant(A,B,C,D,E,F):
    return scalaire_vec(vectoriel(A,B,C,D),vecteur(E,F))
def determinant_vec(u,v,w):
    return scalaire_vec(vectoriel_vec(u,v),w)
def aire_triangle(A,B,C):
    u=vectoriel(A, B, A, C)
    return 0.5*((u[0]**2+u[1]**2+u[2]**2)**0.5)
def aire_parallelo(A,B,C,D):
    u=vectoriel(A, B, A, D)
    return (u[0]**2+u[1]**2+u[2]**2)**0.5
def volume_tetraedre(A,B,C,D):
    return (1/6)*abs(scalaire_vec(vectoriel(B,C,B,D),vecteur(B,A)))
def volume_paralleli(A,B,C,D,E,F,G,H):
    return abs(scalaire_vec(vectoriel(A,B,A,D),vecteur(A,E)))
def dpp(A,Q):
    return (abs(A[0]*Q[0]+A[1]*Q[1]+A[2]*Q[2]+Q[3]))/((Q[0]**2+Q[1]**2+Q[2]**2)**0.5)
def str_to_eqplan(ch):
    """requires valid string"""
    q=[]
    k=0
    if ch[0].isalpha:ch="1"+ch
    if ch[0]=="-" and ch[1].isalpha:ch="-1"+ch[1:]
    for i in ["x","y","z"]:
        if i in ch:
            if k!=0 and ch.index(i)-k==1: ch=ch[:k+1] +"1"+ ch[k+1:]
            q.append(float(ch[k:ch.index(i)]))
            k=ch.index(i)+1
        else:
            q.append(0)
    d=ch[k:ch.index("=")]
    if d!="" : q.append(float(d))
    else : q.append(0)
    return q
def eqplan_list(A,B,C):
    u=vectoriel(A,B,A,C)
    d=-(u[0]*A[0]+u[1]*A[1]+u[2]*A[2])
    return [u[0],u[1],u[2],d]
def eqplan(A,B,C):
    s=""
    u=vectoriel(A,B,A,C)
    d=-(u[0]*A[0]+u[1]*A[1]+u[2]*A[2])
    if u[0]!=0:
        s+=str("%.3f" % u[0])+"x "
    if u[1]!=0:
        if u[1]>0:s+="+"+str("%.3f" % u[1])+"y "
        if u[1]<0:s+=str("%.3f" % u[1])+"y "
    if u[2]!=0:
        if u[2]>0:s+="+"+str("%.3f" % u[2])+"z "
        if u[2]<0:s+=str("%.3f" % u[2])+"z "
    if d!=0:
        s+=str(d)+" "
    s+="= 0"
    return s
