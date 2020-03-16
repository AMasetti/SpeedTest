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

# with open('FTP/files/LogSpeedTest.csv','a') as file:
#     wr = csv.writer(file, quoting=csv.QUOTE_ALL)
#     wr.writerow([Date, Hour, DownloadSpeed, UploadSpeed, Ping, IP, ISP, City, Country])

