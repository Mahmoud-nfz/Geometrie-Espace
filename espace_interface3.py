import os,sys
from tkinter import *
from espace import*
import tkinter.font
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
icon= resource_path("space_icon.ico")
balls = resource_path("balls.gif")
root = Tk()
root.iconbitmap(icon)
root.title("Espace")
root.resizable(False, False)
root.configure(background='#242222')
fonts=[x.lower() for x in list(tkinter.font.families())]
if "bahnschrift condensed" in fonts:
    myFont = tkinter.font.Font(family="bahnschrift condensed",size=20)
    myFont1 = tkinter.font.Font(family="bahnschrift condensed",size=12)
else:
    myFont = tkinter.font.Font(family="gabriola",size=20)
    myFont1 = tkinter.font.Font(family="gabriola",size=12)
if 'esenin script one' in fonts:
    myFont2 = tkinter.font.Font(family='Esenin script One',size=20)
elif 'edwardian script itc' in fonts:
    myFont2 = tkinter.font.Font(family='Edwardian Script ITC',size=20)
else:
    myFont2 = tkinter.font.Font(family='Microsoft Uighur',size=20)
frames = [PhotoImage(file=balls,format = 'gif -index %i' %(i)) for i in range(10)]
    
plans={}
points={}
vecteurs={}
fake=Label(root)
current_w=fake
def update(ind):
    frame = frames[ind]
    ind += 1
    if ind ==10 : ind=0
    gif.configure(image=frame)
    root.after(35, update, ind)
def print_inventory(dct):
    ch=""
    for item, amount in dct.items():
        ch+="{} ({})\n".format(item, amount)
    return ch+"Mahmoud Nefzi"
def labelup1():
    if len(nom.get())==1:
        alfa="Veuillez saisir\nles coordonnées \nde "+nom.get()
        ajout_prompt_c["text"]=alfa
        return True
    else: return False
def labelup2():
    if nom_m.get() in points:
        alfa=f"Veuillez mettre\nles coordonnées de\n{nom_m.get()} à jour"
        return True
        mod_prompt_c.config(text=alfa)
    else: return False
def labelup3():
    alfa=f"Veuillez saisir\nl'equation de\nde {nom_plan.get()} ou 3 pts\nqui lui appartiennent"
    ajout_plan_prompt_c["text"]=alfa
    return True
def labelup4():
    alfa=f"Veuillez saisir\nles composants\nde {nom_vec_ajout.get()}"
    ajout_vec_prompt_c["text"]=alfa
    return True
def stick(objet,r,c,rs,cs,ipy,ipx):
    global current_w
    if current_w!=objet:
        current_w.grid_remove()
        objet.grid(row=r,column=c,rowspan=rs,columnspan=cs,ipady=ipy,ipadx=ipx)
        current_w=objet
    else :
        objet.grid_remove()
        current_w=fake
def ajout_plan():
    global current_w
    current_w.grid_remove()
    group_plan["text"]="Ajouter un plan"
    ajout_plan_prompt_n["text"]="Veuillez saisir un\nnom pour ce plan"
    button_plan["text"]="Ajouter"
    group_plan.grid(row=80, column= 152,rowspan=400,columnspan=400,ipady=10,ipadx=5)
    current_w=group_plan
def mod_plan():
    global current_w
    current_w.grid_remove()
    group_plan["text"]="Modifier un plan"
    ajout_plan_prompt_n["text"]="Veuillez saisir le\nnom du plan"
    button_plan["text"]="Modifier"
    group_plan.grid(row=100, column= 152,rowspan=400,columnspan=400,ipady=10,ipadx=5)
    current_w=group_plan
def ajout_vecteur():
    global current_w
    current_w.grid_remove()
    group_vec_ajout["text"]="Ajouter un Vecteur"
    ajout_vec_prompt_n["text"]="Veuillez saisir un\nnom pour ce vecteur"
    button_vec_ajout["text"]="Ajouter"
    button_vec_ajout["command"]=insert_vec
    group_vec_ajout.grid(row=130, column= 115,rowspan=400,columnspan=400,ipady=10,ipadx=5)
    current_w=group_vec_ajout
def mod_vecteur():
    global current_w
    current_w.grid_remove()
    group_vec_ajout["text"]="Modifier un Vecteur"
    ajout_vec_prompt_n["text"]="Veuillez saisir le\nnom de ce vecteur"
    button_vec_ajout["text"]="Modifier"
    button_vec_ajout["command"]=mod_vec
    group_vec_ajout.grid(row=130, column= 110,rowspan=400,columnspan=400,ipady=10,ipadx=5)
    current_w=group_vec_ajout
    
        
    
def verif(ch,n):
    a=True
    y=ch.split(" ")
    a=len(y)==3
    if a :
        for i in y :
            try : float(i)
            except ValueError : a=False
    else:
        if n==1 :coord.delete(0, END)
        if n==2 :coord_m.delete(0,END)
        if n==3 :c_vec_ajout.delete(0,END)
    return a
def verif_plan(ch):
    if "=" in ch :
        alfas=''.join(filter(str.isalpha, ch))
        t=["x","xy","xz","xyz","y","yz","z"]
        return alfas in t
    else: return False
def insert():
    global points
    if verif(coord.get().strip(" "),1):
        if nom.get()!="":
            if len(nom.get())==1:
                if [float(i) for i in coord.get().strip().split(" ")] in points.values():
                    coord.delete(0, END)
                    coord.insert(0,"ce point est déja pris")
                elif nom.get() in points :
                    nom.delete(0, END)
                    nom.insert(0,"ce nom existe déja")
                else: 
                    points[nom.get()]=[float(i) for i in coord.get().strip().split(" ")]
                    nom.delete(0, END)
                    coord.delete(0, END)
                    points_aff["text"]= print_inventory(points)
                    ajout_prompt_c.config(text="Veuillez saisir\nles coordonnées \nde ce point")
            else:
                nom.delete(0, END)
                nom.insert(0,"1 charactere max")
        else : nom.insert(0,"name cannot be blank")
    else :
        coord.delete(0, END)
        coord.insert(0,"cordonnées invalides")
