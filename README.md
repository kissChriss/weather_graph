# Weather Graphs
Build your own beautiful weather web-based graphs from a pulled data out in csv format. 

![dtsywyvk1o](https://user-images.githubusercontent.com/32354154/36121881-9ed00a34-1058-11e8-9688-633156692c15.gif)

## Built With

* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - The Python library for pulling data out of HTML files.
* [Dash](https://plot.ly/products/dash/) - The Python framework for building analytical web applications.

## What inside

* [weather_parser.py](https://github.com/kissChriss/weather_graph/blob/master/weather_parser.py) 

It is the bs4 script for pulling data out of the [weather source](https://www.gismeteo.ru/weather-sankt-peterburg-4079/). 
Here - building URLs, analyzing data and creating csv-files with weather marks.

* [Months](https://github.com/kissChriss/weather_graph/tree/master/Months) 

The folder for data from [weather_parser.py](https://github.com/kissChriss/weather_graph/blob/master/weather_parser.py) 
Twelve csv months files with weather marks.

* [app.py](https://github.com/kissChriss/weather_graph/blob/master/app.py) 
    - is the Dash application for creating web-page with a graph
 
* [new.py](https://github.com/kissChriss/weather_graph/blob/master/new.csv)  
  - the temporary file which help for creating graphs
