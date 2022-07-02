# https://github.com/amphipath/starforce/blob/master/weights_en.csv
# https://pynative.com/python-weighted-random-choices-with-probability/
# https://towardsdatascience.com/a-complete-guide-to-using-progress-bars-in-python-aa7f4130cda8
import random
from time import sleep
from tqdm import tqdm
from sfList import sf
from math import *
import os
resultlist = ["Success", "Fail(Maintain)", "Fail(Decrease)", "Destroy"]
inplay = True

def calcost(star,eqlevel):
    if 0 <= star <= 9:
        return 100*round(pow(eqlevel,3)*(star+1)/2500+10)
    if 10 <= star <= 14:
        return 100 * round(pow(eqlevel, 3) * pow(star+1,2.7) / 40000 + 10)
    if 15 <= star <= 24:
        return 100*round(pow(eqlevel,3)*pow(star+1,2.7)/20000+10)

def printProbability(Success, FailMaintain,FailDecrease, Destroy):
    print("Probability:")
    if Success > 0:
        print("Success: " + "{:.1f}".format(Success * 100) + "%")
    if FailMaintain > 0:
        print("Fail(Maintain):" + "{:.1f}".format(FailMaintain * 100) + "%")
    if FailDecrease > 0:
        print("Fail(Decrease):" + "{:.1f}".format(FailDecrease * 100) + "%")
    if Destroy > 0:
        print("Destroy:" + "{:.1f}".format(Destroy * 100) + "%")


def printstatus(star,item, totalcost, numdestroy, mindestroy, maxdestroy, mincost, maxcost, minclick, maxclick):
    print("*" * star)
    print("Total Cost: " + "{:,}".format(totalcost))
    print("Number of Destroys: " + str(numdestroy))
    if item>0:
        print("Range Cost: " + "{:,}".format(mincost) + " - " + "{:,}".format(maxcost))
        print("Range of Destroys: " + "{:,}".format(mindestroy) + " - " + "{:,}".format(maxdestroy))
        print("Range of Clicks: " + "{:,}".format(minclick) + " - " + "{:,}".format(maxclick))

def printanalytics(overallstats,limitfail):
    for x in range(limitfail):
        print("Number of Trials")
        print("Num Fail: "+str(x))
        stats = overallstats[x][0]
        mindestroy = overallstats[x][1]
        maxdestroy = overallstats[x][2]
        mincost = overallstats[x][3]
        maxcost = overallstats[x][4]
        minclick = overallstats[x][5]
        maxclick = overallstats[x][6]
        overallcost = overallstats[x][7]
        totaldestroy = overallstats[x][8]
        num = overallstats[x][9]
        avgcost = overallcost / num
        avgdestroy = totaldestroy / num
        for i in range(26):
            print(i,":","*"*i,stats[i])
        print("Range Cost: " + "{:,}".format(mincost) + " - " + "{:,}".format(maxcost))
        print("Range of Destroys: " + "{:,}".format(mindestroy) + " - " + "{:,}".format(maxdestroy))
        print("Range of Clicks: " + "{:,}".format(minclick) + " - " + "{:,}".format(maxclick))
        print("Average Cost: " + "{:,.0f}".format(avgcost))
        print("Average Destroy: " + "{:.2f}".format(avgdestroy))
def failstack(numfail):
    scrolllist = ["Pass", "Fail"]
    count = 0
    while True:
        scrollresult = random.choices(scrolllist, weights=(30,70), k=1)
        if scrollresult[0] == "Fail":  # need conse
            count+=1
        else:
            count = 0
        if count == numfail:
            break

def printprogress(numfail,limitfail,item,numtrial):
    percent = 100 * (numfail/float(limitfail))
    print("Fail Stack: |" + "█" * int(percent/2) + " " * int((100 - percent)/2) + "|", end="")  # '█' - hold alt and press 219 on numpad: /2 is used to reduce size
    print(str(numfail) + "/" + str(limitfail))
    percent = 100 * (item / float(numtrial))
    print("Item Completed: |" + "█" * int(percent/2) + " " * int((100 - percent)/2) + "|", end="")  # '█' - hold alt and press 219 on numpad:  /2 is used to reduce size
    print(str(item) + "/" + str(numtrial))

def printoverallrates(totalsuccess, totalfailm, totalfaild, totaldestroy):
    total = totalsuccess + totalfailm + totalfaild + totaldestroy
    percent1 = 100 * (totalsuccess / float(total))
    percent2 = 100 * (totalfailm / float(total))
    percent3 = 100 * (totalfaild / float(total))
    percent4 = 100 * (totaldestroy / float(total))
    print("Success percentage: " + "{:.2f}".format(percent1) + "%")
    print("Fail(Maintain) percentage: " + "{:.2f}".format(percent2) + "%")
    print("Fail(Decrease) percentage: " + "{:.2f}".format(percent3) + "%")
    print("Destroy percentage: " + "{:.2f}".format(percent4) + "%")