def supprimer():
    global points
    ch=nom_s.get()
    if ch not in points :
        nom_s.delete(0,END)
        nom_s.insert(0,"Ce nom n'est pas disponible")
    else:
        nom_s.delete(0,END)
        nom_s.insert(0,"Point supprimé")
        del points[ch]
        points_aff["text"]= print_inventory(points)
def modifier():
    global points
    if nom_m.get() in points :
        if verif(coord_m.get(),2):
            if [float(i) for i in coord_m.get().strip().split(" ")] in points.values():
                coord_m.delete(0, END)
                coord_m.insert(0,"ce point est déja pris")
            else:
                points[nom_m.get()]=[float(i) for i in coord_m.get().strip().split(" ")]
                nom_m.delete(0, END)
                coord_m.delete(0, END)
                points_aff["text"]= print_inventory(points)
                mod_prompt_c.config(text="Veuillez saisir\nles coordonnées \nde ce point")
        else : coord_m.delete(0, END)
    else:
        nom_m.delete(0,END)
        nom_m.insert(0,"Ce point n'est pas disponible")
        mod_prompt_c.config(text="Veuillez saisir\nles coordonnées \nde ce point")
def findeq():
    global points
    ch=plan_name.get().replace(" ","")
    if len(ch)!=3:
        p_help.config(text="vous n'avez pas\nentré 3 points")
    else:
        if ch[0] in points and ch[1] in points and ch[2] in points:
            ch+=" : "+eqplan(points[ch[0]],points[ch[1]],points[ch[2]])
            p_help.config(text=ch)
        else:
            p_help.config(text="vous n'avez pas\nentré 3 points valables")
def insert_plan():
    global plans
    ch=eq_plan.get().replace(" ","")
    if "=" in ch :
        ch=ch.lower()
        if verif_plan(ch):
            if nom_plan.get()!="":
                plans[nom_plan.get()]=str_to_eqplan(ch)
                nom_plan.delete(0,END)
                eq_plan.delete(0,END)
            else: nom_plan.insert(0,"name cannot be blank")
        else:
            eq_plan.delete(0,END)
            eq_plan.insert(0,"equation invalide")
    else:
        if len(ch)==3 and ch[0] in points and ch[1] in points and ch[2] in points:
            plans[nom_plan.get()]=eqplan_list(points[ch[0]],points[ch[1]],points[ch[2]])
            nom_plan.delete(0,END)
            eq_plan.delete(0,END)
        else :
            plan_e.delete(0,END)
            plan_e.insert(0,"nom incorrect")
def delete_plan():
    global plans
    if nom_s_plan.get() in plans :
        del plans[nom_s_plan.get()]
        nom_s_plan.delete(0,END)
        nom_s_plan.insert(0,"plan supprimé")
    else:
        nom_s_plan.delete(0,END)
        nom_s_plan.insert(0,"plan non valable")
def distance_1():
    global points
    ch=droite.get().replace(" ","")
    if len(ch)!=2:
        d_help.config(text="2 points")
    else:
        if ch[0] in points and ch[1] in points:
            ch+=" = "+str("%.3f" % norme(points[ch[0]],points[ch[1]]))
            d_help.config(text=ch)
        else:
            d_help.config(text="points non valables")
def distance_2():
    global points,plans
    pt=point_e.get()
    pl=plan_e.get()
    if pt not in points :
        point_e.insert(0,"point non valable")
    else:
        if "=" in pl :
            if verif_plan(pl):
                d2_help["text"]="d("+pt+","+pl+")= "+str("%.3f" % dpp(points[pt],str_to_eqplan(pl)))
                nom_plan.delete(0,END)
                eq_plan.delete(0,END)
            else:
                eq_plan.delete(0,END)
                eq_plan.insert(0,"equation invalide")
        else:
            if len(pl)==3 and pl[0] in points and pl[1] in points and pl[2] in points:
                d2_help["text"]="d("+pt+","+pl+")= "+str("%.3f" % dpp(points[pt],eqplan_list(points[pl[0]],points[pl[1]],points[pl[2]])))
            elif pl in plans:
                d2_help["text"]="d("+pt+","+pl+")= "+str("%.3f" % dpp(points[pt],plans[pl]))  
            else :
                plan_e.delete(0,END)
                plan_e.insert(0,"nom incorrect")  
def insert_vec():
    global vecteurs
    if len(nom_vec_ajout.get()) != 1 :
        nom_vec_ajout.delete(0,END)
        nom_vec_ajout.insert(0,"1 char")
    else:
        if verif(c_vec_ajout.get().strip(" "),3):
            if nom_vec_ajout.get() in vecteurs:
                nom_vec_ajout.delete(0,END)
                nom_vec_ajout.insert(0,"ce nom est pris")
            else:
                vecteurs[nom_vec_ajout.get()]=[float(i) for i in c_vec_ajout.get().strip(" ").split(" ")]
                nom_vec_ajout.delete(0,END)
                c_vec_ajout.delete(0,END)
        else:
            c_vec_ajout.delete(0,END)
            c_vec_ajout.insert(0,"composants invalides")
def mod_vec():
    global vecteurs
    if verif(c_vec_ajout.get().strip(" "),3):
        if nom_vec_ajout.get() in vecteurs:
            vecteurs[nom_vec_ajout.get()]=[float(i) for i in c_vec_ajout.get().strip(" ").split(" ")]
            nom_vec_ajout.delete(0,END)
            nom_vec_ajout.insert(0,"point modifié")
        else:
          nom_vec_ajout.delete(0,END)
          nom_vec_ajout.insert(0,"point non valable")  
    else:
        c_vec_ajout.delete(0,END)
        c_vec_ajout.insert(0,"composants invalides")
def supp_vec():
    if nom_s_vec.get() in vecteurs:
        del vecteurs[nom_s_vec.get()]
        nom_s_vec.delete(0,END)
        nom_s_vec.insert(0,"vecteur supprimé")
