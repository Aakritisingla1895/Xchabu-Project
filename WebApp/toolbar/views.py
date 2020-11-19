from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from toolbar.models import East

# Create your views here.
def svg(request):
    sql = East.objects.filter(layoutno="layout 1")
    for q in sql:
        x=0
        y=0
        bedx=q.bedx=x
        q.bedy=y
        bedy=q.bedy+q.util
        bedw=q.bedw
        bedl=q.bedl
        print(bedx,bedy,bedw,bedl) 
        kitx=q.kitx=x
        kity= q.util+q.stal+q.drawl
        kitw=q.kitw
        kitl=q.kitl
        print("kitx(x):",kitx ,"kity(util+stal+drawl):",kity,"kitw:",kitw,"kitl:",kitl)
        toix=x+q.utiw
        toiy=q.toiy=0
        toiw=q.toiw
        toil=q.toil
        print("toix(x+utiw):",toix ,"toiy(y):",toiy,"toiw:",toiw,"toil:",toil) 
        drawx=x+q.staw
        drawy=y+q.util+q.bedl
        draww=q.draww
        drawl=q.drawl
        print("drawx(x+staw):",drawx ,"drawy(y+util+bedl):",drawy,"draww:",draww,"drawl:",drawl)  
        stax=q.stax=x
        stay=y+q.util+q.bedl
        staw=q.staw
        stal=q.stal
        print("stax(x):",stax ,"stay(y+util+bedl):",stay,"staw:",staw,"stal:",stal)    
        dinx=q.dinx
        diny=q.diny
        dinw=q.dinw
        dinl=q.dinl
        print("dinx:",dinx ,"diny:",diny,"dinw:",dinw,"dinl:",dinl)
        ctoix=q.ctoix=x
        ctoiy=y+q.util+q.stal+q.bedl
        ctoiw=q.ctoiw
        ctoil=q.ctoil
        print("ctoix(x):",ctoix ,"ctoiy(y+util+stal+bedl):",ctoiy,"ctoiw:",ctoiw,"ctoil:",ctoil)
        stox=x+q.washw
        stoy=y+q.util+q.bedl+q.stal
        stow=q.stow
        stol=q.stol
        print("stox(x+wasw):",stox ,"stoy(y+util+bedl+stal):",stoy,"stow:",stow,"stol:",stol)
        otsx=q.otsx
        otsy=q.otsy
        otsw=q.otsw
        otsl=q.otsl
        print("otsx:",otsx ,"otsy:",otsy,"otsw:",otsw,"otsl:",otsl)
        washx=q.washx=x
        washy=y+q.util+q.bedl+q.stal
        washw=q.washw
        washl=q.washl
        print("washx(x):",washx ,"washy(y+util+bedl+stal):",washy,"washw:",washw,"washl:",washl)
        entx=x+q.kitw
        enty=y+q.util+q.bedl+q.drawl
        entw=q.entw
        entl=q.entl
        print("entx(x+kitw):",entx ,"enty(y+util+bedl+drawl):",enty,"entw:",entw,"entl:",entl)
        parx=q.parx
        pary=q.pary
        parw=q.parw
        parl=q.parl
        print("parx:",parx ,"pary:",pary,"parw:",parw,"parl:",parl)
        garx=q.garx
        gary=q.gary
        garw=q.garw
        garl=q.garl
        print("garx:",garx ,"gary:",gary,"garw:",garw,"garl:",garl)
        foyx=q.foyx
        foyy=q.foyy
        foyw=q.foyw
        foyl=q.foyl
        print("foyx:",foyx ,"foyy:",foyy,"foyw:",foyw,"foyl:",foyl)
        utix = q.utix=x
        utiy = q.utiy=y
        utiw = q.utiw
        util = q.util
        print("utix(x):",utix ,"utiy(y):",utiy,"utiw:",utiw,"util:",util)
        context={
            "date":datetime.now,
            "bedx":bedx,
            "bedy":bedy,
            "bedw":bedw,
            "bedl":bedl,
            "kitx":kitx,
            "kity":kity,
            "kitw":kitw,
            "kitl":kitl,
            "utix":utix,
            "utiy":utiy,
            "utiw":utiw,
            "util":util,
            "foyx":foyx,
            "foyy":foyy,
            "foyw":foyw,
            "foyl":foyl,
            "garx":garx,
            "gary":gary,
            "garw":garw,
            "garl":garl,
            "parx":parx,
            "pary":pary,
            "parw":parw,
            "parl":parl,
            "entx":entx,
            "enty":enty,
            "entw":entw,
            "entl":entl,
            "washx":washx,
            "washy":washy,
            "washw":washw,
            "washl":washl,
            "otsx":otsx,
            "otsy":otsy,
            "otsw":otsw,
            "otsl":otsl,
            "stox":stox,
            "stoy":stoy,
            "stow":stow,
            "stol":stol,
            "toix":toix,
            "toiy":toiy,
            "toiw":toiw,
            "toil":toil,
            "drawx":drawx,
            "drawy":drawy,
            "draww":draww,
            "drawl":drawl,
            "stax":stax,
            "stay":stay,
            "staw":staw,
            "stal":stal,
            "dinx":dinx,
            "diny":diny,
            "dinw":dinw,
            "dinl":dinl,
            "ctoix":ctoix,
            "ctoiy":ctoiy,
            "ctoiw":ctoiw,
            "ctoil":ctoil,
            "q":q

        }
    return render(request,"index.html",context)