def printavg(totaldestroy, overallcost, num):
    avgcost = overallcost/num
    avgdestroy = totaldestroy/num
    print("Average Cost: " + "{:,.0f}".format(avgcost))
    print("Average Destroy: " + "{:.2f}".format(avgdestroy))


while inplay:
    eqlevel = -1
    startlevel = -1
    endlevel = -1
    basecost = -1
    numtrial = -1
    safeguardstatus = "a"
    starcatchstatus = "a"
    tpercentstatus = "a"
    fivetenstatus = "a"
    seestatus = "a"
    mvpstatus = "a"
    fsstatus = "a"
    safeguard = False
    starcatch = False
    tpercent = False
    fiveten = False
    seeprocess = False
    fs = False
    mvp = 0
    star = 0
    limitfail = 0
    totalsuccess = 0
    totalfailm = 0
    totalfaild = 0


    overallstats=[]
    print("Welcome to Star Force Simulator")
    while eqlevel<0 or eqlevel>200:
        try:
            eqlevel = int(input("Equipment Level: "))
        except Exception as e:
            print("Error")
    while basecost<0:
        try:
            basecost = int(input("Equipment Cost: "))
        except Exception as e:
            print("Error")
    while startlevel<0 or startlevel>24:
        try:
            startlevel = int(input("Current Star Level: "))
        except Exception as e:
            print("Error")
    while endlevel<startlevel or endlevel>25:
        try:
            endlevel = int(input("Desired Star Level: "))
        except Exception as e:
            print("Error")
    while safeguardstatus!="y" and safeguardstatus!="n":
        try:
            safeguardstatus = input("SafeGuard (y/n): ").lower()
            if safeguardstatus == "y":
                safeguard = True
            else:
                safeguard = False
        except Exception as e:
            print("Error")
    while starcatchstatus!="y" and starcatchstatus!="n":
        try:
            starcatchstatus = input("StarCatcher (y/n): ").lower()
            if starcatchstatus == "y":
                starcatch = True
            else:
                starcatch = False
        except Exception as e:
            print("Error")
    while tpercentstatus!="y" and tpercentstatus!="n":
        try:
            tpercentstatus = input("30% off(y/n): ").lower()
            if tpercentstatus == "y":
                tpercent = True
            else:
                tpercent = False
        except Exception as e:
            print("Error")
    while fivetenstatus!="y" and fivetenstatus!="n":
        try:
            fivetenstatus = input("5/10/15 (y/n): ").lower()
            if fivetenstatus == "y":
                fiveten = True
            else:
                fiveten = False
        except Exception as e:
            print("Error")
    while mvpstatus!="s" and mvpstatus!="g" and mvpstatus!="d" and mvpstatus!="r" and mvpstatus!= "n":
        try:
            mvpstatus = input("MVP Silver/Gold/Diamond/Red/None (s/g/d/r/n): ").lower()
            if mvpstatus == "s":
                mvp = 0.03  # 3%
            elif mvpstatus == "g":
                mvp = 0.05  # 5%
            elif mvpstatus == "n":
                mvp = 0
            else:
                mvp = 0.1  # 10%
        except Exception as e:
            print("Error")
    while numtrial < 0:
        try:
            numtrial = int(input("Number of Trials: "))
        except Exception as e:
            print("Error")
    while fsstatus != "y" and fsstatus != "n":
        try:
            fsstatus = input("Fail Stack Process?: (y/n): ").lower()
            if fsstatus == "y":
                fs = True
                limitfail = 5  # 0,1,2,3
            else:
                fs = False
                limitfail = 1
        except Exception as e:
            print("Error")
    while seestatus != "y" and seestatus != "n":
        try:
            seestatus = input("See Staring Process?: (y/n): ").lower()
            if seestatus == "y":
                seeprocess = True
            else:
                seeprocess = False
        except Exception as e:
            print("Error")

    for numfail in tqdm(range(limitfail),desc= "Intervals", ncols=80):
        totalcost = 0
        numdestroy = 0
        mindestroy = 999999999999999
        maxdestroy = 0
        mincost = 999999999999999
        maxcost = 0
        minclick = 999999999999999
        maxclick = 0
        totaldestroy = 0
        overallcost = 0
        stats = [0 for i in range(26)]
        for item in tqdm(range(numtrial),desc= "Item", ncols=80, leave=False):
            star = startlevel
            numdestroy = 0
            totalcost = 0
            fail = 0
            click = 0
            removestatus = False
            while star!=endlevel:
                if seeprocess:
                    sleep(0.01)  # !!!! important so that progress bar is updated and shown before clear screen
                    os.system('cls')
                    print(str(star) + ">" + str(star + 1))
                if star>17 and fs and numfail>0:  # fail statck occurs when star >17, fail stack enable and num of time shld a scroll fail >0
                    failstack(numfail)  # wait till failstack meet
                Success = sf[star]["Success"]
                FailMaintain = sf[star]["Fail(Maintain)"]
                FailDecrease = sf[star]["Fail(Decrease)"]
                Destroy = sf[star]["Destroy"]
                # calculation for Star Catcher, Chance Time, 5/10/15
                if fail == 2 or (fiveten and (star == 5 or star == 10 or star == 15 )):  # Chance Time(2 consecutive fail) or 5/10/15
                    Success = 1.0
                    FailMaintain = 0
                    FailDecrease = 0
                    Destroy = 0
                    result = random.choices(resultlist, weights=(Success,0,0,0), k=1)
                    fail = 0
                    if safeguard:
                        safeguard = False  # for chance time you don't need to pay double mesos for safeguard
                        removestatus = True
                elif starcatch:
                    Success = sf[star]["Success"] * 1.05  # success rate increases by 5% multiplied,
                    # Maintain/Decrease and Destroy rates will be redistributed at the same bracketed rates
                    if FailMaintain>0:
                        FailMaintain -= sf[star]["Success"] * 0.05
                    if FailDecrease>0:
                        FailDecrease -= sf[star]["Success"] * 0.05
                    # weight is based on the value of the variables,  probability = var/sum of vars, k = outcome(s)
                    result = random.choices(resultlist, weights=(Success, FailMaintain, FailDecrease, Destroy), k=1)
                else:
                    result = random.choices(resultlist, weights=(Success, FailMaintain, FailDecrease, Destroy), k=1)

                # calculate cost for safeguard
                cost = calcost(star,eqlevel)
                if safeguard and (12<=star<=16):
                    cost += cost*2
                    if result == "Destroy":
                        result = "Fail(Decrease)"
                # discounts 30%, mvp
                discount = 0
                if tpercent:  # 30% off
                    discount = 0.3
                if mvp>0 and 0<= star <=16:
                    discount += mvp
                cost = round(cost * (1-discount))
                totalcost += cost
                if removestatus:   # once Chance Time or 5/10/15 is activated set safeguard back
                    safeguard = True
                    removestatus = False
                # print("Result: " + result[0])
                match result[0]:
                    case "Success":
                        star += 1
                        fail = 0
                        totalsuccess += 1
                    case "Fail(Maintain)":
                        totalfailm += 1
                        pass
                    case "Fail(Decrease)":
                        fail += 1
                        star -= 1
                        totalfaild += 1
                    case "Destroy":
                        totalcost += basecost  # since item destroyed, add base cost to the totalcost for trace back
                        numdestroy += 1
                        star = 12
                        fail = 0
                        totaldestroy += 1

                stats[star]+=1
                click += 1
                if seeprocess:
                    printProbability(Success, FailMaintain, FailDecrease, Destroy)
                    printstatus(star, item, totalcost, numdestroy, mindestroy, maxdestroy, mincost, maxcost, minclick, maxclick)
                    # printoverallrates(totalsuccess, totalfailm, totalfaild, totaldestroy)
                    if item>0:
                        printavg(totaldestroy, overallcost, item)
                    printprogress(numfail, limitfail, item, numtrial)
                    sleep(0.1)
            overallcost += totalcost
            if click > maxclick:
                maxclick = click
            if click < minclick:
                minclick = click
            if numdestroy > maxdestroy:
                maxdestroy = numdestroy
            if numdestroy < mindestroy:
                mindestroy = numdestroy
            if totalcost > maxcost:
                maxcost = totalcost
            if totalcost < mincost:
                mincost = totalcost
            if seeprocess:
                os.system('cls')
                print(star)
                printstatus(star, item, totalcost, numdestroy,mindestroy, maxdestroy, mincost, maxcost, minclick, maxclick)
                # printoverallrates(totalsuccess, totalfailm, totalfaild, totaldestroy)
                printavg(totaldestroy, overallcost, item+1)
                printprogress(numfail, limitfail, item+1, numtrial)
                print("Starting again in 3s")
                sleep(1)

        overallstats.append([stats, mindestroy, maxdestroy, mincost, maxcost, minclick, maxclick, overallcost, totaldestroy, numtrial])
    os.system('cls')
    print("Summary:")
    # printoverallrates(totalsuccess, totalfailm, totalfaild, totaldestroy)
    printanalytics(overallstats, limitfail)
    again = input("Try Again? y/n:").lower()
    if again == "y":
        os.system('cls')
    else:
        print(again)
        inplay = False