def find_c_vec():
    global points
    ch=pts_vec.get()
    if len(ch)==2 and ch[0]in points and ch[1] in points :
        t=["%.3f" % i for i in vecteur(points[ch[0]],points[ch[1]])]
        vec_res["text"]=f" ( {t[0]} )\n(  {t[1]}  )\n ( {t[2]} )"
    else:
        pts_vec.delete(0,END)
        pts_vec.insert(0,"points invalides")
def extract23(v1,v2,v3,n):
    global points,vecteurs
    a1=a2=a3=False
    if v1 in vecteurs :
        a=vecteurs[v1]
        a1=True
    else: 
        if len(v1)==2 and v1[0]in points and v1[1]in points:
            a=vecteur(points[v1[0]],points[v1[1]])
            a1=True
        else :
            if n==1:
                sc_vec1.delete(0,END)
                sc_vec1.insert(0,"vecteur non valable")
            if n==2:
                ve_vec1.delete(0,END)
                ve_vec1.insert(0,"vecteur non valable")
            if n==3:
                det_vec1.delete(0,END)
                det_vec1.insert(0,"vecteur non valable")
    if v2 in vecteurs :
        b=vecteurs[v2]
        a2=True
    else: 
        if len(v2)==2 and v2[0]in points and v2[1]in points:
            b=vecteur(points[v2[0]],points[v2[1]])
            a2=True
        else :
            if n==1:
                sc_vec2.delete(0,END)
                sc_vec2.insert(0,"vecteur non valable")
            if n==2:
                ve_vec2.delete(0,END)
                ve_vec2.insert(0,"vecteur non valable")
            if n==3:
                det_vec2.delete(0,END)
                det_vec2.insert(0,"vecteur non valable")
    if n==3:
        if v3 in vecteurs :
            c=vecteurs[v3]
            a3=True
        else: 
            if len(v3)==2 and v3[0]in points and v3[1]in points:
                c=vecteur(points[v3[0]],points[v3[1]])
                a3=True
            else :
                det_vec3.delete(0,END)
                det_vec3.insert(0,"vecteur non valable")
    if a1 and a2:
        if n==1 :sc_res["text"]="= "+"%.3f" % scalaire_vec(a,b)
        if n==2 :
            t=["%.3f" % i for i in vectoriel_vec(a,b)]
            ve_res["text"]=f" ( {t[0]} )\n=(  {t[1]}  )\n ( {t[2]} ) "
        if n==3 and a3:
            det_res["text"]=f") = "+"%.3f" % determinant_vec(a,b,c)
def calc_aire1():
    ch=triangle.get().replace(" ","")
    if len(ch)==3:
        if all (k in points for k in ch):
            tri_help["text"]=f"Aire({ch}) = "+"%.3f" % aire_triangle(points[ch[0]],points[ch[1]],points[ch[2]])
        else:
           triangle.delete(0,END)
           triangle.insert(0,"pts non valables") 
    else :
        triangle.delete(0,END)
        triangle.insert(0,"3 pts")
def calc_aire2():
    ch=para.get().replace(" ","")
    if len(ch)==4:
        if all (k in points for k in ch):
            para_help["text"]=f"Aire({ch}) = "+"%.3f" % aire_parallelo(points[ch[0]],points[ch[1]],0,points[ch[3]])
        else:
           para.delete(0,END)
           para.insert(0,"pts non valables") 
    else :
        para.delete(0,END)
        para.insert(0,"4 pts")
def calc_vol1():
    ch=tetra.get().replace(" ","")
    if len(ch)==4:
        if all (k in points for k in ch):
            tetra_help["text"]=f"Volume({ch}) = "+"%.3f" % volume_tetraedre(points[ch[0]],points[ch[1]],points[ch[2]],points[ch[3]])
        else:
           tetra.delete(0,END)
           tetra.insert(0,"pts non valables") 
    else :
        tetra.delete(0,END)
        tetra.insert(0,"4 pts")
def calc_vol2():
    ch=vpara.get().replace(" ","")
    if len(ch)==8:
        if all (k in points for k in ch):
            vpara_help["text"]=f"Volume({ch}) = "+"%.3f" % volume_paralleli(points[ch[0]],points[ch[1]],0,points[ch[3]],points[ch[4]],0,0,0)
        else:
           vpara.delete(0,END)
           vpara.insert(0,"pts non valables") 
    else :
        vpara.delete(0,END)
        vpara.insert(0,"8 pts")
def upstates():
    global points,buttons,plans,vecteurs
    button_1["state"]="normal"
    button_4["state"]="normal"
    if len(vecteurs)<1:
        modifier_vecteur["state"]="disabled"
        supprimer_vecteur["state"]="disabled"
    else:
        modifier_vecteur["state"]="normal"
        supprimer_vecteur["state"]="normal"
    if len(plans)<1:
        modifier_plan["state"]="disabled"
        supprimer_plan["state"]="disabled"
    else:
        modifier_plan["state"]="normal"
        supprimer_plan["state"]="normal"
    if len(points)<1:
        button_101["state"]="disabled"
        for i in buttons[1:3]:
            i["state"]="disabled"
    else :
        button_2["state"]="normal"
        button_3["state"]="normal"
        button_101["state"]="normal"
    if len(points)<2 :
        trouver_cvecteur["state"]="disabled"
    else :
        trouver_cvecteur["state"]="normal"
        button_6["state"]="normal"
    if len(points)<3:
        button_10["state"]="disabled"
    else :
        trouver_eqplan["state"]="normal"
        button_10["state"]="normal"
    if len(points)<4:
        aire_para["state"]="disabled"
        button_11["state"]="disabled"
    else:
        aire_para["state"]="normal"
        button_11["state"]="normal"
    if len(points)<8:
        volume_p["state"]="disabled"
    else:
        volume_p["state"]="normal"
    if len(points)+len(vecteurs)<3 and len(vecteurs)<2:
        button_7["state"]="disabled"
        button_8["state"]="disabled"
    else :
        button_7["state"]="normal"
        button_8["state"]="normal"
    if len(points)+len(vecteurs)<4 and len(vecteurs)<3:
        button_9["state"]="disabled"
    else :
        button_9["state"]="normal"
    if len(points)+len(plans)<2:
        button_5["state"]="disabled"
    else:
        button_5["state"]="normal"
        

