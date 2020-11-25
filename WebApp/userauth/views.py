from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.forms import PasswordResetForm
from .models import User,CreateProject,South,Southwall,Southdoor, Room,ForgotPassword
from userauth.forms import CreateForm
from django.contrib.sessions.models import Session
from django.contrib import messages
from datetime import datetime
from django.conf import settings
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.db import connection
from django.urls import reverse
import sqlite3 as db

# Create your views here.
def userlogin(request):
    if request.session.has_key('uid'):
        return redirect('/dash_bord')

    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        user = User()
        count = User.objects.filter(email=email,password=password).count()
        if count >0:
            request.session['uid'] = request.POST['email']
            return redirect('/dash_bord')
        else:
            messages.error(request,'Invalid Email And Password')
            return redirect('/')

    return render(request,'login.html')

def usersignup(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        address = request.POST['address']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if User.objects.filter(email=email).exists():
            messages.error(request,"Email Already Exists ..")
            return redirect('/sign-up')
        else:
            user = User(name=name,cpassword = cpassword,email=email,phone=phone,gender=gender,address=address,password=password)
            user.save()
            messages.success(request,"Your Acoount Registered with Us")
            return redirect('/')
    return render(request,'signup.html')


def forgot_password(request):

  if request.POST:
    
    reset_email = request.POST['email']
    reset_password = request.POST['password']
    confirm_reset_password = request.POST['cpassword']

    print(reset_email)
    print (reset_password)

    a = User.objects.filter(email=reset_email)
    print(a)


    if User.objects.filter(email=reset_email).exists():
      password_reset = ForgotPassword(reset_email=reset_email, reset_password=reset_password, confirm_reset_password=confirm_reset_password)
      
      # password swap condition
      pswd1 = User.objects.update(password=reset_password, cpassword=confirm_reset_password)
      

      messages.success(request,"Password saved successful")
      
    else:
      messages.error(request,"Please enter a registered email address")
    
  return render(request,"forgot_password.html")

def deletesession(request):
    del request.session['uid']
    return redirect('/')


def deshbord(request):

    if request.session.has_key('uid'):
        user = User.objects.filter(email=request.session['uid'])
        for data in user:
            return render(request,'base.html',{"udata":data,"date":datetime.now})
    else:
        return redirect('/')



def createproject(request,id=id):

    if request.session.has_key('uid'):
        data = CreateProject.objects.all()
        #print(data)

        
        if(request.POST):
            firstname = request.POST.get('firstname')
            ftype = request.POST.get('ftype')
            direction = request.POST.get('direction')
            yes = request.POST.get('yes',0)
            no = request.POST.get('no',0)
            ots = request.POST.get('ots',0)
            store = request.POST.get('store',0)
            garden = request.POST.get('garden',0)
            temple = request.POST.get('temple',0)
            parking = request.POST.get('parking',0)
            dressingroom = request.POST.get('dressingroom',0)
            utility = request.POST.get('utility',0)
            washarea = request.POST.get('washarea',0)
            height = request.POST.get('height')
            width = request.POST.get('width')
            user = User.objects.get(id=id)


            #print (request.POST)
        
            User1 = User.objects.filter(email=request.session['uid'])
            user_name = User1[0]            

            sql = CreateProject(firstname=firstname,ftype=ftype,direction=direction,yes=yes,no=no,
            ots=ots,store=store,garden=garden,temple=temple,parking=parking,dressingroom=dressingroom,utility=utility,
            washarea=washarea,height=height,width=width,user=user_name)

            previous_data = CreateProject.objects.filter(user=user_name).delete()
          
            sql_form_data = sql.save() # check for sql data saved during create project form request

            userdata1 = CreateProject.objects.filter(user=user_name)

            #print (userdata1)
            for x in userdata1: 
              
              #print(x.firstname.replace(" ", ""))
              #print (x.ftype)
              user_direction = x.direction.lower()
              #print (user_direction)
              #print (x.direction.lower())
              #print (x.ots)
              #print(x.utility)

              #keywords for seleting amenities in create project form

              form_ots = 'O'
              form_temple = 'T'
              form_parking = 'P'
              form_store = 'S'
              form_garden = 'G'
              form_utility = 'U'
              form_washarea = 'W'
              form_entry = 'E'
              layout_no23 = ""

              if x.garden == True:
                garden = "checked"
                layout_no23 = layout_no23 + form_garden
              else:
                garden = ""              
              if x.ots == True:
                ots = "checked"
                layout_no23 = layout_no23 + form_ots
              else:
                ots= ""
              if x.parking == True:
                parking = "checked"
                layout_no23 = layout_no23 + form_parking
              else:
                parking = ""
              if x.store == True:
                store = "checked"
                layout_no23 = layout_no23 + form_store
                #print(layout_no23)
              else:
                store=""
              if x.temple == True:
                temple = "checked"
                layout_no23 = layout_no23 + form_temple
              else:
                temple = ""
              if x.utility == True:
                utility="checked"
                layout_no23 = layout_no23 + form_utility
              else:
                utility="" 
              if x.washarea == True:
                washarea="checked"
                layout_no23 = layout_no23 + form_washarea
              else:
                washarea = ""

              print(layout_no23)
              
              string = x.firstname.replace(" ", "")
              user_direction = x.direction.lower()
              #print (user_direction)
              #print (string.split())

              n = 2
              string_chunks = [string[i:i+n] for i in range(0, len(string), n)]
              trial = string_chunks.pop()

              #print (string_chunks)
              

              for l in string_chunks:
                from nltk.tokenize.treebank import TreebankWordDetokenizer
                layout_no= l  + layout_no23

                #print (type(layout_no))
                #print (layout_no)

    
              #layout_no1 = TreebankWordDetokenizer().detokenize(layout_no).replace(" ", "").strip()
              #print(type(layout_no1))
              #connecting to sqlite database for backend connectivity
              conn = db.connect('D:/Work/Xchabu Project/Project Code/room_latest.db')
              cur = conn.cursor()
              sql_query2 = 'SELECT layoutno from {} '.format(user_direction)
              layout_list = cur.execute(sql_query2).fetchall()
              layout_list1 = list(sum(layout_list, ()))


              conn_wall = db.connect('D:/Work/Xchabu Project/Project Code/wall.db')
              cur_wall = conn_wall.cursor()
              sql_query_wall = 'SELECT layoutno from {} '.format(user_direction)
              wall_list = cur_wall.execute(sql_query_wall).fetchall()
              print (wall_list)


              conn_door = db.connect('D:/Work/Xchabu Project/Project Code/door.db')
              cur_door = conn_door.cursor()
              sql_query_door = 'SELECT layoutno from {} '.format(user_direction)
              door_list = cur_door.execute(sql_query_door).fetchall()
              print (door_list)



              from difflib import get_close_matches

              match1 = get_close_matches(layout_no, layout_list1)
              for x12 in match1:
                print(x12)
                

              import random

              x1 = random.choice(match1)
                
              sql_query1 = 'SELECT * from {} where layoutno = ? '.format(user_direction)
              
              
              #data = cur.execute('SELECT * from %s where layoutno = "1B2TW"', [user_direction]).fetchall() #passing sql query to specific row of sepcif database
              
              #tup1 = (user_direction, layout_no1)
              room_data = cur.execute(sql_query1, (x12,)).fetchall()
              wall_data = cur_wall.execute(sql_query1, (x12,)).fetchall()
              door_data = cur_door.execute(sql_query1, (x12,)).fetchall()
              print(door_data)
              
              #print(room_data)

              ratio = 10
              room_list = []

              for item in room_data:
                #print(list(item))
                bedl = item[1]*ratio
                bedw = item[2]*ratio
                bedx = item[3]*ratio
                bedy = item[4]*ratio
                kitl = item[5]*ratio
                kitw = item[6]*ratio
                kitx = item[7]*ratio
                kity = item[8]*ratio
                toil = item[9]*ratio
                toiw = item[10]*ratio
                toix = item[11]*ratio
                toiy = item[12]*ratio
                drawl = item[13]*ratio
                draww = item[14]*ratio
                drawx = item[15]*ratio
                drawy = item[16]*ratio
                stal = item[17]*ratio
                staw = item[18]*ratio
                stax = item[19]*ratio
                stay = item[20]*ratio
                dinl = item[21]*ratio
                dinw = item[22]*ratio
                dinx = item[23]*ratio
                diny = item[24]*ratio
                ctoil = item[25]*ratio
                ctoiw = item[26]*ratio
                ctoix = item[27]*ratio
                ctoiy = item[28]*ratio
                stol = item[29]*ratio
                stow = item[30]*ratio
                stox = item[31]*ratio
                stoy = item[32]*ratio
                otsl = item[33]*ratio
                otsw = item[34]*ratio
                otsx = item[35]*ratio
                otsy = item[36]*ratio
                washl = item[37]*ratio
                washw = item[38]*ratio
                washx = item[39]*ratio
                washy = item[40]*ratio
                entl = item[41]*ratio
                entw = item[42]*ratio
                entx = item[43]*ratio
                enty = item[44]*ratio
                parl = item[45]*ratio
                parw = item[46]*ratio
                parx = item[47]*ratio
                pary = item[48]*ratio
                garl = item[49]*ratio 
                garw = item[50]*ratio
                garx = item[51]*ratio
                gary = item[52]*ratio
                foyl = item[53]*ratio
                foyw = item[54]*ratio
                foyx = item[55]*ratio
                foyy = item[56]*ratio
                util = item[57]*ratio
                utiw = item[58]*ratio
                utix = item[59]*ratio
                utiy = item[60]*ratio
                sto2l = item[61]*ratio
                sto2w = item[62]*ratio
                sto2x = item[63]*ratio
                sto2y = item[64]*ratio
                bed2l = item[65]*ratio
                bed2w = item[66]*ratio
                bed2x = item[67]*ratio
                bed2y = item[68]*ratio
                emptyl = item[69]*ratio
                emptyw = item[70]*ratio
                emptyx = item[71]*ratio
                emptyy = item[72]*ratio
                ots2l = item[73]*ratio
                ots2w = item[74]*ratio
                ots2x = item[75]*ratio
                ots2y = item[76]*ratio

                room_list.append(item)
                print (room_list)


                


                # coordinates for text
                bed_xco = bedx + (bedw/4)
                bed_yco = bedy + (bedl/3)
                kit_xco = kitx + (kitw/4)
                kit_yco = kity + (kitl/3)
                toi_xco = toix + (toiw/4)
                toi_yco = toiy + (toil/3)
                draw_xco = drawx + (draww/4)
                draw_yco = drawy + (drawl/3)
                sta_xco = stax + (staw/6)
                sta_yco = stay + (stal/3)
                wash_xco = washx + (washw/3)
                wash_yco = washy + (washl/3)


                din_xco = dinx + (dinw/4)     #  text coordinates for DINNING 
                din_yco = diny + (dinl/3)
                ctoi_xco = ctoix + (ctoiw/2)  #  text coordinates for TOILET 
                ctoi_yco = ctoiy + (ctoil/3)
                sto_xco = stox + (stow/2)
                sto_yco = stoy + (stol/3)
                ots_xco = otsx + (otsw/4)     #  text coordinates for OTS
                ots_yco = otsy + (otsl/3)
                ent_xco = bedx + (entw/4)     #  text coordinates for ENTRY
                ent_yco = bedy + (entl/3)
                par_xco = parx + (parw/4)     #  text coordinates for PARKING
                par_yco = pary + (parl/3)
                gar_xco = garx + (garw/4)     #  text coordinates for GARDEN
                gar_yco = gary + (garl/3)
                foy_xco = foyx + (foyw/4)     #  text coordinates for FOYER
                foy_yco = foyy + (foyl/3)
                uti_xco = utix + (utiw/4)     #  text coordinates for UTILITY
                uti_yco = utiy + (util/3)
                sto2_xco = sto2x + (sto2w/4)  #  text coordinates for DOUBLE_STORE
                sto2_yco = sto2y + (sto2l/3)
                ots2_xco = ots2x + (ots2w/4)   #  text coordinates for DOUBLE_OTS
                ots2_yco = ots2y + (ots2l/3)
                bed2_xco = bed2x + (bed2w/4)   #  text coordinates for DOUBLE_BED
                bed2_yco = bed2y + (bed2l/3)
                ent_xco = entx + (entw/4)      #  text coordinates for ENTRY
                ent_yco = enty + (entl/3)
                
                for w in wall_data:

                  wbedl = w[1]*ratio
                  wbedw = w[2]*ratio
                  wbedx = w[3]*ratio
                  wbedy = w[4]*ratio
                  wkitl = w[5]*ratio
                  wkitw = w[6]*ratio
                  wkitx = w[7]*ratio
                  wkity = w[8]*ratio
                  wtoil = w[9]*ratio
                  wtoiw = w[10]*ratio
                  wtoix = w[11]*ratio
                  wtoiy = w[12]*ratio
                  wdrawl = w[13]*ratio
                  wdraww = w[14]*ratio
                  wdarwx = w[15]*ratio
                  wdrawy = w[16]*ratio
                  wstal = w[17]*ratio
                  wstaw = w[18]*ratio
                  wstax = w[19]*ratio
                  wstay = w[20]*ratio
                  wdinl = w[21]*ratio
                  wdinw = w[22]*ratio
                  wdinx = w[23]*ratio
                  wdiny = w[24]*ratio
                  wctoil = w[25]*ratio
                  wctoiw = w[26]*ratio
                  wctoix = w[27]*ratio
                  wctoiy = w[28]*ratio
                  wstol = w[29]*ratio
                  wstow = w[30]*ratio
                  wstox = w[31]*ratio
                  wstoy = w[32]*ratio
                  wotsl = w[33]*ratio
                  wotsw = w[34]*ratio
                  wotsx = w[35]*ratio
                  wotsy = w[36]*ratio
                  wwashl = w[37]*ratio
                  wwashw = w[38]*ratio
                  wwashx = w[39]*ratio
                  wwashy = w[40]*ratio
                  wentl = w[41]*ratio
                  wentw = w[42]*ratio
                  wentx = w[43]*ratio
                  wenty = w[44]*ratio
                  wparl = w[45]*ratio
                  wparw = w[46]*ratio
                  wparx = w[47]*ratio
                  wpary = w[48]*ratio
                  wgarl = w[49]*ratio
                  wgarw = w[50]*ratio
                  wgarx = w[51]*ratio
                  wgary = w[52]*ratio
                  wfoyl = w[53]*ratio
                  wfoyw = w[54]*ratio
                  wfoyx = w[55]*ratio
                  wfoyy = w[56]*ratio
                  wutil = w[57]*ratio
                  wutiw = w[58]*ratio
                  wutix = w[59]*ratio
                  wutiy = w[60]*ratio
                  wsto2l = w[61]*ratio
                  wsto2w = w[62]*ratio
                  wsto2x = w[63]*ratio
                  wsto2y = w[64]*ratio
                  wbed2l = w[65]*ratio
                  wbed2w = w[66]*ratio
                  wbed2x = w[67]*ratio
                  wbed2y = w[68]*ratio
                  wemptyl = w[69]*ratio
                  wemptyw = w[70]*ratio
                  wemptyx = w[71]*ratio
                  wemptyy = w[72]*ratio
                  wots2l = w[73]*ratio
                  wots2w = w[74]*ratio
                  wots2x = w[75]*ratio
                  wots2y = w[76]*ratio


                for d in door_data:

                  dbedl = d[1]*ratio
                  dbedw = d[2]*ratio
                  dbedx = d[3]*ratio
                  dbedy = d[4]*ratio
                  dkitl = d[5]*ratio
                  dkitw = d[6]*ratio
                  dkitx = d[7]*ratio
                  dkity = d[8]*ratio
                  dtoil = d[9]*ratio
                  dtoiw = d[10]*ratio
                  dtoix = d[11]*ratio
                  dtoiy = d[12]*ratio
                  ddrawl = d[13]*ratio
                  ddraww = d[14]*ratio
                  ddarwx = d[15]*ratio
                  ddrawy = d[16]*ratio
                  dstal = d[17]*ratio
                  dstaw = d[18]*ratio
                  dstax = d[19]*ratio
                  dstay = d[20]*ratio
                  ddinl = d[21]*ratio
                  ddinw = d[22]*ratio
                  ddinx = d[23]*ratio
                  ddiny = d[24]*ratio
                  dctoil = d[25]*ratio
                  dctoiw = d[26]*ratio
                  dctoix = d[27]*ratio
                  dctoiy = d[28]*ratio
                  dstol = d[29]*ratio
                  dstow = d[30]*ratio
                  dstox = d[31]*ratio
                  dstoy = d[32]*ratio
                  dotsl = d[33]*ratio
                  dotsw = d[34]*ratio
                  dotsx = d[35]*ratio
                  dotsy = d[36]*ratio
                  dwashl = d[37]*ratio
                  dwashw = d[38]*ratio
                  dwashx = d[39]*ratio
                  dwashy = d[40]*ratio
                  dentl = d[41]*ratio
                  dentw = d[42]*ratio
                  dentx = d[43]*ratio
                  denty = d[44]*ratio
                  dparl = d[45]*ratio
                  dparw = d[46]*ratio
                  dparx = d[47]*ratio
                  dpary = d[48]*ratio
                  dgarl = d[49]*ratio
                  dgarw = d[50]*ratio
                  dgarx = d[51]*ratio
                  dgary = d[52]*ratio
                  dfoyl = d[53]*ratio
                  dfoyw = d[54]*ratio
                  dfoyx = d[55]*ratio
                  dfoyy = d[56]*ratio
                  dutil = d[57]*ratio
                  dutiw = d[58]*ratio
                  dutix = d[59]*ratio
                  dutiy = d[60]*ratio
                  dsto2l = d[61]*ratio
                  dsto2w = d[62]*ratio
                  dsto2x = d[63]*ratio
                  dsto2y = d[64]*ratio
                  dbed2l = d[65]*ratio
                  dbed2w = d[66]*ratio
                  dbed2x = d[67]*ratio
                  dbed2y = d[68]*ratio
                  demptyl = d[69]*ratio
                  demptyw = d[70]*ratio
                  demptyx = d[71]*ratio
                  demptyy = d[72]*ratio
                  dots2l = d[73]*ratio
                  dots2w = d[74]*ratio
                  dots2x = d[75]*ratio
                  dots2y = d[76]*ratio
                
                
 
                

                # for optional amenities, looping condition............................

                if dinx == diny == dinl == dinw == 0: #dinning
                  din_fill = "None"
                else:
                  din_fill = "Black"
               
                if ctoil == ctoiw == ctoix == ctoiy == 0: #toilet
                  ctoi_fill = "None"
                else:
                  ctoi_fill = "Black"
                if stol == stow == stox == stoy == 0: #store
                  sto_fill ="None"
                else:
                  sto_fill = "Black"
                if otsl == otsw == otsx == otsy == 0: #ots
                  ots_fill ="None"
                else:
                  ots_fill = "Black"
                if entl == entw == entx == enty == 0: #entry
                  ent_fill = "None"
                else:
                  ent_fill = "Black"
                if parl == parw == parx == pary == 0: #parking
                  par_fill = "None"
                else:
                  par_fill = "Black"
                if garl == garw == garx == gary == 0: #garden
                  gar_fill = "None"
                else:
                  gar_fill = "Black"
                if foyl == foyw == foyx == foyy == 0: #foyer
                  foy_fill = "None"
                else:
                  foy_fill = "Black"
                if util == utiw == utix == utiy == 0: #utility
                  uti_fill = "None"
                else:
                  uti_fill = "Black"
                if sto2l == sto2w == sto2x == sto2y == 0: #double_store
                  sto2_fill = "None"
                else:
                  sto2_fill = "Black"
                if ots2l == ots2w == ots2x == ots2y == 0: #double_ots
                  ots2_fill = "None"
                else:
                  ots2_fill = "Black"
                if bed2l == bed2w == bed2x == bed2y == 0: # double_bed
                  bed2_fill = "None"
                else:
                  bed2_fill = "Black"
                if washl == washw == washx == washy == 0:
                  wash_fill = "None"
                else:
                  wash_fill = "Black"

                

                userdata3 = CreateProject.objects.filter(user=user_name)

                context = {

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
                  "bed2x":bed2x,  
                  "bed2y":bed2y,
                  "bed2w":bed2w,
                  "bed2l":bed2l,
                  "sto2x":sto2x,
                  "sto2y":sto2y,
                  "sto2w":sto2w,
                  "sto2l":sto2l,
                  "bed_xco":bed_xco,
                  "bed_yco":bed_yco,
                  "roomdata":room_data,
                  "kit_xco":kit_xco,
                  "kit_yco":kit_yco,
                  "draw_xco":draw_xco,
                  "draw_yco":draw_yco,
                  "sta_xco":sta_xco,
                  "sta_yco":sta_yco,
                  "ots2l":ots2l, 
                  "ots2w":ots2w,
                  "ots2x":ots2x,
                  "ots2y":ots2y,
                  "emptyl":emptyl,
                  "emptyw":emptyw,
                  "emptyx":emptyx, 
                  "emptyy":emptyy,
                  "toi_xco":toi_xco,
                  "toi_yco":toi_yco,
                  "wash_xco":wash_xco,
                  "wash_yco":wash_yco,
                  "din_xco":din_xco,
                  "din_yco":din_yco, 
                  "din_fill":din_fill,
                  "ctoi_fill":ctoi_fill,
                  "ctoi_xco":ctoi_xco, "ctoi_yco":ctoi_yco,
                  "sto_fill":sto_fill, "sto_xco":sta_xco, "sto_yco":sto_yco,"ots_fill":ots_fill, "ots_xco":ots_xco, "ots_yco":ots_yco,
                  "ent_xco":ent_xco, "ent_yco":ent_yco, "ent_fill":ent_fill, "par_fill":par_fill, "par_xco":par_xco, "par_yco":par_yco,
                  "gar_fill":gar_fill, "gar_xco":gar_xco, "gar_yco":gar_yco, "foy_fill":foy_fill, "foy_xco":foy_xco, "foy_yco":foy_yco, "uti_xco":uti_xco, "uti_yco":uti_yco, "uti_fill":uti_fill,
                  "sto2_fill":sto2_fill, "sto2_xco":sto2_xco, "sto2_yco":sto2_yco,"ots2_xco":ots2_xco,"ots2_yco":ots2_yco, "ots2_fill":ots2_fill,
                  "bed2_xco":bed2_xco,"bed2_yco":bed2_yco, "bed2_fill":bed2_fill,"wash_fill":wash_fill,
                  "wbedl":wbedl, "wbedw":wbedw, "wbedx":wbedx, "wbedy":wbedy, "wkitl":wkitl, "wkitw":wkitw, "wkitx":wkitx, "wkity":wkity,
                  "wtoil":wtoil, "wtoiw":wtoiw, "wtoix":wtoix , "wtoiy":wtoiy, "wdrawl":wdrawl, "wdraww":wdraww, "wdrawx":wdarwx, "wdrawy":wdrawy,
                  "wstal":wstal, "wstaw":wstaw, "wstax":wstax, "wstay":wstay, "wdinl":wdinl, "wdinw":wdinw, "wdinx":wdinx, "wdiny":wdiny,
                  "wctoil":wctoil, "wctoiw":wctoiw, "wctoix":wctoix, "wctoiy":wctoiy, "wstol":wstol, "wstow":wstow, "wstox":wstox, "wstoy":wstoy,
                  "wotsl":wotsl, "wotsw":wotsw, "wotsx":wotsx, "wotsy":wotsy, "wwashl":wwashl, "wwashw":wwashw, "wwashx":wwashx, "wwashy":wwashy,
                  "wentl":wentl, "wentw":wentw, "wentx":wentx, "wenty":wenty, "wparl":wparl, "wparw":wparw, "wparx":wparx, "wpary":wpary, "wgarl":wgarl, 
                  "wgarw":wgarw, "wgarx":wgarx, "wgary":wgary, "wfoyl":wfoyl, "wfoyw":wfoyw, "wfoyx":wfoyx, "wfoyy":wfoyy, "wutil":wutil, "wutiw":wutiw, "wutix":wutix, "wutiy":wutiy,

                  "wsto2l":wsto2l, "wsto2w":wsto2w, "wsto2x":wsto2x, "wsto2y":wsto2y, "wbed2l":wbed2l, "wbed2w":wbed2w, "wbed2x":wbed2x, "wbed2y":wbed2y, 
                  "wemptyl":wemptyl, "wemptyw":wemptyw, "wemptyx":wemptyx, "wemptyy":wemptyy, "wots2l":wots2l,"wots2w":wots2w, "wots2x":wots2x, "wots2y":wots2y,


                  "dbedl":dbedl, "dbedw":dbedw,"dbedx":dbedx, "dbedy":dbedy,"dkitl":dkitl, "dkitw":dkitw,"dkitx":dkitx,
                  "dkity":dkity, "dtoil":dtoil, "dtoiw":dtoiw, "dtoiy":dtoiy, "ddrawl":ddrawl, "ddraww":ddraww, "ddrawy":ddrawy,
                  "dstal":dstal, "dstaw":dstaw, "dstax":dstax, "dstay":dstay, "ddinl":ddinl,"ddinw":ddinw, "ddinx":ddinx,
                  "ddiny":ddiny, "dctoil":dctoil,"dctoiw":dctoiw,"dctoix":dctoix, "dctoiy":dctoiy, "dstol":dstol, "dstow":dstow, "dstox":dstox, "dstoy":dstoy,
                  "dotsl":dotsl, "dotsw":dotsw, "dotsx":dotsx, "dotsy":dotsy, "dwashl":dwashl, "dwashw":dwashw, "dwashx":dwashx,"dwashy":dwashy,
                  "dentl":dentl, "dentw":dentw, "dentx":dentx, "denty":denty, "dparl":dparl, "dparw":dparw, "dparx":dparx, "dpary":dpary,
                  "dgarl":dgarl, "dgarw":dgarw, "dgarx":dgarx, "dgary":dgary, "dfoyl":dfoyl, "dfoyw":dfoyw, "dfoyx":dfoyx, "dfoyy":dfoyy, 

                  "dutil":dutil, "dutiw":dutiw, "dutix":dutix, "dutiy":dutiy, "dsto2l":dsto2l, "dsto2w":dsto2w, "dsto2x":dsto2x, "dsto2y":dsto2y,
                  "dbed2l":dbed2l, "dbed2w":dbed2w, "dbed2x":dbed2x, "dbed2y":dbed2y, "demptyl":demptyl, "demptyw":demptyw, "demptyx":demptyx, "demptyy":demptyy,
                  "dots2l":dots2l, "dots2w":dots2w, "dots2x":dots2x, "dots2y":dots2y,
                  
                  "forms1":userdata3, "data1": data, "store":store, "ots": ots, "parking":parking,"washarea":washarea, "dressingroom":dressingroom, "utility":utility, "temple":temple, "garden":garden,
                  "match1": match1,
                }  

                #print (context)
                room_context =  Room(bedl=bedl,bedw=bedw,bedx=bedx,bedy=bedy,kitl=kitl,kitw=kitw,kitx=kitx,kity=kity,
                toil=toil,toiw=toiw,toix=toix,toiy=toiy,drawl=drawl,draww=draww,drawx=drawx,drawy=drawy,stal=stal,staw=staw,
                stax=stax, stay=stay,dinl=dinl,dinw=dinw,dinx=dinx,diny=diny,ctoil=ctoil,ctoiw=ctoiw,ctoix=ctoix,ctoiy=ctoiy,
                stol=stol,stow=stow,stox=stox,stoy=stoy,otsl=otsl,otsw=otsw,otsx=otsx,otsy=otsy,washl=washl,washw=washw,
                washx=washx,washy=washy,entl=entl,entw=entw,entx=entx,enty=enty,parl=parl,parw=parw,parx=parx,pary=pary,garl=garl, 
                garw=garw,garx=garx,gary=gary,foyl=foyl,foyw=foyw,foyx=foyx,foyy=foyy,util=util,utiw=utiw,utix=utix,utiy=utiy,sto2l=sto2l,
                sto2w=sto2w,sto2x=sto2x,sto2y=sto2y,bed2l=bed2l,bed2w=bed2w,bed2x=bed2x,bed2y=bed2y,bed_xco=bed_xco,bed_yco=bed_yco,kit_xco=kit_xco,kit_yco=kit_yco,
                draw_xco=draw_xco,draw_yco=draw_yco,sta_xco=sta_xco,sta_yco=sta_yco,ots2l=ots2l,ots2w=ots2w,ots2x=ots2x,ots2y=ots2y,
                emptyl=emptyl,emptyw=emptyw,emptyx=emptyx,emptyy=emptyy,toi_xco=toi_xco,toi_yco=toi_yco,wash_xco=wash_xco,wash_yco=wash_yco,din_xco=din_xco,
                din_yco=din_yco, ctoi_xco=ctoi_xco,ctoi_yco=ctoi_yco,sto_xco=sto_xco,sto_yco=sto_yco,ots_xco=ots_xco,
                ots_yco=ots_yco,par_xco=par_xco,par_yco=par_yco,ent_xco=ent_xco,ent_yco=ent_yco,gar_xco=gar_xco,gar_yco=gar_yco,
                foy_xco=foy_xco,foy_yco=foy_yco,uti_xco=uti_xco,uti_yco=uti_yco,sto2_xco=sto2_xco,sto2_yco=sto2_yco,ots2_xco=ots2_xco,
                ots2_yco=ots2_yco,bed2_xco=bed2_xco,bed2_yco=bed2_yco )

                check_print = room_context.save()
                #user_del = Room.objects.filter(bedl=bedl).delete()
                
                print (check_print)
                
                return render(request, 'toolbar.html', context)

                       
        return render(request,'createproject.html',{"udata":User.objects.filter(email=request.session['uid']),"date":datetime.now()})

def toolbar(request):
  
          
  return render(request,'toolbar.html')
 

def layout_download(request) :
  
  if request.session.has_key('uid'): 
    room_dict = Room.objects.all()
    print(room_dict)
    #ratio = 10
  
  
    for r in room_dict:

      bedl = (r.bedl/10)
      bedw = (r.bedw/10)
      bedx = (r.bedx/10)
      bedy = (r.bedy/10)
      kitl = (r.kitl/10) 
      kitw = (r.kitw/10) 
      kitx = (r.kitx/10)
      kity = (r.kity/10)
      toil = (r.toil/10)
      toiw = (r.toiw/10)
      toix = (r.toix/10) 
      toiy = (r.toiy/10)
      drawl = (r.drawl/10) 
      draww = (r.draww/10) 
      drawx = (r.drawx/10) 
      drawy = (r.drawy/10)
      stal =  (r.stal/10) 
      staw = (r.staw/10) 
      stax = (r.stax/10)
      stay = (r.stay/10)
      dinl = (r.dinl/10) 
      dinx = (r.dinx/10) 
      diny = (r.diny/10)
      dinw = (r.dinw/10)
      ctoil = (r.ctoil/10) 
      ctoiw = (r.ctoiw/10) 
      ctoix = (r.ctoix/10)
      ctoiy = (r.ctoiy/10)
      stol = (r.stol/10) 
      stow = (r.stow/10) 
      stox = (r.stox/10) 
      stoy = (r.stoy/10)
      otsl = (r.otsl/10) 
      otsw = (r.otsw/10)
      otsx = (r.otsx/10) 
      otsy = (r.otsy/10)
      washl = (r.washl/10) 
      washw = (r.washw/10) 
      washx = (r.washx/10) 
      washy = (r.washy/10)
      entl = (r.entl/10) 
      entw = (r.entw/10)
      entx = (r.entx/10) 
      enty = (r.enty/10)
      parl = (r.parl/10) 
      parw = (r.parw/10)
      parx = (r.parx/10) 
      pary = (r.pary/10)
      garl = (r.garl/10) 
      garw = (r.garw/10)
      garx = (r.garx/10) 
      gary = (r.gary/10)
      foyl = (r.foyl/10) 
      foyw = (r.foyw/10)
      foyx = (r.foyx/10) 
      foyy = (r.foyy/10)
      util = (r.util/10) 
      utiw = (r.utiw/10) 
      utix = (r.utix/10) 
      utiy = (r.utiy/10)
      sto2l = (r.sto2l/10)
      sto2w = (r.sto2w/10)
      sto2x = (r.sto2x/10)
      sto2y = (r.sto2y/10)
      bed2l = (r.bed2l/10) 
      bed2w = (r.bed2w/10) 
      bed2x = (r.bed2x/10) 
      bed2y = (r.bed2y/10)
      bed_xco = (r.bed_xco/10)
      bed_yco = (r.bed_yco/10)
      kit_xco = (r.kit_xco/10)
      kit_yco = (r.kit_yco/10)
      draw_xco = (r.draw_xco/10)
      draw_yco = (r.draw_yco/10)
      sta_xco = (r.sta_xco/10)
      sta_yco = (r.sta_yco/10)
      ots2l = (r.ots2l/10)
      ots2w = (r.ots2w/10)
      ots2x = (r.ots2x/10)
      ots2y = (r.ots2y/10)
      emptyl = (r.emptyl/10)
      emptyw = (r.emptyw/10)
      emptyx = (r.emptyx/10)
      emptyy = (r.emptyy/10)
      toi_xco = (r.toi_xco/10)
      toi_yco = (r.toi_yco/10)
      wash_xco = (r.wash_xco/10)
      wash_yco = (r.wash_yco/10)
      din_xco = (r.din_xco/10)
      din_yco = (r.din_yco/10)
      ctoi_xco = (r.ctoi_xco/10)
      ctoi_yco = (r.ctoi_yco/10)
      sto_xco = (r.sto_xco/10)
      sto_yco = (r.sto_yco/10)
      ots_xco = (r.ots_xco/10)
      ots_yco = (r.ots_yco/10)
      par_xco = (r.par_xco/10)
      par_yco = (r.par_yco/10)
      ent_xco = (r.ent_xco/10)
      ent_yco = (r.ent_yco/10)
      gar_xco = (r.gar_xco/10)
      gar_yco = (r.gar_yco/10)
      foy_xco = (r.foy_xco/10)
      foy_yco = (r.foy_yco/10)
      uti_xco = (r.uti_xco/10)
      uti_yco = (r.uti_yco/10)
      sto2_xco = (r.sto2_xco/10)
      sto2_yco = (r.sto2_yco/10)
      ots2_xco = (r.ots2_xco/10)
      ots2_yco = (r.ots2_yco/10)
      bed2_xco = (r.bed2_xco/10)
      bed2_yco = (r.bed2_yco/10)


      from dxfwrite import DXFEngine as dxf
      import random
      import os
      import datetime
      now = datetime.datetime.now()
      currentDate = str(now.strftime("%S"))+"_"  + str(now.month) +  "_" + str(now.year)
      name=f"Layout_{currentDate}.dxf"
      drawing = dxf.drawing(name)

      # rectangle for elements
      drawing.add(dxf.rectangle((bedx, bedy),bedw,bedl,color=7))
      drawing.add(dxf.rectangle((kitx, kity) ,kitw,kitl,color=7))
      drawing.add(dxf.rectangle((toix, toiy) ,toiw,toil,color=7))
      drawing.add(dxf.rectangle((drawx, drawy) ,draww,drawl,color=7))
      drawing.add(dxf.rectangle((stax, stay) ,staw,stal,color=7))
      drawing.add(dxf.rectangle((dinx, diny) ,dinw,dinl,color=7))
      drawing.add(dxf.rectangle((ctoix, ctoiy) ,ctoiw,ctoil,color=7))
      drawing.add(dxf.rectangle((stox, stoy) ,stow,stol,color=7))
      drawing.add(dxf.rectangle((washx, washy) ,washw,washl,color=7))
      drawing.add(dxf.rectangle((entx, enty) ,entw,entl,color=7))


      drawing.add(dxf.rectangle((parx, pary) ,parw,parl,color=7))
      drawing.add(dxf.rectangle((garx, gary) ,garw,garl,color=7))
      drawing.add(dxf.rectangle((foyx, foyy) ,foyw,foyl,color=7))
      drawing.add(dxf.rectangle((utix, utiy) ,utiw,util,color=7))
      drawing.add(dxf.rectangle((ots2x, ots2y) ,ots2w,ots2l,color=7))
      drawing.add(dxf.rectangle((bed2x, bed2y) ,bed2w,bed2l,color=7))
      drawing.add(dxf.rectangle((emptyx,emptyy) ,emptyw,emptyl,color=7))
      drawing.add(dxf.rectangle((sto2x, sto2y) ,sto2w,sto2l,color=7))
      # coordinates for text
      bed_xco = bedx + (bedw/2.5)
      bed_yco = bedy + (bedl/2)
      kit_xco = kitx + (kitw/2.5)
      kit_yco = kity + (kitl/2)
      toi_xco = toix + (toiw/2.5)
      toi_yco = toiy + (toil/2)
      draw_xco = drawx + (draww/2.5)
      draw_yco = drawy + (drawl/2)
      sta_xco = stax + (staw/2.5)
      sta_yco = stay + (stal/2)

      # Text 
      drawing.add(dxf.text('Bedroom', (bed_xco,bed_yco ),height=0.6,rotation =180))
      drawing.add(dxf.text('kitchen', (kit_xco,kit_yco),height=0.6,rotation =180))
      drawing.add(dxf.text('Toilet', (toi_xco,toi_yco ),height=0.6,rotation =180))
      drawing.add(dxf.text('Drawing', (draw_xco,draw_yco ),height=0.6,rotation =180))
      drawing.add(dxf.text('Stairs', (sta_xco,sta_yco),height=0.6,rotation =180))

      # Displaying text if condition is meet
      if (ctoiw and ctoil is not 0):
        ctoi_xco = ctoix + (ctoiw/2.5)
        ctoi_yco = ctoiy + (ctoil/2)
        drawing.add(dxf.text('Toilet', (ctoi_xco,ctoi_yco ),height=0.6,rotation =180))
      if (dinw and dinl is not 0):
        din_xco = dinx + (dinw/2.5)
        din_yco = diny + (dinl/2)
        drawing.add(dxf.text('Dining', (din_xco,din_yco),height=0.6,rotation =180))
      if (stow and stol is not 0):
        sto_xco = stox + (stow/2.5)
        sto_yco = stoy + (stol/2)
        drawing.add(dxf.text('Store', (sto_xco,sto_yco),height=0.6,rotation =180))
      if (otsw and otsl is not 0):
        ots_xco = otsx + (otsw/2.5)
        ots_yco = otsy + (otsl/2)
        drawing.add(dxf.text('Ots', (ots_xco,ots_yco ),height=0.6,rotation =180))
      if (washw and washl is not 0):
        wash_xco = washx + (washw/2.5)
        wash_yco = washy + (washl/2)
        drawing.add(dxf.text('Wash', (wash_xco,wash_yco),height=0.6,rotation =180))
      if (entw and entl is not 0):
        ent_xco = entx + (entw/2.5)
        ent_yco = enty + (entl/2)
        drawing.add(dxf.text('Entry', (ent_xco,ent_yco),height=0.6,rotation =180))
      if (parw and parl is not 0):
        par_xco = parx + (parw/2.5)
        par_yco = pary + (parl/2)
        drawing.add(dxf.text('Parking', (par_xco,par_yco),height=0.6,rotation =180))
      if (garw and garl is not 0):
        gar_xco = garx + (garw/2.5)
        gar_yco = gary + (garl/2)
        drawing.add(dxf.text('Garden', (gar_xco,gar_yco ),height=0.6,rotation =180))
      if (foyw and foyl is not 0):
        foy_xco = foyx + (foyw/2.5)
        foy_yco = foyy + (foyl/2)
        drawing.add(dxf.text('Foyer', (foy_xco,foy_yco),height=0.6,rotation =180))
      if (utiw and util is not 0):
        uti_xco = utix + (utiw/2.5)
        uti_yco = utiy + (util/2)
        drawing.add(dxf.text('Utility', (uti_xco,uti_yco),height=0.6,rotation =180))
      if (sto2w and sto2l is not 0):
        sto2_xco = sto2x + (sto2w/2.5)
        sto2_yco = sto2y + (sto2l/2)
        drawing.add(dxf.text('Store', (sto2_xco,sto2_yco ),height=0.6,rotation =180))
      if (ots2w and ots2l is not 0):
        ots2_xco = ots2x + (ots2w/2.5)
        ots2_yco = ots2y + (ots2l/2)
        drawing.add(dxf.text('Ots', (ots2_xco,ots2_yco),height=0.6,rotation =180))
      if (bed2w and bed2l is not 0):
        bed2_xco = bed2x + (bed2w/2.5)
        bed2_yco = bed2y + (bed2l/2)
        drawing.add(dxf.text('Bedroom', (bed2_xco,bed2_yco),height=0.6,rotation =180))


      drawing.save()
      print("drawing '%s' created.\n" % name)

      return redirect('/toolbar')


    
    

  
    
  
  
      
  
def cardfilter(request):
    if request.session.has_key('uid'): 
        return render(request,'cardfilter.html',{"udata":User.objects.filter(email=request.session['uid']),"date":datetime.now()})
    else:
        return('/')
        
def autocadexprt(request):
    return render(request,'toolbar.html')
