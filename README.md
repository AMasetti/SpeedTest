# SpeedTest

 Automatic Speedtest Script for recording Internet connection data.

### Prerequisites

Dependencies instalation

```
 pip install -r requirements.txt 
```

### Installing

Place the SpeedTestLogger.py in the /home/pi/ folder on you Raspberry Pi. Create the required Cron Tasks using the command

```
 crontab -e
```

I made my Script to run every Hour and Half Hour, these are the entries used:

```
To run every hour
0 0 * * * python /home/pi/Speedtest.py
0 1 * * * python /home/pi/Speedtest.py
0 2 * * * python /home/pi/Speedtest.py
0 3 * * * python /home/pi/Speedtest.py
0 4 * * * python /home/pi/Speedtest.py
0 5 * * * python /home/pi/Speedtest.py
0 6 * * * python /home/pi/Speedtest.py
0 7 * * * python /home/pi/Speedtest.py
0 8 * * * python /home/pi/Speedtest.py
0 9 * * * python /home/pi/Speedtest.py
0 10 * * * python /home/pi/Speedtest.py
0 12 * * * python /home/pi/Speedtest.py
0 13 * * * python /home/pi/Speedtest.py
0 14 * * * python /home/pi/Speedtest.py
0 15 * * * python /home/pi/Speedtest.py
0 16 * * * python /home/pi/Speedtest.py
0 17 * * * python /home/pi/Speedtest.py
0 18 * * * python /home/pi/Speedtest.py
0 19 * * * python /home/pi/Speedtest.py
0 20 * * * python /home/pi/Speedtest.py
0 21 * * * python /home/pi/Speedtest.py
0 22 * * * python /home/pi/Speedtest.py
0 23 * * * python /home/pi/Speedtest.py

To run every half hour
30 0 * * * python /home/pi/Speedtest.py
30 1 * * * python /home/pi/Speedtest.py
30 2 * * * python /home/pi/Speedtest.py
30 3 * * * python /home/pi/Speedtest.py
30 4 * * * python /home/pi/Speedtest.py
30 5 * * * python /home/pi/Speedtest.py
30 6 * * * python /home/pi/Speedtest.py
30 7 * * * python /home/pi/Speedtest.py
30 8 * * * python /home/pi/Speedtest.py
30 9 * * * python /home/pi/Speedtest.py
30 10 * * * python /home/pi/Speedtest.py
30 12 * * * python /home/pi/Speedtest.py
30 13 * * * python /home/pi/Speedtest.py
30 14 * * * python /home/pi/Speedtest.py
30 15 * * * python /home/pi/Speedtest.py
30 16 * * * python /home/pi/Speedtest.py
30 17 * * * python /home/pi/Speedtest.py
30 18 * * * python /home/pi/Speedtest.py
30 19 * * * python /home/pi/Speedtest.py
30 20 * * * python /home/pi/Speedtest.py
30 21 * * * python /home/pi/Speedtest.py
30 22 * * * python /home/pi/Speedtest.py
30 23 * * * python /home/pi/Speedtest.py
```

## Running

The Script will run every time a Cron Task is executed generating a log file named LogSpeedTest.csv with the following data structured in columns:

* Date
* Time
* Donwload Speed in Mb/s
* Upload Speed in Mb/s
* Ping in ms
* IP
* ISP
* City
* Country

## Built With

* [Speedtest-CLI](https://pypi.org/project/speedtest-cli/) - Library used
## Authors

* **Augusto Masetti** - *Initial work* - [AMasetti](https://github.com/AMasetti)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