root.after(0, update, 0)
gif = Label(root)
gif.configure(background='#242222')
gif.grid(row=0,column=200,columnspan=500,rowspan=700)
#ajout
group_ajout = LabelFrame(root,text="Ajouter un point",relief="raised",bg="#BADA55",font=myFont2,fg="white")
nom=Entry(group_ajout,width=7,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",
          validate="focusout",validatecommand=lambda:labelup1(),font=myFont1)
coord=Entry(group_ajout,width=16,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",
            validate="focusout",validatecommand=lambda:verif(coord.get(),1),font=myFont1)
ajout_prompt_n=Label(group_ajout,text=f"Veuillez saisir un\nnom pour ce point",bg="#BADA55",font=myFont2)
ajout_prompt_c=Label(group_ajout,text=f"Veuillez saisir\nles coordonnées \nde ce point",bg="#BADA55",font=myFont2)
ajout_prompt_help=Label(group_ajout,text="exemple : 77.6572 77.7985 -68",bg="#2b2b2b",fg="white",font=myFont1)
button_ajout = Button(group_ajout, text="Ajouter",takefocus="",font=myFont,
                  command=insert,bg="#005668",fg="white",activebackground="#0a4753")
nom.grid(row=6,column=10,columnspan=1)
coord.grid(row=9,column=9,columnspan=3 )
button_ajout.grid(row=10,column=9,columnspan=3,rowspan=1)
ajout_prompt_n.grid(row=6,column=7)
ajout_prompt_c.grid(row=9,column=7)
ajout_prompt_help.grid(row=10,column=7)
#supprimer
group_supp = LabelFrame(root,text="Supprimer un point",relief="raised",bg="#BADA55",font=myFont2,fg="white")
nom_s=Entry(group_supp,width=15,bg="#657478",fg="white",relief="flat",justify="center",font=myFont1)
supp_prompt=Label(group_supp,text=f"Veuillez saisir le\nnom du point",bg="#BADA55",font=myFont2)
button_supp = Button(group_supp, text="Supprimer",takefocus="",font=myFont,width=17,
                  command=supprimer,bg="#005668",fg="white",activebackground="#0a4753")
supp_prompt.grid(row=2,column=2,columnspan=4)
nom_s.grid(row=2,column=6,columnspan=5)
button_supp.grid(row=5,column=3,columnspan=6,rowspan=1)
#modifier
group_mod = LabelFrame(root,text="Modifier un point",relief="raised",bg="#BADA55",font=myFont2,fg="white")
nom_m=Entry(group_mod,width=7,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",
          validate="focusout",validatecommand=lambda :labelup2(),font=myFont1)
coord_m=Entry(group_mod,width=16,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",
            validate="focusout",validatecommand=lambda:verif(coord_m.get(),2),font=myFont1)
mod_prompt_n=Label(group_mod,text=f"Veuillez saisir le\nnom du point",bg="#BADA55",font=myFont2)
mod_prompt_c=Label(group_mod,text=f"Veuillez mettre\nses coordonnées\nà jour",bg="#BADA55",font=myFont2)
button_mod = Button(group_mod, text="Modifier",takefocus="",font=myFont,width=17,
                  command=modifier,bg="#005668",fg="white",activebackground="#0a4753")
nom_m.grid(row=6,column=10,columnspan=1)
coord_m.grid(row=9,column=9,columnspan=3 )
button_mod.grid(row=10,column=7,columnspan=6,rowspan=1)
mod_prompt_n.grid(row=6,column=7)
mod_prompt_c.grid(row=9,column=7)
#plans menu
plan_aff = Frame(root,relief="raised",bg="#BADA55")
ajouter_plan = Button(plan_aff, text="Ajouter un plan",takefocus="",font=myFont,width=20,state="normal",
                  command=ajout_plan,bg="#14836e",fg="white",activebackground="#147865")
modifier_plan = Button(plan_aff, text="Modifier un plan",takefocus="",font=myFont,width=20,state="disabled",
                  command=mod_plan,bg="#14836e",fg="white",activebackground="#147865")
supprimer_plan = Button(plan_aff, text="Supprimer un plan",takefocus="",font=myFont,width=20,state="disabled",
                  command=lambda:stick(group_supp_plan,55,105,400,400,10,5),bg="#14836e",fg="white",activebackground="#147865")
trouver_eqplan = Button(plan_aff, text="Trouver l'eq d'un plan",takefocus="",font=myFont,width=20,
                  command=lambda:stick(group_eq,105,105,300,400,5,0),bg="#14836e",fg="white",activebackground="#147865",state="disabled")
ajouter_plan.grid(row=5,column=3,columnspan=6,rowspan=1)
modifier_plan.grid(row=9,column=3,columnspan=6,rowspan=1)
supprimer_plan.grid(row=13,column=3,columnspan=6,rowspan=1)
trouver_eqplan.grid(row=17,column=3,columnspan=6,rowspan=1)
#equation d'un plan
group_eq = LabelFrame(root,text="Trouver une equation d'un plan",relief="raised",bg="#BADA55",font=myFont2,fg="white")

