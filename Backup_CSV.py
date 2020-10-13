import csv
import os
from netmiko import ConnectHandler
import time
from datetime import date

def main():


    print("==============================================================")
    print("                 PROGRAM for IOS BACKUP\n==============================================================\n")
    print("               Created By SIDHEEQUL AKBAR \n==============================================================\n")

    os.chdir("//172.21.134.139/Switch Backup")  #Working Directory

    today=date.today()
    Date01=today.strftime("%d-%b-%Y")

    if os.path.exists(Date01)==True:

        print("Folder Already Exist")
    else:
        os.mkdir(Date01)

        
    file1=open("C:/Users/sidheequl.akbar/Desktop/Relvents/Python Programs/Auto Backups/CSV's/Network.csv")
    csv_Extract=csv.reader(file1)

    for x in csv_Extract:

        IP_ADD=x[1]

        if x[1]=="IP Address":

            continue
        else:

            try:

                if IP_ADD==("10.0.0.61" or "10.0.0.62"):

                    net_connect = ConnectHandler(device_type='cisco_nxos', host=IP_ADD, username="RGH36747", password="Minnu@123")

                elif IP_ADD==("10.10.25.2" or "172.21.10.7"):

                    net_connect = ConnectHandler(device_type="fortinet", host=IP_ADD, username="_svc_netdbackup", password="*p!Q^DzYw%-3e5")
                    print("Connected to %s Succesfully"%IP_ADD)
                    time.sleep(1)
                    print(net_connect.find_prompt())
                    
                    #file1=open("//172.21.134.139/Switch Backup/%s/%s#-%s.txt"%(Date01,net_connect.find_prompt(),IP_ADD),"w+")
                    
                    output1 = net_connect.send_command("get system status")

                    print(output1)
                    
                    #file1.write(output1)

                    print("Backup is Successfull and copied")

                    continue

                else:
                    net_connect = ConnectHandler(device_type='cisco_ios', host=IP_ADD, username="RGH36747", password="Minnu@123")


                print("Connected to %s Succesfully"%IP_ADD)

                time.sleep(1)
                print(net_connect.find_prompt())


                file1=open("//172.21.134.139/Switch Backup/%s/%s#-%s.txt"%(Date01,net_connect.find_prompt(),IP_ADD),"w+")

                output1 = net_connect.send_command("show run")

                file1.write(output1)

                print("Backup is Successfull and copied")

            except Exception as E:
                print(E)
                
main()



    
