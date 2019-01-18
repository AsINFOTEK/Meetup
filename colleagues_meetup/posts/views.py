from django.http import HttpResponse
from .models import user, date, datelog
import datetime
from datetime import timedelta
import json

def index(request):
    now = datetime.datetime.now()
    nextday = datetime.datetime.now() + timedelta(days=3)

    # now.strftime('%A')
    whichday = nextday.strftime('%a')
    # Sun
    # Sat

    if (whichday == 'Sat'):
        nextday = datetime.datetime.now() + timedelta(days=5)
        whichday = nextday.strftime('%a')
    elif (whichday == 'Sun'):
        nextday = datetime.datetime.now() + timedelta(days=4)
        whichday = nextday.strftime('%a')
    else:
        print("Okay Day")

    if (whichday == 'Mon'):
        event1day = '1'
        event2day = '6'
        event3day = '11'
    elif (whichday == 'Tue'):
        event1day = '2'
        event2day = '7'
        event3day = '12'
    elif (whichday == 'Wed'):
        event1day = '3'
        event2day = '8'
        event3day = '13'
    elif (whichday == 'Thu'):
        event1day = '4'
        event2day = '9'
        event3day = '14'
    elif (whichday == 'Fri'):
        event1day = '5'
        event2day = '10'
        event3day = '15'
    else:
        print("Error In day which day ")
        print(whichday)
    print(event1day+','+event2day+','+event3day)
    # DAYS
    # 1   2  3  4  5
    # 6   7  8  9  10
    # 11 12 13 14 15

    '''
    print("first time")
    print(now)
    print("After 5 days")
    print(datetime.datetime.now() + timedelta(days=3))
    '''

    users=user.objects.all()
    dates=date.objects.all()
    datelog1=datelog.objects.all()

    #Retrive User Date


    #Rerive Date Date
    dates=dates.values()
    dates = [entry for entry in dates]

    #Rerive Date Date
    datelog1=datelog1.values()
    datelog2 = [entry for entry in datelog1]


    #Rerive users Data
    users=users.values()
    users = [entry for entry in users]
    usersextra=users

    # print("run once")
    # for user1 in users:
    #     print(user1)
    # print("run second time")
    # for user1 in users:
    #     print(user1)
    # print("Run third time")
    # for user1 in users:
    #     print(user1)



    dateis="%d-" % now.year
    dateis+="%d-" % now.month
    dateis+="%d" % now.day


    Pdateis="%d-" % nextday.year
    monthis=str(nextday.month)
    if(len(monthis)<2):
        Pdateis += '0' + monthis + '-'
    else:
        Pdateis += "%d-" % now.month

    dayis=str(nextday.day)
    if(len(dayis)<2):
        Pdateis += '0' + dayis
    else:
        Pdateis += "%d" % now.day

    #Pdateis+="%d-" % nextday.month
    #Pdateis+="%d" % nextday.day
    #
    # print("Prediction date")
    # print((Pdateis))
    #
    # print('predictionfordate')
    # print(nextday.day)



    event1=list()
    event2=list()
    event3=list()
    for date1 in dates:
        isokay=0
        thiseventweekday = date1['weekday']
        thiseventweekday = thiseventweekday.split(',')

        for thisday in thiseventweekday:
            if(thisday==event1day):
                isokay=1
            elif(thisday==event2day):
                isokay=1
            elif(thisday==event3day):
                isokay=1


            if(isokay==1):
                calendarblocked=date1['calendarblocked']
                calendarblocked=calendarblocked.split(',')
                for calendarblockdate in calendarblocked:
                    if(calendarblockdate==Pdateis):
                        isokay=0
                        # print("this user event request removed due to block date selection ")
                        # print(date1)


        if(isokay==1):
            if(date1['event'] == '1'):
                event1.append((date1))
            elif(date1['event'] == '2'):
                event2.append((date1))
            elif(date1['event'] == '3'):
                event3.append((date1))
            else:
                print(date1['event'])
                print("Some Thing Wrong in Database")

    finalevent1=list()
    # print("print in event1")
    for event in event1:
        # print(event)
        for user1 in users:
            if(user1['id']==event['userid']):
                usertemp=user1
                eventtem=event
                newtemp= {**usertemp, **eventtem}
                finalevent1.append(newtemp)
            # else:
            #     print("this user not match")
            #     print(user1)
        # print(event)
    # print("Event List 2")
    finalevent2=list()
    # print("print users before event2")
    # for user1 in usersextra:
        # print(user1)
    for event in event2:
        # print("creating final array")
        for user1 in users:
            # print(user1)
            if(user1['id']==event['userid']):

                # print(user1)
                # print(event)
                # print("above match")
                newtemp = {**user1, **event}
                finalevent2.append(newtemp)
                #print("final temp")
                # print(temp)
                # print("final temp")
                # finalevent2.append(temp)
            # else:
            #     print("this usr not match with any event")
            #     print(user1)
        # print(event)
    # print("Event List 3")
    finalevent3=list()
    for event in event3:
        # print("is Event User ID"+str(event['userid']))
        for user1 in users:
            # print("is user ID" + str(user1['id']))
            if(user1['id']==event['userid']):
                newtemp = {**user1, **event}
                finalevent3.append(newtemp)

    '''
        # print(event)
    print("final Event 1")
    for final1 in finalevent1:
        print(final1)

    print("final Event 2")
    for final2 in finalevent2:
        print(final2)

    print("final Event 3")
    for final3 in finalevent3:
        print(final3)
    '''
    finalhaevent1=list()
    for final1 in finalevent1:
        tempfinal1 = final1
        tempfinal1["match"] = ""
        totelmatch=0
        for final2 in finalevent1:
            if(final1['division']==final2['division'] and  final1['location']==final2['location'] and final1['department']!=final2['department']):
                totelmatch=totelmatch+1
                if(tempfinal1["match"]!=""):
                    tempfinal1["match"]=tempfinal1["match"]+','
                tempfinal1['match']=tempfinal1["match"] + str(final2["userid"])
        tempfinal1["totelmatch"]=totelmatch
        finalhaevent1.append(tempfinal1)

    finalhaevent2=list()
    for final1 in finalevent2:
        tempfinal1 = final1
        tempfinal1["match"] = ""
        totelmatch=0
        for final2 in finalevent2:
            if(final1['division']==final2['division'] and  final1['location']==final2['location'] and final1['department']!=final2['department']):
                totelmatch=totelmatch+1
                if(tempfinal1["match"]!=""):
                    tempfinal1["match"]=tempfinal1["match"]+','
                tempfinal1['match']=tempfinal1["match"] + str(final2["userid"])
        tempfinal1["totelmatch"]=totelmatch
        finalhaevent2.append(tempfinal1)

    finalhaevent3=list()
    for final1 in finalevent3:
        tempfinal1 = final1
        tempfinal1["match"] = ""
        totelmatch=0
        for final2 in finalevent3:
            if(final1['division']==final2['division'] and  final1['location']==final2['location'] and final1['department']!=final2['department']):
                totelmatch=totelmatch+1
                if(tempfinal1["match"]!=""):
                    tempfinal1["match"]=tempfinal1["match"]+','
                tempfinal1['match']=tempfinal1["match"] + str(final2["userid"])
        tempfinal1["totelmatch"]=totelmatch
        finalhaevent3.append(tempfinal1)



    # print("final Event 1")

    # for final in finalhaevent1:
    #     print(final)


    finalhalen = len(finalhaevent1)
    finalhaevent01=list()
    while(finalhalen>0):
        eventindex=0
        temp=-1
        recordindex=-1
        for final1 in finalhaevent1:
            if(temp<final1['totelmatch']):
                temp=final1['totelmatch']
                recordindex=eventindex
            eventindex = eventindex + 1
        tempevent=finalhaevent1.pop(recordindex)
        finalhaevent01.append(tempevent)
        finalhalen = len(finalhaevent1)
    # finalhaevent01.reverse()

    finalhalen = len(finalhaevent2)
    finalhaevent02 = list()
    while (finalhalen > 0):
        eventindex = 0
        temp = -1
        recordindex = -1
        for final1 in finalhaevent2:
            if (temp < final1['totelmatch']):
                temp = final1['totelmatch']
                recordindex = eventindex
            eventindex = eventindex + 1
        tempevent = finalhaevent2.pop(recordindex)
        finalhaevent02.append(tempevent)
        finalhalen = len(finalhaevent2)
    # finalhaevent01.reverse()

    finalhalen = len(finalhaevent3)
    finalhaevent03 = list()
    while (finalhalen > 0):
        eventindex = 0
        temp = -1
        recordindex = -1
        for final1 in finalhaevent3:
            if (temp < final1['totelmatch']):
                temp = final1['totelmatch']
                recordindex = eventindex
            eventindex = eventindex + 1
        tempevent = finalhaevent3.pop(recordindex)
        finalhaevent03.append(tempevent)
        finalhalen = len(finalhaevent3)
    # finalhaevent01.reverse()


    # print("01   01    01    01   01")
    # for test in finalhaevent01:
    #     print(test)


    # print("User list final for final")
    finalhaeventfinal=finalhaevent01+finalhaevent02+finalhaevent03

    userinvited=list()
    usersignored=list()

    finalhalen=len(finalhaevent01)
    # print(finalhalen)
    # print("Enter final event 1")
    # print(finalhaevent01)
    while(0<finalhalen):
        # print("is True")
        # print(usersignored)
        ignore=0
        tempuser=finalhaevent01.pop()
        finalhalen = len(finalhaevent01)
        # print(tempuser)
        for userignored in usersignored:

            listformatch = tempuser['match']
            listidis = listformatch.split(',')
            listdis = listidis[0]
            listidis = str(listdis)

            if (str(tempuser['userid'])==str(userignored) or str(listidis)==str(userignored)):
                ignore=1
            else:
                print("Not Match")
                print(tempuser['userid'])
                print(type(tempuser['userid']))

                print(userignored)
                print(type(userignored))
        if(tempuser['totelmatch']==0):
            tempiduser=tempuser['userid']
            usersignored.append(tempiduser)
            ignore=1
        if(ignore!=1):
            listformatch=tempuser['match']
            listidis=listformatch.split(',')
            listdis=listidis[0]
            listidis=str(listdis)
            tempiduser = tempuser['userid']
            usersignored.append(tempiduser)
            usersignored.append(listidis)
            temp_dict = dict()
            # print("user temp user")
            # print(finalhaeventfinal[finalhalen])
            temp_dict['firstuserid'] = tempuser['userid']
            for isdata in finalhaeventfinal:
                if(str(isdata['userid'])==str(tempuser['userid'])):
                    temp_dict['firstusername']=isdata['mail']
                # print(type(isdata['userid']))
                # print(type(listidis))
                if (str(isdata['userid']) == str(listidis)):
                    temp_dict['seonduserid'] = listidis
                    temp_dict['seondusername'] = isdata['mail']


            temp_dict['eventid']='1'
            userinvited.append(temp_dict)
        finalhalen=len(finalhaevent01)
        # print("meeting Setup for these user")
        # print(userinvited)


    #event 2
    finalhalen = len(finalhaevent02)
    while (0 < finalhalen):
        # print("is True")
        ignore = 0
        tempuser = finalhaevent02.pop()
        # print(tempuser)
        for userignored in usersignored:
            # if (str(tempuser['userid']) == str(userignored)):
            if (str(tempuser['userid']) == str(userignored) or str(listidis) == str(userignored)):
                ignore = 1
        if (tempuser['totelmatch'] == 0):
            tempiduser = tempuser['userid']
            usersignored.append(tempiduser)
            ignore = 1
        if (ignore != 1):
            listformatch = tempuser['match']
            listidis = listformatch.split(',')
            listdis = listidis[0]
            listidis = str(listdis)
            tempiduser = tempuser['userid']
            usersignored.append(tempiduser)
            usersignored.append(listidis)
            temp_dict = dict()
            temp_dict['firstuserid'] = tempuser['userid']
            for isdata in finalhaeventfinal:
                if (str(isdata['userid']) == str(tempuser['userid'])):
                    temp_dict['firstusername'] = isdata['mail']
                # print(type(isdata['userid']))
                # print(type(listidis))
                if (str(isdata['userid']) == str(listidis)):
                    temp_dict['seonduserid'] = listidis
                    temp_dict['seondusername'] = isdata['mail']

            temp_dict['eventid'] = '2'
            userinvited.append(temp_dict)
        finalhalen = len(finalhaevent02)
    # print("meeting Setup for these user")
    # print(userinvited)

    #event 3
    finalhalen = len(finalhaevent03)
    while (0 < finalhalen):

        # print("is True")
        ignore = 0
        tempuser = finalhaevent03.pop()
        # print(tempuser)
        for userignored in usersignored:
            if (str(tempuser['userid']) == str(userignored) or str(listidis) == str(userignored)):
                ignore = 1
        if (tempuser['totelmatch'] == 0):
            tempiduser = tempuser['userid']
            usersignored.append(tempiduser)
            ignore = 1
        if (ignore != 1):
            listformatch = tempuser['match']
            listidis = listformatch.split(',')

            listdis = listidis[0]
            listidis = str(listdis)

            tempiduser = tempuser['userid']
            usersignored.append(tempiduser)
            usersignored.append(listidis)
            temp_dict = dict()

            temp_dict['firstuserid'] = tempuser['userid']
            for isdata in finalhaeventfinal:
                if (str(isdata['userid']) == str(tempuser['userid'])):
                    temp_dict['firstusername'] = isdata['mail']
                # print(type(isdata['userid']))
                # print(type(listidis))
                if (str(isdata['userid']) == str(listidis)):
                    temp_dict['seonduserid'] = listidis
                    temp_dict['seondusername'] = isdata['mail']

            temp_dict['eventid'] = '3'

            userinvited.append(temp_dict)
        finalhalen = len(finalhaevent03)

            # if(userignored==tempuser)
        # tempevent.split(',')

        print("meeting Setup for these user")
        print(userinvited)

        response_data=list()




    response_data=userinvited


    '''
    print("final Event 01")
    for final in finalhaevent01:
        print(final)


    print("final Event 02")
    for final in finalhaevent02:
        print(final)

    print("final Event 03")
    for final in finalhaevent03:
        print(final)
    '''

    # print(len(finalevent3))



    # print("Final Three")
    # for final3 in finalevent3:
    #     print(final3)



    '''
    print(type(users))

    for user1 in users:
        print(user1)
    del users[0]
    #del users[3]
    print("after remove no 3")
    for user1 in users:
        print(user1)
    #print(users)
    '''
    # print("list is")
    # for listis in usersignored:
    #     print(listis)
    output = "Hello! everywhere from posts!!!"
    return HttpResponse(json.dumps(response_data), content_type="application/json")

from django.shortcuts import render

# Create your views here.