plan_name=Entry(group_eq,width=7,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",font=myFont1)
p_label=Label(group_eq,text=f"Veuillez choisir 3 points\nde ce plan",bg="#BADA55",font=myFont2)
p_help=Label(group_eq,text=f"exemple : ABC",bg="#BADA55",font=myFont1)
button_p = Button(group_eq, text="Trouver l'equation",takefocus="",font=myFont,width=17,
                  command=findeq,bg="#005668",fg="white",activebackground="#0a4753")
plan_name.grid(row=6,column=10,columnspan=1,rowspan=2)
button_p.grid(row=10,column=7,columnspan=6,rowspan=1)
p_label.grid(row=6,column=7)
p_help.grid(row=7,column=7)
#ajouter/modifier un plan
group_plan = LabelFrame(root,text="Ajouter un plan",relief="raised",bg="#BADA55",font=myFont2,fg="white")
nom_plan=Entry(group_plan,width=7,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",
          validate="focusout",validatecommand=lambda:labelup3(),font=myFont1)
eq_plan=Entry(group_plan,width=16,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",
            validate="focusout",font=myFont1)
ajout_plan_prompt_n=Label(group_plan,text=f"Veuillez saisir un\nnom pour ce plan",bg="#BADA55",font=myFont2)
ajout_plan_prompt_c=Label(group_plan,text=f"Veuillez saisir\nl'equation de\nde ce plan ou 3 pts\nqui lui appartiennent",
                          bg="#BADA55",font=myFont2)
ajout_plan_prompt_help=Label(group_plan,text="exemple : 77.65x-72.7779y-85z+68=0",bg="#2b2b2b",fg="white",font=myFont1)
button_plan = Button(group_plan, text="Ajouter",takefocus="",font=myFont,
                  command=insert_plan,bg="#005668",fg="white",activebackground="#0a4753")
nom_plan.grid(row=6,column=10,columnspan=1)
eq_plan.grid(row=9,column=9,columnspan=3 )
button_plan.grid(row=10,column=9,columnspan=3,rowspan=1)
ajout_plan_prompt_n.grid(row=6,column=7)
ajout_plan_prompt_c.grid(row=9,column=7)
ajout_plan_prompt_help.grid(row=10,column=7)
#supprimer un plan
group_supp_plan = LabelFrame(root,text="Supprimer un plan",relief="raised",bg="#BADA55",font=myFont2,fg="white")
nom_s_plan=Entry(group_supp_plan,width=15,bg="#657478",fg="white",relief="flat",justify="center",font=myFont1)
supp_prompt_plan=Label(group_supp_plan,text=f"Veuillez saisir le\nnom du plan",bg="#BADA55",font=myFont2)
button_supp_plan= Button(group_supp_plan, text="Supprimer",font=myFont,width=17,
                  command=delete_plan,bg="#005668",fg="white",activebackground="#0a4753")
supp_prompt_plan.grid(row=2,column=2,columnspan=4)
nom_s_plan.grid(row=2,column=6,columnspan=5)
button_supp_plan.grid(row=5,column=3,columnspan=6,rowspan=1)
#distances
distances = Frame(root,relief="raised",bg="#BADA55")
dpoint = Button(distances, text="Distance entre deux points",takefocus="",font=myFont,width=28,
                  command=lambda:stick(group_d1,160,120,300,400,10,0),bg="#14836e",fg="white",activebackground="#0a4753")
dplan = Button(distances, text="Distance entre un point et un plan",takefocus="",font=myFont,width=28,
                  command=lambda:stick(group_d2,160,215,300,400,10,10),bg="#14836e",fg="white",activebackground="#0a4753")
dpoint.grid(row=5,column=3,columnspan=6,rowspan=1)
dplan.grid(row=9,column=3,columnspan=6,rowspan=1)
#distance a un point
group_d1 = LabelFrame(root,text="Calculer la distance entre deux points",relief="raised",bg="#BADA55",font=myFont2,fg="white")

droite=Entry(group_d1,width=7,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",font=myFont1)
d_label=Label(group_d1,text=f"Veuillez choisir les deux points",bg="#BADA55",font=myFont2)
d_help=Label(group_d1,text=f"exemple : AB",bg="#BADA55",font=myFont1)
button_d1 = Button(group_d1, text="Calculer la distance",takefocus="",font=myFont,width=17,
                  command=distance_1,bg="#005668",fg="white",activebackground="#0a4753")
droite.grid(row=6,column=10,columnspan=1,rowspan=2)
button_d1.grid(row=10,column=7,columnspan=6,rowspan=1)
d_label.grid(row=6,column=7)
d_help.grid(row=7,column=7)
#distance a un plan
group_d2 = LabelFrame(root,text="Calculer la distance entre un point et un plan",relief="raised",bg="#BADA55",font=myFont2,fg="white")

point_e=Entry(group_d2,width=7,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",font=myFont1)
plan_e=Entry(group_d2,width=17,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",font=myFont1)
poe_label=Label(group_d2,text=f"Veuillez choisir le point",bg="#BADA55",font=myFont2)
ple_label=Label(group_d2,text=f"Veuillez choisir le plan",bg="#BADA55",font=myFont2)
d2_help=Label(group_d2,bg="#BADA55",font=myFont1,
              text=f"Vouz pouvez entrer l'equation\nou le nom d'un plan ou saisir 3 pts\nqui lui appartiennent")
button_d2 = Button(group_d2, text="Calculer",takefocus="",font=myFont,width=17,
                  command=distance_2,bg="#005668",fg="white",activebackground="#0a4753")
point_e.grid(row=6,column=10,columnspan=1,rowspan=2)
plan_e.grid(row=8,column=10,columnspan=1,rowspan=2)
button_d2.grid(row=10,column=8,columnspan=4,rowspan=1)
poe_label.grid(row=6,column=7)
ple_label.grid(row=8,column=7)
d2_help.grid(row=10,column=7)
"""vecteurs menu"""
vecteurs_aff = Frame(root,relief="raised",bg="#BADA55")
ajouter_vecteur = Button(vecteurs_aff, text="Ajouter un vecteur",takefocus="",font=myFont,width=20,
                  command=ajout_vecteur,bg="#14836e",fg="white",activebackground="#0a4753")
modifier_vecteur = Button(vecteurs_aff, text="Modifier un vecteur",takefocus="",font=myFont,width=20,
                  command=mod_vecteur,bg="#14836e",fg="white",activebackground="#0a4753")
supprimer_vecteur = Button(vecteurs_aff, text="Supprimer un vecteur",takefocus="",font=myFont,width=20,
                          command=lambda:stick(group_supp_vec,130,105,400,400,10,5),bg="#14836e",fg="white",activebackground="#0a4753")
trouver_cvecteur = Button(vecteurs_aff, text="Trouver un vecteur",takefocus="",font=myFont,width=20,
                  command=lambda:stick(group_find_vec,130,125,400,400,10,5),bg="#14836e",fg="white",activebackground="#0a4753")
ajouter_vecteur.grid(row=5,column=3,columnspan=6,rowspan=1)
modifier_vecteur.grid(row=9,column=3,columnspan=6,rowspan=1)
supprimer_vecteur.grid(row=13,column=3,columnspan=6,rowspan=1)
trouver_cvecteur.grid(row=17,column=3,columnspan=6,rowspan=1)
#ajouter/modifier un vecteur
group_vec_ajout = LabelFrame(root,text="Ajouter un plan",relief="raised",bg="#BADA55",font=myFont2,fg="white")
nom_vec_ajout=Entry(group_vec_ajout,width=7,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",
          validate="focusout",validatecommand=lambda:labelup4(),font=myFont1)
c_vec_ajout=Entry(group_vec_ajout,width=16,bg="#657478",fg="white",relief="flat",
                  justify="center",takefocus="",font=myFont1)
ajout_vec_prompt_n=Label(group_vec_ajout,text=f"Veuillez saisir un\nnom pour ce vecteur",bg="#BADA55",font=myFont2)
ajout_vec_prompt_c=Label(group_vec_ajout,text=f"Veuillez saisir\nles composants\nde ce vecteur",
                          bg="#BADA55",font=myFont2)
ajout_vec_prompt_help=Label(group_vec_ajout,text="exemple : 1.5 2 3",bg="#2b2b2b",fg="white",font=myFont1)
button_vec_ajout = Button(group_vec_ajout, text="Ajouter",takefocus="",font=myFont,
                  command=insert_plan,bg="#005668",fg="white",activebackground="#0a4753")
nom_vec_ajout.grid(row=6,column=10,columnspan=1)
c_vec_ajout.grid(row=9,column=9,columnspan=3 )
button_vec_ajout.grid(row=10,column=9,columnspan=3,rowspan=1)
ajout_vec_prompt_n.grid(row=6,column=7)
ajout_vec_prompt_c.grid(row=9,column=7)
ajout_vec_prompt_help.grid(row=10,column=7)
#supprimer un vecteur
group_supp_vec = LabelFrame(root,text="Supprimer un vecteur",relief="raised",bg="#BADA55",font=myFont2,fg="white")
nom_s_vec=Entry(group_supp_vec,width=15,bg="#657478",fg="white",relief="flat",justify="center",font=myFont1)
supp_vec_prompt=Label(group_supp_vec,text=f"Veuillez saisir le\nnom du vecteur",bg="#BADA55",font=myFont2)
button_supp_vec = Button(group_supp_vec, text="Supprimer",takefocus="",font=myFont,width=17,
                  command=supp_vec,bg="#005668",fg="white",activebackground="#0a4753")
supp_vec_prompt.grid(row=2,column=2,columnspan=4)
nom_s_vec.grid(row=2,column=6,columnspan=5)
button_supp_vec.grid(row=5,column=3,columnspan=6,rowspan=1)
#trouver un vecteur
group_find_vec=LabelFrame(root,text="Trouver un vecteur",relief="raised",bg="#BADA55",font=myFont2,fg="white")
pts_vec=Entry(group_find_vec,width=10,bg="#657478",fg="white",relief="flat",justify="center",font=myFont1)
f_vec_prompt=Label(group_find_vec,text=f"Veuillez saisir les\ndeux points qui forment le vecteur",bg="#BADA55",font=myFont2)
vec_res=Label(group_find_vec,text=" ( 0 )\n(  0  )\n ( 0 ) ",bg="#BADA55",font=myFont1)
button_f_vec = Button(group_find_vec, text="Trouver ses composants",takefocus="",font=myFont,width=20,
                  command=find_c_vec,bg="#005668",fg="white",activebackground="#0a4753")
f_vec_prompt.grid(row=2,column=2,columnspan=10)
pts_vec.grid(row=4,column=4,columnspan=5)
button_f_vec.grid(row=5,column=3,columnspan=8,rowspan=1,padx=30)
vec_res.grid(row=4,column=7,columnspan=6,rowspan=1)
#Produit scalaire
group_scalaire=LabelFrame(root,text="Calculer un produit scalaire",relief="raised",bg="#BADA55",font=myFont2,fg="white")
sc_vec1=Entry(group_scalaire,width=7,bg="#657478",fg="white",relief="flat",justify="center",font=myFont1)
sc_vec2=Entry(group_scalaire,width=7,bg="#657478",fg="white",relief="flat",justify="center",font=myFont1)
sc_prompt=Label(group_scalaire,text=f"Veuillez saisir les deux vecteurs\nou les points qui les forment",bg="#BADA55",font=myFont2)
sc_res=Label(group_scalaire,text="= 0 ",bg="#BADA55",font=myFont1)
sc_point=Label(group_scalaire,text=".",bg="#BADA55",font=myFont1)
button_sc = Button(group_scalaire, text="Calculer",takefocus="",font=myFont,width=20,
                  command=lambda:extract23(sc_vec1.get(),sc_vec2.get(),"",1),bg="#005668",fg="white",activebackground="#0a4753")
sc_prompt.grid(row=2,column=1,columnspan=10)
sc_vec1.grid(row=4,column=2,columnspan=1)
sc_point.grid(row=4,column=3,columnspan=1)
sc_vec2.grid(row=4,column=4,columnspan=1)
button_sc.grid(row=5,column=1,columnspan=8,rowspan=1,padx=30,pady=10)
sc_res.grid(row=4,column=5,columnspan=1,rowspan=1)
#Produit vectoriel
group_vectoriel=LabelFrame(root,text="Calculer un produit vectoriel",relief="raised",bg="#BADA55",font=myFont2,fg="white")
ve_vec1=Entry(group_vectoriel,width=7,bg="#657478",fg="white",relief="flat",justify="center",font=myFont1)
ve_vec2=Entry(group_vectoriel,width=7,bg="#657478",fg="white",relief="flat",justify="center",font=myFont1)
ve_prompt=Label(group_vectoriel,text=f"Veuillez saisir les deux vecteurs\nou les points qui les forment",bg="#BADA55",font=myFont2)
ve_res=Label(group_vectoriel,text="  ( 0 )\n= (  0  )\n   ( 0 ) ",bg="#BADA55",font=myFont1)
ve_point=Label(group_vectoriel,text="^",bg="#BADA55",font=myFont1)
button_ve = Button(group_vectoriel, text="Calculer",takefocus="",font=myFont,width=20,
                  command=lambda:extract23(ve_vec1.get(),ve_vec2.get(),"",2),bg="#005668",fg="white",activebackground="#0a4753")
ve_prompt.grid(row=2,column=1,columnspan=10)
ve_vec1.grid(row=4,column=2,columnspan=1)
ve_point.grid(row=4,column=3,columnspan=1)
ve_vec2.grid(row=4,column=4,columnspan=1)
button_ve.grid(row=5,column=1,columnspan=8,rowspan=1,padx=30,pady=10)
ve_res.grid(row=4,column=5,columnspan=1,rowspan=1)
#Determinant
group_determinant=LabelFrame(root,text="Calculer un determinant",relief="raised",bg="#BADA55",font=myFont2,fg="white")
det_vec1=Entry(group_determinant,width=4,bg="#657478",fg="white",relief="flat",justify="center",font=myFont1)
det_vec2=Entry(group_determinant,width=4,bg="#657478",fg="white",relief="flat",justify="center",font=myFont1)
det_vec3=Entry(group_determinant,width=4,bg="#657478",fg="white",relief="flat",justify="center",font=myFont1)
det_prompt=Label(group_determinant,text=f"Veuillez saisir les trois vecteurs\nou les points qui les forment",bg="#BADA55",font=myFont2)
det_res=Label(group_determinant,text=") = 0 ",bg="#BADA55",font=myFont1)
det_point=Label(group_determinant,text="det (",bg="#BADA55",font=myFont1)
button_det = Button(group_determinant, text="Calculer",takefocus="",font=myFont,width=20,
                  command=lambda:extract23(det_vec1.get(),det_vec2.get(),det_vec3.get(),3),bg="#005668",fg="white",activebackground="#0a4753")
det_prompt.grid(row=2,column=1,columnspan=10)
det_vec1.grid(row=4,column=3,columnspan=1)
det_point.grid(row=4,column=2,columnspan=1)
det_vec2.grid(row=4,column=4,columnspan=1)
det_vec3.grid(row=4,column=5,columnspan=1)
button_det.grid(row=5,column=1,columnspan=10,rowspan=1,padx=30,pady=10)
det_res.grid(row=4,column=7,columnspan=1,rowspan=1)
#aires
aires = Frame(root,relief="raised",bg="#BADA55")
aire_tri = Button(aires, text="Aire d'un triangle",takefocus="",font=myFont,width=20,
                  command=lambda:stick(group_aire1,380,100,300,400,10,4),bg="#14836e",fg="white",activebackground="#0a4753")
aire_para = Button(aires, text="Aire d'un parallélograme",takefocus="",font=myFont,width=20,
                  command=lambda:stick(group_aire2,390,120,300,400,10,0),bg="#14836e",fg="white",activebackground="#0a4753")
aire_tri.grid(row=5,column=3,columnspan=6,rowspan=1)
aire_para.grid(row=9,column=3,columnspan=6,rowspan=1)
#aire triangle
group_aire1 = LabelFrame(root,text="Calculer l'aire d'un triangle",relief="raised",bg="#BADA55",font=myFont2,fg="white")
triangle=Entry(group_aire1,width=7,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",font=myFont1)
tri_label=Label(group_aire1,text=f"Veuillez entrer le nom\nde ce triangle",bg="#BADA55",font=myFont2)
tri_help=Label(group_aire1,text=f"exemple : ABC",bg="#BADA55",font=myFont1)
button_tri = Button(group_aire1, text="Calculer l'aire",takefocus="",font=myFont,width=17,
                  command=calc_aire1,bg="#005668",fg="white",activebackground="#0a4753")
triangle.grid(row=6,column=10,columnspan=1,rowspan=2)
button_tri.grid(row=10,column=7,columnspan=7,rowspan=1,padx=5)
tri_label.grid(row=6,column=7)
tri_help.grid(row=7,column=7)
#aire parallelo
group_aire2 = LabelFrame(root,text="Calculer l'aire d'un parallélogramme",relief="raised",bg="#BADA55",font=myFont2,fg="white")
para=Entry(group_aire2,width=7,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",font=myFont1)
para_label=Label(group_aire2,text=f"Veuillez entrer le nom\nde ce parallélogramme",bg="#BADA55",font=myFont2)
para_help=Label(group_aire2,text=f"exemple : ABCD",bg="#BADA55",font=myFont1)
button_para = Button(group_aire2, text="Calculer l'aire",takefocus="",font=myFont,width=17,
                  command=calc_aire2,bg="#005668",fg="white",activebackground="#0a4753")
para.grid(row=6,column=11,columnspan=1,rowspan=2)
button_para.grid(row=10,column=7,columnspan=10,rowspan=1,padx=55)
para_label.grid(row=6,column=7,padx=20)
para_help.grid(row=7,column=7)
#volumes
volumes = Frame(root,relief="raised",bg="#BADA55")
volume_t = Button(volumes, text="Volume d'un tétraedre",takefocus="",font=myFont,width=22,
                  command=lambda:stick(group_vol1,480,100,300,400,10,4),bg="#14836e",fg="white",activebackground="#0a4753")
volume_p = Button(volumes, text="Volume d'un parallélipede",takefocus="",font=myFont,width=22,state="disabled",
                  command=lambda:stick(group_vol2,480,128,300,400,10,0),bg="#14836e",fg="white",activebackground="#0a4753")
volume_t.grid(row=5,column=3,columnspan=6,rowspan=1)
volume_p.grid(row=9,column=3,columnspan=6,rowspan=1)
#Volume tetraédre
group_vol1 = LabelFrame(root,text="Calculer l'aire d'un triangle",relief="raised",bg="#BADA55",font=myFont2,fg="white")
tetra=Entry(group_vol1,width=7,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",font=myFont1)
tetra_label=Label(group_vol1,text=f"Veuillez entrer le nom\nde ce tétraedre",bg="#BADA55",font=myFont2)
tetra_help=Label(group_vol1,text=f"exemple : ABCD",bg="#BADA55",font=myFont1)
button_tetra = Button(group_vol1, text="Calculer la volume",takefocus="",font=myFont,width=17,
                  command=calc_vol1,bg="#005668",fg="white",activebackground="#0a4753")
tetra.grid(row=6,column=10,columnspan=1,rowspan=2)
button_tetra.grid(row=10,column=7,columnspan=7,rowspan=1,padx=5)
tetra_label.grid(row=6,column=7)
tetra_help.grid(row=7,column=7)
#aire parallelo
group_vol2 = LabelFrame(root,text="Calculer l'aire d'un parallélipede",relief="raised",bg="#BADA55",font=myFont2,fg="white")
vpara=Entry(group_vol2,width=7,bg="#657478",fg="white",relief="flat",justify="center",takefocus="",font=myFont1)
vpara_label=Label(group_vol2,text=f"Veuillez entrer le nom\nde ce parallélipede",bg="#BADA55",font=myFont2)
vpara_help=Label(group_vol2,text=f"exemple : ABCDEFGH",bg="#BADA55",font=myFont1)
button_vpara = Button(group_vol2, text="Calculer la volume",takefocus="",font=myFont,width=17,
                  command=calc_vol2,bg="#005668",fg="white",activebackground="#0a4753")
vpara.grid(row=6,column=11,columnspan=1,rowspan=2)
button_vpara.grid(row=10,column=7,columnspan=10,rowspan=1,padx=55)
vpara_label.grid(row=6,column=7,padx=20)
vpara_help.grid(row=7,column=7)
#afficher points
afficher_points=LabelFrame(root,text="Points",relief="raised",bg="#BADA55",width=100,height=100,font=myFont2,fg="white")
points_aff=Label(afficher_points,text=print_inventory(points),bg="#BADA55",font=myFont2,pady=10,padx=10)
points_aff.pack()




wd=18
button_1 = tkinter.Button(root, text="Ajouter un point",width=wd,relief="groove",font=myFont,state="disabled",
                  command=lambda:stick(group_ajout,10,120,400,400,15,5) ,bg="#005668",fg="white",activebackground="#0a4753")
button_2 = tkinter.Button(root, text="Modifier un point",width=wd,relief="groove",font=myFont,state="disabled",
                  command=lambda:stick(group_mod,50,107,300,400,15,5),bg="#005668",fg="white",activebackground="#0a4753")
button_3 = tkinter.Button(root, text="Supprimer un point",width=wd,relief="groove",font=myFont,state="disabled",
                  command=lambda:stick(group_supp,40,104,300,400,10,4),bg="#005668",fg="white",activebackground="#0a4753")
button_4 = tkinter.Button(root, text="Plan",width=wd,relief="groove",font=myFont,state="disabled",
                  command=lambda:stick(plan_aff,70,85,400,400,0,0),bg="#005668",fg="white",activebackground="#0a4753")
button_5 = tkinter.Button(root, text="Distance",width=wd,relief="groove",font=myFont,state="disabled",
                  command=lambda:stick(distances,120,118,300,400,0,0),bg="#005668",fg="white",activebackground="#0a4753")
button_6 = tkinter.Button(root, text="Vecteur",width=wd,relief="groove",font=myFont,
                  command=lambda:stick(vecteurs_aff,180,90,400,400,0,0),bg="#005668",fg="white",activebackground="#0a4753")
button_7 = tkinter.Button(root, text="Produit Scalaire",width=wd,relief="groove",font=myFont,state="disabled",
                  command=lambda:stick(group_scalaire,200,120,300,400,0,0),bg="#005668",fg="white",activebackground="#0a4753")
button_8 = tkinter.Button(root, text="Produit Vectoriel",width=wd,relief="groove",font=myFont,state="disabled",
                  command=lambda:stick(group_vectoriel,200,120,400,400,0,0),bg="#005668",fg="white",activebackground="#0a4753")
button_9 = tkinter.Button(root, text="Determinant",width=wd,relief="groove",font=myFont,state="disabled",
                  command=lambda:stick(group_determinant,200,120,300,400,0,0),bg="#005668",fg="white",activebackground="#0a4753")
button_10 = tkinter.Button(root, text="Aire",width=wd,relief="groove",font=myFont,state="disabled",
                  command=lambda:stick(aires,420,89,300,400,0,0),bg="#005668",fg="white",activebackground="#0a4753")
button_11 = tkinter.Button(root, text="Volume",width=wd,relief="groove",font=myFont,state="disabled",
                  command=lambda:stick(volumes,530,92,300,400,0,0),bg="#005668",fg="white",activebackground="#0a4753")
button_101 = tkinter.Button(root, text="Afficher les points",width=wd,relief="groove",font=myFont,
                  command=lambda:stick(afficher_points,0,200,700,400,10,20),bg="#008080",fg="white",activebackground="#f4f6fa")

buttons=[button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_10,
         button_11,button_101]
for b in buttons:
    b.grid(row=(buttons.index(b)*58),column=10,columnspan=110,rowspan=65)
    



while True:
    try :
        upstates()
        root.update_idletasks()
        root.update()
    except : break
    
    
    
    
    