import speedtest
import csv
from datetime import datetime

# Get current Time and Date
now = datetime.now() 
Date = now.strftime("%m/%d/%Y")
Hour = date_time = now.strftime("%H:%M:%S")

# Perform Speed Test
servers = []
s = speedtest.Speedtest()
s.get_servers(servers)
s.get_best_server()
s.download()
s.upload()
results_dict = s.results.dict()


# Process only required aata
DownloadSpeed = round(float(results_dict['download'])/(1024*1024),2)
# DownloadSpeed = str(DownloadSpeed)+" Mb/s"
UploadSpeed = round(float(results_dict['upload'])/(1024*1024),2)
# UploadSpeed = str(UploadSpeed)+" Mb/s"
Ping = results_dict['ping']
# Ping = str(Ping)+" ms"
Ping = results_dict['ping']
ISP = results_dict['client']['isp']
IP = results_dict['client']['ip']
Country = results_dict['client']['country']
City = results_dict['server']['name']

Line = [Date, Hour, DownloadSpeed, UploadSpeed, Ping, IP, ISP, City, Country]

with open('LogSpeedTest.csv','a') as file:
    wr = csv.writer(file, quoting=csv.QUOTE_ALL)
    wr.writerow([Date, Hour, DownloadSpeed, UploadSpeed, Ping, IP, ISP, City, Country])


# To run every hour
# 0 0 * * * python /home/pi/Speedtest.py
# 0 1 * * * python /home/pi/Speedtest.py
# 0 2 * * * python /home/pi/Speedtest.py
# 0 3 * * * python /home/pi/Speedtest.py
# 0 4 * * * python /home/pi/Speedtest.py
# 0 5 * * * python /home/pi/Speedtest.py
# 0 6 * * * python /home/pi/Speedtest.py
# 0 7 * * * python /home/pi/Speedtest.py
# 0 8 * * * python /home/pi/Speedtest.py
# 0 9 * * * python /home/pi/Speedtest.py
# 0 10 * * * python /home/pi/Speedtest.py
# 0 12 * * * python /home/pi/Speedtest.py
# 0 13 * * * python /home/pi/Speedtest.py
# 0 14 * * * python /home/pi/Speedtest.py
# 0 15 * * * python /home/pi/Speedtest.py
# 0 16 * * * python /home/pi/Speedtest.py
# 0 17 * * * python /home/pi/Speedtest.py
# 0 18 * * * python /home/pi/Speedtest.py
# 0 19 * * * python /home/pi/Speedtest.py
# 0 20 * * * python /home/pi/Speedtest.py
# 0 21 * * * python /home/pi/Speedtest.py
# 0 22 * * * python /home/pi/Speedtest.py
# 0 23 * * * python /home/pi/Speedtest.py

# To run every half hour
# 30 0 * * * python /home/pi/Speedtest.py
# 30 1 * * * python /home/pi/Speedtest.py
# 30 2 * * * python /home/pi/Speedtest.py
# 30 3 * * * python /home/pi/Speedtest.py
# 30 4 * * * python /home/pi/Speedtest.py
# 30 5 * * * python /home/pi/Speedtest.py
# 30 6 * * * python /home/pi/Speedtest.py
# 30 7 * * * python /home/pi/Speedtest.py
# 30 8 * * * python /home/pi/Speedtest.py
# 30 9 * * * python /home/pi/Speedtest.py
# 30 10 * * * python /home/pi/Speedtest.py
# 30 12 * * * python /home/pi/Speedtest.py
# 30 13 * * * python /home/pi/Speedtest.py
# 30 14 * * * python /home/pi/Speedtest.py
# 30 15 * * * python /home/pi/Speedtest.py
# 30 16 * * * python /home/pi/Speedtest.py
# 30 17 * * * python /home/pi/Speedtest.py
# 30 18 * * * python /home/pi/Speedtest.py
# 30 19 * * * python /home/pi/Speedtest.py
# 30 20 * * * python /home/pi/Speedtest.py
# 30 21 * * * python /home/pi/Speedtest.py
# 30 22 * * * python /home/pi/Speedtest.py
# 30 23 * * * python /home/pi/Speedtest.py
