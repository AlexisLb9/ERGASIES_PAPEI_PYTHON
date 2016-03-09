#PA=panw aristera PK=panw kentro PD=panw deksia k.o.k.

panw=["pa","pk","pd"]
mesh=["ma","mk","md"]
katw=["ka","kk","kd"]
i=2
s1=0
s2=0
m1=0
m2=0
b1=0
b2=0
#ftiaxnw 3 diaforetikes listes wste na tis gemisw me 0 kai 1.Opou 0-->paixths no1 kai 1 -->paixths no2.Me auton ton tropo tha elegxo thn sunthiki ths epanalipsis gia na stamataei otan kapios kanei triliza!
panw1=[2,3,4]
mesh1=[5,6,7]
katw1=[8,9,10]

while (panw1[0]!=panw1[1]!=panw1[2])and(mesh1[0]!=mesh1[1]!=mesh1[2])and(katw1[0]!=katw1[1]!=katw1[2])and(panw1[0]!=mesh1[0]!=katw1[0])and(panw1[1]!=mesh1[1]!=katw1[1])and(panw1[2]!=mesh1[2]!=katw1[2])and(panw1[0]!=mesh1[1]!=katw1[2])and(panw1[2]!=mesh1[1]!=katw1[0])and(s1+s2+m1+m2+b1+b2<12):
    if i%2==0:
        print "Paizei o paixths No1"
        #-------------------------------------------------PAIXTHS NO2-----------------------------------------------------------------------------
    
        i=i+1
        flag=0
    
        while flag==0:
            a = raw_input("Thesh?epiloges=(PA,PK,PD,MA,MK,MD,KA,KM,KD)")
            b = raw_input("Megethos pioniou?epiloges=(s->small,m->medium,b->big)")
            #PA ------------------------------------------------------------------
            if a=="PA":
                if b=="s":
                    if s1<2:
                        
                        if panw[0]=="pa":
                            panw[0]="s1"
                            panw1[0]=0
                            s1=s1+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m1<2:
                        if panw[0]=="m1" or panw[0]=="b1" or panw[0]=="m2"or panw[0]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            panw[0]="m1"
                            m1=m1+1
                            panw1[0]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b1<2:
                        if panw[0]=="b1" or panw[0]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            panw[0]="b1"
                            panw1[0]=0
                            b1=b1+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #PK ------------------------------------------------------------------------------
            elif a=="PK":
                if b=="s":
                    if s1<2:
                        
                        if panw[1]=="pk":
                            panw[1]="s1"
                            panw1[1]=0
                            s1=s1+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m1<2:
                        if panw[1]=="m1" or panw[1]=="b1" or panw[1]=="m2"or panw[1]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            panw[1]="m1"
                            panw1[1]=0
                            m1=m1+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b1<2:
                        if panw[1]=="b1" or panw[1]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            panw[1]="b1"
                            b1=b1+1
                            panw1[1]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #PD----------------------------------------------------------------------
            elif a=="PD":
                if b=="s":
                    if s1<2:
                        
                        if panw[2]=="pd":
                            panw[2]="s1"
                            panw1[2]=0
                            s1=s1+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m1<2:
                        if panw[2]=="m1" or panw[2]=="b1" or panw[2]=="m2"or panw[2]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            panw[2]="m1"
                            m1=m1+1
                            panw1[2]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b1<2:
                        if panw[2]=="b1" or panw[2]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            panw[2]="b1"
                            b1=b1+1
                            panw1[2]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #MA --------------------------------------------------------------------
            elif a=="MA":
                if b=="s":
                    if s1<2:
                        
                        if mesh[0]=="ma":
                            mesh[0]="s1"
                            mesh1[0]=0
                            s1=s1+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag="t"
                    
                elif b=="m":
                    if m1<2:
                        if mesh[0]=="m1" or mesh[0]=="b1" or mesh[0]=="m2"or mesh[0]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            mesh[0]="m1"
                            m1=m1+1
                            mesh1[0]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b1<2:
                        if mesh[0]=="b1" or mesh[0]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            mesh[0]="b1"
                            b1=b1+1
                            mesh1[0]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #MK ---------------------------------------------------------------
            elif a=="MK":
                if b=="s":
                    if s1<2:
                        
                        if mesh[1]=="mk":
                            mesh[1]="s1"
                            mesh1[1]=0
                            s1=s1+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m1<2:
                        if mesh[1]=="m1" or mesh[1]=="b1" or mesh[1]=="m2"or mesh[1]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            mesh[1]="m1"
                            m1=m1+1
                            mesh1[1]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b1<2:
                        if mesh[1]=="b1" or mesh[1]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            mesh[1]="b1"
                            b1=b1+1
                            mesh1[1]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #MD -----------------------------------------------------------------------------------
            elif a=="MD":
                if b=="s":
                    if s1<2:
                        
                        if mesh[2]=="md":
                            mesh[2]="s1"
                            s1=s1+1
                            mesh1[2]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m1<2:
                        if mesh[2]=="m1" or mesh[2]=="b1" or mesh[2]=="m2"or mesh[2]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            mesh[2]="m1"
                            m1=m1+1
                            mesh1[2]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b1<2:
                        if mesh[2]=="b1" or mesh[2]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            mesh[2]="b1"
                            b1=b1+1
                            flag=1
                            mesh1[2]=0
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #KA ------------------------------------------------------------------------
            elif a=="KA":
                if b=="s":
                    if s1<2:
                        
                        if katw[0]=="ka":
                            katw[0]="s1"
                            katw1[0]=0
                            s1=s1+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m1<2:
                        if katw[0]=="m1" or katw[0]=="b1" or katw[0]=="m2"or katw[0]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            katw[0]="m1"
                            m1=m1+1
                            flag=1
                            katw1[0]=0
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b1<2:
                        if katw[0]=="b1" or katw[0]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            katw[0]="b1"
                            b1=b1+1
                            katw1[0]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #KK --------------------------------------------------------------------------------------
            elif a=="KK":
                if b=="s":
                    if s1<2:
                        
                        if katw[1]=="kk":
                            katw[1]="s1"
                            katw1[1]=0
                            s1=s1+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m1<2:
                        if katw[1]=="m1" or katw[1]=="b1" or katw[1]=="m2"or katw[1]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            katw[1]="m1"
                            m1=m1+1
                            katw1[1]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b1<2:
                        if katw[1]=="b1" or katw[1]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            katw[1]="b1"
                            b1=b1+1
                            katw1[1]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #KD ---------------------------------------------------------------
            elif a=="KD":
                if b=="s":
                    if s1<2:
                        
                        if katw[2]=="kd":
                            katw[2]="s1"
                            s1=s1+1
                            katw1[2]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m1<2:
                        if katw[2]=="m1" or katw[2]=="b1" or katw[2]=="m2"or katw[2]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            katw[2]="m1"
                            m1=m1+1
                            katw1[2]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b1<2:
                        if katw[2]=="b1" or katw[2]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            katw[2]="b1"
                            b1=b1+1
                            katw1[2]=0
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                        
    else:
        print "Paizei o paixths No2"
        #-----------------------------------------------PAIXTHS NO2---------------------------------------------
        i=i+1
        flag=0
    
        while flag==0:
            a = raw_input("Thesh?epiloges=(PA,PK,PD,MA,MK,MD,KA,KM,KD)")
            b = raw_input("Megethos pioniou?epiloges=(s->small,m->medium,b->big)")
            #PA ------------------------------------------------------------------
            if a=="PA":
                if b=="s":
                    if s2<2:
                        
                        if panw[0]=="pa":
                            panw[0]="s2"
                            panw1[0]=1
                            s2=s2+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m2<2:
                        if panw[0]=="m1" or panw[0]=="b1" or panw[0]=="m2"or panw[0]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            panw[0]="m2"
                            m2=m2+1
                            flag=1
                            panw1[0]=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b2<2:
                        if panw[0]=="b1" or panw[0]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            panw[0]="b2"
                            b2=b2+1
                            panw1[0]=1
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #PK ------------------------------------------------------------------------------
            elif a=="PK":
                if b=="s":
                    if s2<2:
                        
                        if panw[1]=="pk":
                            panw[1]="s2"
                            panw1[1]=1
                            s2=s2+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m2<2:
                        if panw[1]=="m1" or panw[1]=="b1" or panw[1]=="m2"or panw[1]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            panw[1]="m2"
                            m2=m2+1
                            panw1[1]=1
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b2<2:
                        if panw[1]=="b1" or panw[1]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            panw[1]="b2"
                            b2=b2+1
                            flag=1
                            panw1[1]=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #PD----------------------------------------------------------------------
            elif a=="PD":
                if b=="s":
                    if s2<2:
                        
                        if panw[2]=="pd":
                            panw[2]="s2"
                            panw1[2]=1
                            s2=s2+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m2<2:
                        if panw[2]=="m1" or panw[2]=="b1" or panw[2]=="m2"or panw[2]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            panw[2]="m2"
                            m2=m2+1
                            flag=1
                            panw1[2]=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b2<2:
                        if panw[2]=="b1" or panw[2]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            panw[2]="b2"
                            b2=b2+1
                            flag=1
                            panw1[2]=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #MA --------------------------------------------------------------------
            elif a=="MA":
                if b=="s":
                    if s2<2:
                        
                        if mesh[0]=="ma":
                            mesh[0]="s2"
                            mesh1[0]=1
                            s2=s2+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m2<2:
                        if mesh[0]=="m1" or mesh[0]=="b1" or mesh[0]=="m2"or mesh[0]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            mesh[0]="m2"
                            m2=m2+1
                            mesh1[0]=1
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b2<2:
                        if mesh[0]=="b1" or mesh[0]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            mesh[0]="b2"
                            b2=b2+1
                            mesh1[0]=1
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #MK ---------------------------------------------------------------
            elif a=="MK":
                if b=="s":
                    if s2<2:
                        
                        if mesh[1]=="mk":
                            mesh[1]="s2"
                            mesh1[1]=1
                            s2=s2+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m2<2:
                        if mesh[1]=="m1" or mesh[1]=="b1" or mesh[1]=="m2"or mesh[1]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            mesh[1]="m2"
                            m2=m2+1
                            mesh1[1]=1
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b2<2:
                        if mesh[1]=="b1" or mesh[1]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            mesh[1]="b2"
                            b2=b2+1
                            flag=1
                            mesh1[1]=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #MD -----------------------------------------------------------------------------------
            elif a=="MD":
                if b=="s":
                    if s2<2:
                        
                        if mesh[2]=="md":
                            mesh[2]="s2"
                            mesh1[2]=1
                            s2=s2+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m2<2:
                        if mesh[2]=="m1" or mesh[2]=="b1" or mesh[2]=="m2"or mesh[2]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            mesh[2]="m2"
                            m2=m2+1
                            mesh1[2]=1
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b2<2:
                        if mesh[2]=="b1" or mesh[2]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            mesh[2]="b2"
                            b2=b2+1
                            flag=1
                            mesh1[2]=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #KA ------------------------------------------------------------------------
            elif a=="KA":
                if b=="s":
                    if s2<2:
                        
                        if katw[0]=="ka":
                            katw[0]="s2"
                            katw1[0]=1
                            s2=s2+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m2<2:
                        if katw[0]=="m1" or katw[0]=="b1" or katw[0]=="m2"or katw[0]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            katw[0]="m2"
                            m2=m2+1
                            katw1[0]=1
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b2<2:
                        if katw[0]=="b1" or katw[0]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            katw[0]="b2"
                            b2=b2+1
                            katw1[0]=1
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #KK --------------------------------------------------------------------------------------
            elif a=="KK":
                if b=="s":
                    if s2<2:
                        
                        if katw[1]=="kk":
                            katw[1]="s2"
                            katw1[1]=1
                            s2=s2+1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m2<2:
                        if katw[1]=="m1" or katw[1]=="b1" or katw[1]=="m2"or katw[1]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            katw[1]="m2"
                            m2=m2+1
                            katw1[1]=1
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b2<2:
                        if katw[1]=="b1" or katw[1]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            katw[1]="b2"
                            b2=b2+1
                            katw1[1]=1
                            flag=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
                    #KD ---------------------------------------------------------------
            elif a=="KD":
                if b=="s":
                    if s2<2:
                        
                        if katw[2]=="kd":
                            katw[2]="s2"
                            s2=s2+1
                            katw1[2]=1
                            flag=1
                            print panw
                            print mesh
                            print katw
                        else:
                            print "den mporeis na to topothethseis edw"
                            flag=0
                    else:
                        print "exeis hdh xrhsimopoihsei 2 mikra.Paikse ksana!"
                        flag=0
                    
                elif b=="m":
                    if m2<2:
                        if katw[2]=="m1" or katw[2]=="b1" or katw[2]=="m2"or katw[2]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            katw[2]="m2"
                            m2=m2+1
                            flag=1
                            katw1[2]=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 mesaia.Paikse Ksana!"
                        flag=0
                elif b=="b":
                    if b2<2:
                        if katw[2]=="b1" or katw[2]=="b2":
                            flag=0
                            print "den mporeis na to topothethseis edw"
                        else:
                            katw[2]="b2"
                            b2=b2+1
                            flag=1
                            katw1[2]=1
                            print panw
                            print mesh
                            print katw
                    else:
                        print "exeis xrhsimopoihsei 2 magala.Paikse ksana!"
                        flag=0
                else:
                    print "edwses lathos apanthsh.Paikse ksana!"
                    flag=0
    print "Telos seiras"
    print panw1
    print mesh1
    print katw1
if (s1+s2+m1+m2+b1+b2!=12):
    if i%2==0:
        print "O Paixths No2 Nikhse!!!"
    else:
        print "O Paixths No1 Nikhse!!!"
        


#Kapou sto telos katalava oti eprepe na exw kanei mia sunarthsh apla:P
        
