# NOAA Integrated Surface Hourly Timeseries Dataset

The CSV[1922-csv] is built with the assumption you'll load the data into Pandas or something similar. 1922-csv is a sample-set. The full NOAA FTP data is available here(ftp://ftp.ncdc.noaa.gov/pub/data/noaa/readme.txt).

Also available is a fully, pre-processed dataset from 1901 -> 1978. To understand the columns, please reference ish-abbreviated.txt

### Larger Datasets Available

  * Request 1901 -to- 1977 here: https://goo.gl/forms/hpnI9Sjx0pCuUrxz2

### Loading Data

```
$ git clone git@github.com:jbcurtin/noaa-timeseries-dataset.git $HOME/noaa-timeseries-dataset
$ cd $HOME/noaa-timeseries-dataset
$ virtualenv -p $(which python3) env
$ source env/bin/activate
$ pip install pandas requests
$ python load-data.py
```
