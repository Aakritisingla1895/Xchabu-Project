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
import psycopg2
import numpy as np
import itertools 
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
                print (layout_no)

              
              connection = psycopg2.connect(
              host = 'xchaburoom.cmpbnicytdnf.us-east-2.rds.amazonaws.com',
              port = '5432',
              user = 'xchaburoom',
              password = 'xchabupassword',
              database='xchaburoom',
              )
              print ("Room_DB is connected successfully")

              raw_query = "SELECT * FROM {} ".format(user_direction)
              print(layout_no)
              cursor = connection.cursor()
              cursor.execute(raw_query)
              layout_list = cursor.fetchall()
              #print (layout_list)

              connection = psycopg2.connect(
              host = 'xchabudoor.cmpbnicytdnf.us-east-2.rds.amazonaws.com',
              port = '5432',
              user = 'xchabudoor',
              password = 'xchabupassword',
              database='xchabudoor',
              )
              print ("Door_DB is connected successfully")

              raw_door_query = "SELECT * FROM {} ".format(user_direction)
              print(layout_no)
              door_cursor = connection.cursor()
              door_cursor.execute(raw_door_query)
              door_list = door_cursor.fetchall()
              #print (door_list)
              

              connection = psycopg2.connect(
              host = 'xchabuwall.cmpbnicytdnf.us-east-2.rds.amazonaws.com',
              port = '5432',
              user = 'xchabuwall',
              password = 'xchabupassword',
              database='xchabuwall',
              )
              print ("Wall_DB is connected successfully")

              raw_wall_query = "SELECT * FROM {} ".format(user_direction)
              #print(layout_no)
              wall_cursor = connection.cursor()
              wall_cursor.execute(raw_wall_query)
              wall_list = wall_cursor.fetchall()
              #print (wall_list)

              suggested_layout_list = []

              layout_list1 = list(sum(layout_list, ()))
              from difflib import get_close_matches

              match1 = get_close_matches(layout_no, layout_list1)
              for x12 in match1:
                print(match1)
                #suggested_layout_list = list((match1[1], match1[2]))
                #print (suggested_layout_list)

                sg_1 = match1[1]
                print (sg_1)
                sg_2 = match1[2]
                print (sg_2)
                break
              
                
              sql_query1 = "SELECT * from {0} where layoutno = '{1}' ".format(user_direction, x12)
              
              room_data2 = cursor.execute(sql_query1)
              room_data = cursor.fetchall()
              print (room_data)
                
              sql_query_sg1 = "SELECT * from {0} where layoutno = '{1}' ".format(user_direction, sg_1)
              sq1_data2 = cursor.execute(sql_query_sg1)
              sq1_data = cursor.fetchall()
              print (sq1_data)


              door_data2 = door_cursor.execute(sql_query1)
              door_data = door_cursor.fetchall()
              #print(door_data)
                         

              wall_data2 = wall_cursor.execute(sql_query1)
              wall_data = wall_cursor.fetchall()
              #print(wall_data)

              ratio = 10
              room_list = []
             
              for item in room_data:
                #print(list(item))
                bedl = (eval(item[1])*10)
                bedw = (eval(item[2])*10)
                bedx = (eval(item[3])*10)
                bedy = (eval(item[4])*10)
                kitl = (eval(item[5])*10)
                kitw = (eval(item[6])*10)
                kitx = (eval(item[7])*10)
                kity = (eval(item[8])*10)
                toil = (eval(item[9])*10)
                toiw = (eval(item[10])*10)
                toix = (eval(item[11])*10)
                toiy = (eval(item[12])*10)
                drawl = (eval(item[13])*10)
                draww = (eval(item[14])*10)
                drawx = (eval(item[15])*10)
                drawy = (eval(item[16])*10)
                stal = (eval(item[17])*10)
                staw = (eval(item[18])*10)
                stax = (eval(item[19])*10)
                stay = (eval(item[20])*10)
                dinl = (eval(item[21])*10)
                dinw = (eval(item[22])*10)
                dinx = (eval(item[23])*10)
                diny = (eval(item[24])*10)
                ctoil = (eval(item[25])*10)
                ctoiw = (eval(item[26])*10)
                ctoix = (eval(item[27])*10)
                ctoiy = (eval(item[28])*10)
                stol = (eval(item[29])*10)
                stow = (eval(item[30])*10)
                stox = (eval(item[31])*10)
                stoy = (eval(item[32])*10)
                otsl = (eval(item[33])*10)
                otsw = (eval(item[34])*10)
                otsx = (eval(item[35])*10)
                otsy = (eval(item[36])*10)
                washl = (eval(item[37])*10)
                washw = (eval(item[38])*10)
                washx = (eval(item[39])*10)
                washy = (eval(item[40])*10)
                entl = (eval(item[41])*10)
                entw = (eval(item[42])*10)
                entx = (eval(item[43])*10)
                enty = (eval(item[44])*10)
                parl = (eval(item[45])*10)
                parw = (eval(item[46])*10)
                parx = (eval(item[47])*10)
                pary = (eval(item[48])*10)
                garl = (eval(item[49])*10)
                garw = (eval(item[50])*10)
                garx = (eval(item[51])*10)
                gary = (eval(item[52])*10)
                foyl = (eval(item[53])*10)
                foyw = (eval(item[54])*10)
                foyx = (eval(item[55])*10)
                foyy = (eval(item[56])*10)
                util = (eval(item[57])*10)
                utiw = (eval(item[58])*10)
                utix = (eval(item[59])*10)
                utiy = (eval(item[60])*10)
                sto2l = (eval(item[61])*10)
                sto2w = (eval(item[62])*10)
                sto2x = (eval(item[63])*10)
                sto2y = (eval(item[64])*10)
                bed2l = (eval(item[65])*10)
                bed2w = (eval(item[66])*10)
                bed2x = (eval(item[67])*10)
                bed2y = (eval(item[68])*10)
                emptyl = (eval(item[69])*10)
                emptyw = (eval(item[70])*10)
                emptyx = (eval(item[71])*10)
                emptyy = (eval(item[72])*10)
                ots2l = (eval(item[73])*10)
                ots2w = (eval(item[74])*10)
                ots2x = (eval(item[75])*10)
                ots2y = (eval(item[76])*10)

                room_list.append(item)
                #print (room_list)

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
                
                for d in door_data:

                  dbedl = (eval(d[1])*10)
                  dbedw = (eval(d[2])*10)
                  dbedx = (eval(d[3])*10)
                  dbedy = (eval(d[4])*10)
                  dkitl = (eval(d[5])*10)
                  dkitw = (eval(d[6])*10)
                  dkitx = (eval(d[7])*10)
                  dkity = (eval(d[8])*10)
                  dtoil = (eval(d[9])*10)
                  dtoiw = (eval(d[10])*10)
                  dtoix = (eval(d[11])*10)
                  dtoiy = (eval(d[12])*10)
                  ddrawl = (eval(d[13])*10)
                  ddraww = (eval(d[14])*10)
                  ddarwx = (eval(d[15])*10)
                  ddrawy = (eval(d[16])*10)
                  dstal = (eval(d[17])*10)
                  dstaw = (eval(d[18])*10)
                  dstax = (eval(d[19])*10)
                  dstay = (eval(d[20])*10)
                  ddinl = (eval(d[21])*10)
                  ddinw = (eval(d[22])*10)
                  ddinx = (eval(d[23])*10)
                  ddiny = (eval(d[24])*10)
                  dctoil = (eval(d[25])*10)
                  dctoiw = (eval(d[26])*10)
                  dctoix = (eval(d[27])*10)
                  dctoiy = (eval(d[28])*10)
                  dstol = (eval(d[29])*10)
                  dstow = (eval(d[30])*10)
                  dstox = (eval(d[31])*10)
                  dstoy = (eval(d[32])*10)
                  dotsl = (eval(d[33])*10)
                  dotsw = (eval(d[34])*10)
                  dotsx = (eval(d[35])*10)
                  dotsy = (eval(d[36])*10)
                  dwashl = (eval(d[37])*10)
                  dwashw = (eval(d[38])*10)
                  dwashx = (eval(d[39])*10)
                  dwashy = (eval(d[40])*10)
                  dentl = (eval(d[41])*10)
                  dentw = (eval(d[42])*10)
                  dentx = (eval(d[43])*10)
                  denty = (eval(d[44])*10)
                  dparl = (eval(d[45])*10)
                  dparw = (eval(d[46])*10)
                  dparx = (eval(d[47])*10)
                  dpary = (eval(d[48])*10)
                  dgarl = (eval(d[49])*10)
                  dgarw = (eval(d[50])*10)
                  dgarx = (eval(d[51])*10)
                  dgary = (eval(d[52])*10)
                  dfoyl = (eval(d[53])*10)
                  dfoyw = (eval(d[54])*10)
                  dfoyx = (eval(d[55])*10)
                  dfoyy = (eval(d[56])*10)
                  dutil = (eval(d[57])*10)
                  dutiw = (eval(d[58])*10)
                  dutix = (eval(d[59])*10)
                  dutiy = (eval(d[60])*10)
                  dsto2l = (eval(d[61])*10)
                  dsto2w = (eval(d[62])*10)
                  dsto2x = (eval(d[63])*10)
                  dsto2y = (eval(d[64])*10)
                  dbed2l = (eval(d[65])*10)
                  dbed2w = (eval(d[66])*10)
                  dbed2x = (eval(d[67])*10)
                  dbed2y = (eval(d[68])*10)
                  demptyl = (eval(d[69])*10)
                  demptyw = (eval(d[70])*10)
                  demptyx = (eval(d[71])*10)
                  demptyy = (eval(d[72])*10)
                  dots2l = (eval(d[73])*10)
                  dots2w = (eval(d[74])*10)
                  dots2x = (eval(d[75])*10)
                  dots2y = (eval(d[76])*10)
                
                for w in wall_data:

                  wbedl = (eval(w[1])*10)
                  wbedw = (eval(w[2])*10)
                  wbedx = (eval(w[3])*10)
                  wbedy = (eval(w[4])*10)
                  wkitl = (eval(w[5])*10)
                  wkitw = (eval(w[6])*10)
                  wkitx = (eval(w[7])*10)
                  wkity = (eval(w[8])*10)
                  wtoil = (eval(w[9])*10)
                  wtoiw = (eval(w[10])*10)
                  wtoix = (eval(w[11])*10)
                  wtoiy = (eval(w[12])*10)
                  wdrawl = (eval(w[13])*10)
                  wdraww = (eval(w[14])*10)
                  wdarwx = (eval(w[15])*10)
                  wdrawy = (eval(w[16])*10)
                  wstal = (eval(w[17])*10)
                  wstaw = (eval(w[18])*10)
                  wstax = (eval(w[19])*10)
                  wstay = (eval(w[20])*10)
                  wdinl = (eval(w[21])*10)
                  wdinw = (eval(w[22])*10)
                  wdinx = (eval(w[23])*10)
                  wdiny = (eval(w[24])*10)
                  wctoil = (eval(w[25])*10)
                  wctoiw = (eval(w[26])*10)
                  wctoix = (eval(w[27])*10)
                  wctoiy = (eval(w[28])*10)
                  wstol = (eval(w[29])*10)
                  wstow = (eval(w[30])*10)
                  wstox = (eval(w[31])*10)
                  wstoy = (eval(w[32])*10)
                  wotsl = (eval(w[33])*10)
                  wotsw = (eval(w[34])*10)
                  wotsx = (eval(w[35])*10)
                  wotsy = (eval(w[36])*10)
                  wwashl = (eval(w[37])*10)
                  wwashw = (eval(w[38])*10)
                  wwashx = (eval(w[39])*10)
                  wwashy = (eval(w[40])*10)
                  wentl = (eval(w[41])*10)
                  wentw = (eval(w[42])*10)
                  wentx = (eval(w[43])*10)
                  wenty = (eval(w[44])*10)
                  wparl = (eval(w[45])*10)
                  wparw = (eval(w[46])*10)
                  wparx = (eval(w[47])*10)
                  wpary = (eval(w[48])*10)
                  wgarl = (eval(w[49])*10)
                  wgarw = (eval(w[50])*10)
                  wgarx = (eval(w[51])*10)
                  wgary = (eval(w[52])*10)
                  wfoyl = (eval(w[53])*10)
                  wfoyw = (eval(w[54])*10)
                  wfoyx = (eval(w[55])*10)
                  wfoyy = (eval(w[56])*10)
                  wutil = (eval(w[57])*10)
                  wutiw = (eval(w[58])*10)
                  wutix = (eval(w[59])*10)
                  wutiy = (eval(w[60])*10)
                  wsto2l = (eval(w[61])*10)
                  wsto2w = (eval(w[62])*10)
                  wsto2x = (eval(w[63])*10)
                  wsto2y = (eval(w[64])*10)
                  wbed2l = (eval(w[65])*10)
                  wbed2w = (eval(w[66])*10)
                  wbed2x = (eval(w[67])*10)
                  wbed2y = (eval(w[68])*10)
                  wemptyl = (eval(w[69])*10)
                  wemptyw = (eval(w[70])*10)
                  wemptyx = (eval(w[71])*10)
                  wemptyy = (eval(w[72])*10)
                  wots2l = (eval(w[73])*10)
                  wots2w = (eval(w[74])*10)
                  wots2x = (eval(w[75])*10)
                  wots2y = (eval(w[76])*10)
                

                for item in sq1_data:
                #print(list(item))
                  s1_bedl = (eval(item[1])*10)
                  s1_bedw = (eval(item[2])*10)
                  s1_bedx = (eval(item[3])*10)
                  s1_bedy = (eval(item[4])*10)
                  s1_kitl = (eval(item[5])*10)
                  s1_kitw = (eval(item[6])*10)
                  s1_kitx = (eval(item[7])*10)
                  s1_kity = (eval(item[8])*10)
                  s1_toil = (eval(item[9])*10)
                  s1_toiw = (eval(item[10])*10)
                  s1_toix = (eval(item[11])*10)
                  s1_toiy = (eval(item[12])*10)
                  s1_drawl = (eval(item[13])*10)
                  s1_draww = (eval(item[14])*10)
                  s1_drawx = (eval(item[15])*10)
                  s1_drawy = (eval(item[16])*10)
                  s1_stal = (eval(item[17])*10)
                  s1_staw = (eval(item[18])*10)
                  s1_stax = (eval(item[19])*10)
                  s1_stay = (eval(item[20])*10)
                  s1_dinl = (eval(item[21])*10)
                  s1_dinw = (eval(item[22])*10)
                  s1_dinx = (eval(item[23])*10)
                  s1_diny = (eval(item[24])*10)
                  s1_ctoil = (eval(item[25])*10)
                  s1_ctoiw = (eval(item[26])*10)
                  s1_ctoix = (eval(item[27])*10)
                  s1_ctoiy = (eval(item[28])*10)
                  s1_stol = (eval(item[29])*10)
                  s1_stow = (eval(item[30])*10)
                  s1_stox = (eval(item[31])*10)
                  s1_stoy = (eval(item[32])*10)
                  s1_otsl = (eval(item[33])*10)
                  s1_otsw = (eval(item[34])*10)
                  s1_otsx = (eval(item[35])*10)
                  s1_otsy = (eval(item[36])*10)
                  s1_washl = (eval(item[37])*10)
                  s1_washw = (eval(item[38])*10)
                  s1_washx = (eval(item[39])*10)
                  s1_washy = (eval(item[40])*10)
                  s1_entl = (eval(item[41])*10)
                  s1_entw = (eval(item[42])*10)
                  s1_entx = (eval(item[43])*10)
                  s1_enty = (eval(item[44])*10)
                  s1_parl = (eval(item[45])*10)
                  s1_parw = (eval(item[46])*10)
                  s1_parx = (eval(item[47])*10)
                  s1_pary = (eval(item[48])*10)
                  s1_garl = (eval(item[49])*10)
                  s1_garw = (eval(item[50])*10)
                  s1_garx = (eval(item[51])*10)
                  s1_gary = (eval(item[52])*10)
                  s1_foyl = (eval(item[53])*10)
                  s1_foyw = (eval(item[54])*10)
                  s1_foyx = (eval(item[55])*10)
                  s1_foyy = (eval(item[56])*10)
                  s1_util = (eval(item[57])*10)
                  s1_utiw = (eval(item[58])*10)
                  s1_utix = (eval(item[59])*10)
                  s1_utiy = (eval(item[60])*10)
                  s1_sto2l = (eval(item[61])*10)
                  s1_sto2w = (eval(item[62])*10)
                  s1_sto2x = (eval(item[63])*10)
                  s1_sto2y = (eval(item[64])*10)
                  s1_bed2l = (eval(item[65])*10)
                  s1_bed2w = (eval(item[66])*10)
                  s1_bed2x = (eval(item[67])*10)
                  s1_bed2y = (eval(item[68])*10)
                  s1_emptyl = (eval(item[69])*10)
                  s1_emptyw = (eval(item[70])*10)
                  s1_emptyx = (eval(item[71])*10)
                  s1_emptyy = (eval(item[72])*10)
                  s1_ots2l = (eval(item[73])*10)
                  s1_ots2w = (eval(item[74])*10)
                  s1_ots2x = (eval(item[75])*10)
                  s1_ots2y = (eval(item[76])*10)

                  room_list.append(item)
                  #print (room_list)

                  # coordinates for text for layout 1
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
  
                

                # for layout 1 optional amenities, looping condition............................

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


                  #################layout 2...............
                   # coordinates for text for layout 2
                  s1_bed_xco = s1_bedx + (s1_bedw/4)
                  s1_bed_yco = s1_bedy + (s1_bedl/3)
                  s1_kit_xco = s1_kitx + (s1_kitw/4)
                  s1_kit_yco = s1_kity + (s1_kitl/3)
                  s1_toi_xco = s1_toix + (s1_toiw/4)
                  s1_toi_yco = s1_toiy + (s1_toil/3)
                  s1_draw_xco = s1_drawx + (s1_draww/4)
                  s1_draw_yco = s1_drawy + (s1_drawl/3)
                  #s1_sta_xco = s1_stax + (s1_staw/6)
                  s1_sta_yco = s1_stay + (s1_stal/3)
                  s1_wash_xco = s1_washx + (s1_washw/3)
                  s1_wash_yco = s1_washy + (s1_washl/3)


                  s1_din_xco = s1_dinx + (s1_dinw/4)     #  text coordinates for DINNING 
                  s1_din_yco = s1_diny + (s1_dinl/3)
                  s1_ctoi_xco = s1_ctoix + (s1_ctoiw/2)  #  text coordinates for TOILET 
                  s1_ctoi_yco = s1_ctoiy + (s1_ctoil/3)
                  s1_sto_xco = s1_stox + (s1_stow/2)
                  s1_sto_yco = s1_stoy + (s1_stol/3)
                  s1_ots_xco = s1_otsx + (s1_otsw/4)     #  text coordinates for OTS
                  s1_ots_yco = s1_otsy + (s1_otsl/3)
                  s1_ent_xco = s1_bedx + (s1_entw/4)     #  text coordinates for ENTRY
                  s1_ent_yco = s1_bedy + (s1_entl/3)
                  s1_par_xco = s1_parx + (s1_parw/4)     #  text coordinates for PARKING
                  s1_par_yco = s1_pary + (s1_parl/3)
                  s1_gar_xco = s1_garx + (s1_garw/4)     #  text coordinates for GARDEN
                  s1_gar_yco = s1_gary + (s1_garl/3)
                  s1_foy_xco = s1_foyx + (s1_foyw/4)     #  text coordinates for FOYER
                  s1_foy_yco = s1_foyy + (s1_foyl/3)
                  s1_uti_xco = s1_utix + (s1_utiw/4)     #  text coordinates for UTILITY
                  s1_uti_yco = s1_utiy + (s1_util/3)
                  s1_sto2_xco = s1_sto2x + (s1_sto2w/4)  #  text coordinates for DOUBLE_STORE
                  s1_sto2_yco = s1_sto2y + (s1_sto2l/3)
                  s1_ots2_xco = s1_ots2x + (s1_ots2w/4)   #  text coordinates for DOUBLE_OTS
                  s1_ots2_yco = s1_ots2y + (s1_ots2l/3)
                  s1_bed2_xco = s1_bed2x + (s1_bed2w/4)   #  text coordinates for DOUBLE_BED
                  s1_bed2_yco = s1_bed2y + (s1_bed2l/3)
                  s1_ent_xco = s1_entx + (s1_entw/4)      #  text coordinates for ENTRY
                  s1_ent_yco = s1_enty + (s1_entl/3)
                 
  
                # for layout 2 optional amenities, looping condition............................

                if s1_dinx == s1_diny == s1_dinl == s1_dinw == 0: #dinning
                  s1_din_fill = "None"
                else:
                  s1_din_fill = "Black"
               
                if s1_ctoil == s1_ctoiw == s1_ctoix == s1_ctoiy == 0: #toilet
                  s1_ctoi_fill = "None"
                else:
                  s1_ctoi_fill = "Black"
                if s1_stol == s1_stow == s1_stox == s1_stoy == 0: #store
                  s1_sto_fill ="None"
                else:
                  s1_sto_fill = "Black"
                if s1_otsl == s1_otsw == s1_otsx == s1_otsy == 0: #ots
                  s1_ots_fill ="None"
                else:
                  s1_ots_fill = "Black"
                if s1_entl == s1_entw == s1_entx == s1_enty == 0: #entry
                  s1_ent_fill = "None"
                else:
                  s1_ent_fill = "Black"
                if s1_parl == s1_parw == s1_parx == s1_pary == 0: #parking
                  s1_par_fill = "None"
                else:
                  s1_par_fill = "Black"
                if s1_garl == s1_garw == s1_garx == s1_gary == 0: #garden
                  s1_gar_fill = "None"
                else:
                  gar_fill = "Black"
                if s1_foyl == s1_foyw == s1_foyx == s1_foyy == 0: #foyer
                  s1_foy_fill = "None"
                else:
                  s1_foy_fill = "Black"
                if s1_util == s1_utiw == s1_utix == s1_utiy == 0: #utility
                  s1_uti_fill = "None"
                else:
                  s1_uti_fill = "Black"
                if s1_sto2l == s1_sto2w == s1_sto2x == s1_sto2y == 0: #double_store
                  s1_sto2_fill = "None"
                else:
                  s1_sto2_fill = "Black"
                if s1_ots2l == s1_ots2w == s1_ots2x == s1_ots2y == 0: #double_ots
                  s1_ots2_fill = "None"
                else:
                  s1_ots2_fill = "Black"
                if s1_bed2l == s1_bed2w == s1_bed2x == s1_bed2y == 0: # double_bed
                  s1_bed2_fill = "None"
                else:
                  bed2_fill = "Black"
                if s1_washl == s1_washw == s1_washx == s1_washy == 0:
                  s1_wash_fill = "None"
                else:
                  s1_wash_fill = "Black"

                userdata3 = CreateProject.objects.filter(user=user_name)

                layout_a = 'layout1'
                layout_b = 'layout2'
                #layout_c = 'layout3'

                layout_one =  Room(bedl=bedl,bedw=bedw,bedx=bedx,bedy=bedy,kitl=kitl,kitw=kitw,kitx=kitx,kity=kity,
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
                ots2_yco=ots2_yco,bed2_xco=bed2_xco,bed2_yco=bed2_yco)

                layout_two =  Room(bedl=s1_bedl, bedw=s1_bedw, bedx=s1_bedx, bedy=s1_bedy, kitl=s1_kitl, kitw=s1_kitw, kitx=s1_kitx, kity=s1_kity,
                toil=s1_toil, toiw=s1_toiw, toix=s1_toix,toiy=s1_toiy,drawl=s1_drawl,draww=s1_draww,drawx=s1_drawx,drawy=s1_drawy,stal=s1_stal,staw=s1_staw,
                stax=s1_stax, stay=s1_stay,dinl=s1_dinl,dinw=s1_dinw,dinx=s1_dinx,diny=s1_diny,ctoil=s1_ctoil,ctoiw=s1_ctoiw,ctoix=s1_ctoix,ctoiy=s1_ctoiy,
                stol=s1_stol,stow=s1_stow,stox=s1_stox,stoy=s1_stoy,otsl=s1_otsl,otsw=s1_otsw,otsx=s1_otsx,otsy=s1_otsy,washl=s1_washl,washw=s1_washw,
                washx=s1_washx,washy=s1_washy,entl=s1_entl,entw=s1_entw,entx=s1_entx,enty=s1_enty,parl=s1_parl,parw=s1_parw,parx=s1_parx,pary=s1_pary,garl=s1_garl, 
                garw=s1_garw,garx=s1_garx,gary=s1_gary,foyl=s1_foyl,foyw=s1_foyw,foyx=s1_foyx,foyy=s1_foyy,util=s1_util,utiw=s1_utiw,utix=s1_utix,utiy=s1_utiy,sto2l=s1_sto2l,
                sto2w=s1_sto2w,sto2x=s1_sto2x,sto2y=s1_sto2y,bed2l=s1_bed2l,bed2w=s1_bed2w,bed2x=s1_bed2x,bed2y=s1_bed2y,bed_xco=bed_xco,bed_yco=bed_yco,kit_xco=kit_xco,kit_yco=kit_yco,
                draw_xco=draw_xco,draw_yco=draw_yco,sta_xco=sta_xco,sta_yco=sta_yco,ots2l=s1_ots2l,ots2w=s1_ots2w,ots2x=s1_ots2x,ots2y=s1_ots2y,
                emptyl=s1_emptyl,emptyw=s1_emptyw,emptyx=s1_emptyx,emptyy=s1_emptyy,toi_xco=toi_xco,toi_yco=toi_yco,wash_xco=wash_xco,wash_yco=wash_yco,din_xco=din_xco,
                din_yco=din_yco, ctoi_xco=ctoi_xco,ctoi_yco=ctoi_yco,sto_xco=sto_xco,sto_yco=sto_yco,ots_xco=ots_xco,
                ots_yco=ots_yco,par_xco=par_xco,par_yco=par_yco,ent_xco=ent_xco,ent_yco=ent_yco,gar_xco=gar_xco,gar_yco=gar_yco,
                foy_xco=foy_xco,foy_yco=foy_yco,uti_xco=uti_xco,uti_yco=uti_yco,sto2_xco=sto2_xco,sto2_yco=sto2_yco,ots2_xco=ots2_xco,
                ots2_yco=ots2_yco,bed2_xco=bed2_xco,bed2_yco=bed2_yco)

                check_print = layout_one.save()
                check_print1 = layout_two.save()
                #user_del = Room.objects.filter(bedl=bedl).delete()
                
                print (check_print)

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
                  "bed2_xco":bed2_xco,"bed2_yco":bed2_yco, "bed2_fill":bed2_fill,"wash_fill":wash_fill, "layout_one":layout_one,


                  "dbedl":dbedl, "dbedw":dbedw,"dbedx":dbedx, "dbedy":dbedy,"dkitl":dkitl, "dkitw":dkitw,"dkitx":dkitx,
                  "dkity":dkity, "dtoil":dtoil, "dtoiw":dtoiw, "dtoiy":dtoiy, "ddrawl":ddrawl, "ddraww":ddraww, "ddrawy":ddrawy,
                  "dstal":dstal, "dstaw":dstaw, "dstax":dstax, "dstay":dstay, "ddinl":ddinl,"ddinw":ddinw, "ddinx":ddinx,
                  "ddiny":ddiny, "dctoil":dctoil,"dctoiw":dctoiw,"dctoix":dctoix, "dctoiy":dctoiy, "dstol":dstol, "dstow":dstow, "dstox":dstox, "dstoy":dstoy,
                  "dotsl":dotsl, "dotsw":dotsw, "dotsx":dotsx, "dotsy":dotsy, "dwashl":dwashl, "dwashw":dwashw, "dwashx":dwashx,"dwashy":dwashy,
                  "dentl":dentl, "dentw":dentw, "dentx":dentx, "denty":denty, "dparl":dparl, "dparw":dparw, "dparx":dparx, "dpary":dpary,
                  "dgarl":dgarl, "dgarw":dgarw, "dgarx":dgarx, "dgary":dgary, "dfoyl":dfoyl, "dfoyw":dfoyw, "dfoyx":dfoyx, "dfoyy":dfoyy, 
                  "dtoix":dtoix, "ddarwx":ddarwx,

                  "dutil":dutil, "dutiw":dutiw, "dutix":dutix, "dutiy":dutiy, "dsto2l":dsto2l, "dsto2w":dsto2w, "dsto2x":dsto2x, "dsto2y":dsto2y,
                  "dbed2l":dbed2l, "dbed2w":dbed2w, "dbed2x":dbed2x, "dbed2y":dbed2y, "demptyl":demptyl, "demptyw":demptyw, "demptyx":demptyx, "demptyy":demptyy,
                  "dots2l":dots2l, "dots2w":dots2w, "dots2x":dots2x, "dots2y":dots2y, 


                  
				          "wbedl":wbedl, "wbedw":wbedw, "wbedx":wbedx, "wbedy":wbedy, "wkitl":wkitl, "wkitw":wkitw, "wkitx":wkitx, "wkity":wkity,
                  "wtoil":wtoil, "wtoiw":wtoiw, "wtoix":wtoix , "wtoiy":wtoiy, "wdrawl":wdrawl, "wdraww":wdraww, "wdrawx":wdarwx, "wdrawy":wdrawy,
                  "wstal":wstal, "wstaw":wstaw, "wstax":wstax, "wstay":wstay, "wdinl":wdinl, "wdinw":wdinw, "wdinx":wdinx, "wdiny":wdiny,
                  "wctoil":wctoil, "wctoiw":wctoiw, "wctoix":wctoix, "wctoiy":wctoiy, "wstol":wstol, "wstow":wstow, "wstox":wstox, "wstoy":wstoy,
                  "wotsl":wotsl, "wotsw":wotsw, "wotsx":wotsx, "wotsy":wotsy, "wwashl":wwashl, "wwashw":wwashw, "wwashx":wwashx, "wwashy":wwashy,
                  "wentl":wentl, "wentw":wentw, "wentx":wentx, "wenty":wenty, "wparl":wparl, "wparw":wparw, "wparx":wparx, "wpary":wpary, "wgarl":wgarl, 
                  "wgarw":wgarw, "wgarx":wgarx, "wgary":wgary, "wfoyl":wfoyl, "wfoyw":wfoyw, "wfoyx":wfoyx, "wfoyy":wfoyy, "wutil":wutil, "wutiw":wutiw, "wutix":wutix, "wutiy":wutiy,

                  "wsto2l":wsto2l, "wsto2w":wsto2w, "wsto2x":wsto2x, "wsto2y":wsto2y, "wbed2l":wbed2l, "wbed2w":wbed2w, "wbed2x":wbed2x, "wbed2y":wbed2y, 
                  "wemptyl":wemptyl, "wemptyw":wemptyw, "wemptyx":wemptyx, "wemptyy":wemptyy, "wots2l":wots2l,"wots2w":wots2w, "wots2x":wots2x, "wots2y":wots2y,

                  
                  "s1_bedl":s1_bedl, "s1_bedw":s1_bedw, "s1_bedx":s1_bedx, "s1_bedy":s1_bedy, "s1_kitl":s1_kitl, "s1_kitw":s1_kitw, "s1_kitx":s1_kitx, 
                  "s1_kity":s1_kity, "s1_toil":s1_toil, "s1_toiw":s1_toiw, "s1_toix":s1_toix, "s1_toiy":s1_toiy, "s1_drawl":s1_drawl, "s1_draww":s1_draww,
                  "s1_drawx":s1_drawx,"s1_drawy":s1_drawy, "s1_stal":s1_stal,"s1_staw":s1_staw, "s1_stax":s1_stax,"s1_stay":s1_stay, "s1_dinl":s1_dinl,
                  "s1_dinw":s1_dinw, "s1_dinx":s1_dinx, "s1_diny":s1_diny, "s1_ctoil":s1_ctoil, "s1_ctoiw":s1_ctoiw,"s1_ctoix":s1_ctoix,
                  "s1_ctoiy":s1_ctoiy,"s1_stol":s1_stol,"s1_stow":s1_stow,"s1_stox":s1_stox,"s1_stoy":s1_stoy,"s1_otsl":s1_otsl,"s1_otsw":s1_otsw, "s1_otsx":s1_otsx,
                  "s1_otsy":s1_otsy,"s1_washl":s1_washl,"s1_washw":s1_washw,"s1_washx":s1_washx,"s1_washy":s1_washy,"s1_entl":s1_entl,
                  "s1_entw":s1_entw,"s1_entx":s1_entx,"s1_enty":s1_enty,"s1_parl":s1_parl,"s1_parw":s1_parw,"s1_parx":s1_parx,"s1_pary":s1_pary,"s1_garl":s1_garl, 
                  "s1_garw":s1_garw, "s1_garx":s1_garx,"s1_gary":s1_gary,"s1_foyl":s1_foyl,"s1_foyw":s1_foyw,"s1_foyx":s1_foyx,"s1_foyy":s1_foyy,"s1_util":s1_util,
                  "s1_utiw":s1_utiw, "s1_utix":s1_utix, "s1_utiy":s1_utiy,"s1_sto2l":s1_sto2l,"s1_sto2w":s1_sto2w,"s1_sto2x":s1_sto2x,"s1_sto2y":s1_sto2y,"s1_bed2l":s1_bed2l,
                  "s1_bed2w":s1_bed2w,"s1_bed2x":s1_bed2x,"s1_bed2y":s1_bed2y,"s1_emptyl":s1_emptyl,"s1_emptyw":s1_emptyw,"s1_emptyx":s1_emptyx,"s1_emptyy":s1_emptyy,
                  "s1_ots2l":s1_ots2l,"s1_ots2w":s1_ots2w,"s1_ots2x":s1_ots2x,"s1_ots2y":s1_ots2y,


                  "s1_bed_xco":s1_bed_xco,"s1_bed_yco":s1_bed_yco,"s1_kit_xco":s1_kit_xco,"s1_kit_yco":s1_kit_yco,"s1_toi_xco":s1_toi_xco,"s1_toi_yco":s1_toi_yco,
                  "s1_draw_xco":s1_draw_xco,"s1_draw_yco":s1_draw_yco,"s1_draw_yco":s1_draw_yco, "s1_sta_yco":s1_sta_yco,"s1_wash_xco":s1_wash_xco,"s1_wash_yco":s1_wash_yco,
                  "s1_din_xco":s1_din_xco,"s1_din_yco":s1_din_yco,
                  "s1_ctoi_xco":s1_ctoi_xco,"s1_ctoi_yco":s1_ctoi_yco,"s1_sto_xco":s1_sto_xco,"s1_sto_yco":s1_sto_yco,"s1_ots_xco":s1_ots_xco,"s1_ots_yco":s1_ots_yco,
                  "s1_ent_xco":s1_ent_xco,"s1_ent_yco":s1_ent_yco,"s1_par_xco":s1_par_xco,"s1_par_yco":s1_par_yco,"s1_gar_xco":s1_gar_xco,"s1_gar_yco":s1_gar_yco,"s1_foy_xco":s1_foy_xco,
                  "s1_foy_yco":s1_foy_yco,"s1_uti_xco":s1_uti_xco,"s1_uti_yco":s1_uti_yco, "s1_sto2_xco":s1_sto2_xco,"s1_sto2_yco":s1_sto2_yco,"s1_ots2_xco":s1_ots2_xco,"s1_ots2_yco":s1_ots2_yco,
                  "s1_bed2_xco":s1_bed2_xco,"s1_bed2_yco":s1_bed2_yco, "s1_din_fill":s1_din_fill,"s1_ctoi_fill":s1_ctoi_fill, "s1_sto_fill":s1_sto_fill, "s1_ots_fill":s1_ots_fill, "s1_ent_fill":s1_ent_fill,
                  "s1_par_fill":s1_par_fill,"s1_gar_fill":s1_gar_fill,"s1_foy_fill":s1_foy_fill, "s1_uti_fill":s1_uti_fill, "s1_sto2_fill":s1_sto2_fill, "s1_ots2_fill":s1_ots2_fill, "s1_bed2_fill":s1_bed2_fill,
                  "s1_wash_fill":s1_wash_fill,

                  
                  
                  "data1": userdata3, "store":store, "ots": ots, "parking":parking,"washarea":washarea, "dressingroom":dressingroom, "utility":utility, "temple":temple, "garden":garden,
                  "match1": match1,
                }  

                #print (context)
                
                
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
