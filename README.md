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
*/60 * * * * python /home/pi/Speedtest.py

To run every half hour
*/30 * * * * python /home/pi/Speedtest.py
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

## Reference

* [Cron on Raspberry Pi](https://www.raspberrypi.org/documentation/linux/usage/cron.md) - Basic tutorial on how to schedule tasks

## Authors

* **Augusto Masetti** - *Initial work* - [AMasetti](https://github.com/AMasetti)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
