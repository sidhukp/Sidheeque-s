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
    
    Hosts=["172.21.134.145","172.21.10.10","172.21.10.11","172.21.10.12","172.21.10.13","172.21.10.14","172.21.10.15","172.21.10.188","172.21.10.122","172.21.10.116","172.21.10.177","172.21.10.19","172.21.10.18","10.10.0.11","10.10.0.27","10.10.0.33","10.10.0.31","10.10.0.30","172.21.10.5","172.21.10.4","10.10.0.1","10.10.0.61","10.10.0.62"]

    for x in Hosts:

        IP_ADD=x

        

        try:

            if IP_ADD==("10.0.0.61" or "10.0.0.62"):
                
                net_connect = ConnectHandler(device_type='cisco_nxos', host=IP_ADD, username="RGH36747", password="Minnu@123")

            elif IP_ADD==("10.10.25.2" or "172.21.10.7"):

                net_connect = ConnectHandler(device_type="fortinet", host=IP_ADD, username="_svc_netdbackup", password="*p!Q^DzYw%-3e5")

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
            
        
    


    















"""file1 = open("C:/Users/sidheequl.akbar/Desktop/Relvents/Python Programs/Program to Create Username and pwd in Multuple Switches/csvsample.csv")
    csv_Exctract=csv.reader(file1)
    
    for x in csv_Exctract:
        IP_ADD=x[1]
        print("\nDevice Name %s\n"%x[2])
        count = count+1

        try:
        
            net_connect = ConnectHandler(device_type='cisco_ios', host=IP_ADD, username=Username, password=Password)
            print("Connected to %s Succesfully"%IP_ADD)
            time.sleep(1)
            print(net_connect.find_prompt())

            
            config_account=["username %s privilege 15 secret 0 %s"%(New_Username,New_Password)]

            output2=net_connect.send_config_set(config_account)

            print(output2)
            output1 = net_connect.send_command("wr")

            print(output1)

            print("Account Created...\nNext Device %d\n"%count)
            time.sleep(1)

        except Exception as E:
            print(E)

    print("Added to %d Devices"%count)"""

main()
        
         
