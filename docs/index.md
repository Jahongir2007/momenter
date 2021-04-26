## Momenter v1.1.8
### Run this library
1. Install .zip file in github
2. Copy file: pynumeral-main/bin/momenter.py
3. Create new folder and paste momenter.py
4. Create new (for example test.py) .py file in this folder (the folder must contain a momenter file)
5. Write the code to your newly opened .py file and run it, following the Momenter syntax
### Importting Momenter
Import Mometer:
```python
import momenter
```
### Create
If you want to create your own date, then you need to use the `mydate()` method.
```python
a = [2007, 25, 5]
b = value(a)
def MyFunction():
  global b
  momenter.mydate(b)
```
### Calendar
For current date:
```python 
momenter.calendar() # Sun Apr 25 19:31:42 2021
```
### Formatting

You can format the current view in different views using the `format()` method.

```python
momenter.format("YYYY MM DD HH MM SS") # 2021 04 Sunday 10 16 36
momenter.format("YYYY MM DD HH MM") # 2021 04 Sunday 10 16
momenter.format("YYYY MM DD HH") # 2021 04 Sunday 10
momenter.format("YYYY MM DD") # 2021 04 Sunday
momenter.format("YYYY MM") # 2021 04 
momenter.format("YYYY") # 2021
momenter.format("MM") # 04
momenter.format("DD") # Sunday
momenter.format("HH") # 10
momenter.format("MM") # 16
momenter.format("SS") # 36
momenter.format("h:m") # 10:16
momenter.format("h:m:s") # 10:16:36
momenter.format("m/d/y") # 04/25/21
```
### Get now date
You can use the `calendar()` method to see today's date.

```python
momenter.calendar() #Sun Apr 25 10:16:36 2021
```
### Current hours
If your watch is broken, the `moment()` method will help you.
```python
momenter.moment() # 10:16:36
```

### Calc between times
The `betwean()` method is used to find the time from one time to the next:
```python
momenter.between(600, 1600, "YYYY") # 1000 years
momenter.between(4, 5, "MM") # 1 month
momenter.between(11, 14, "DD") # 3 days
momenter.between(32, 44, "HH") # 12 hours
momenter.between(22, 34, "mm") # 12 minutes
momenter.between(4, 14, "SS") # 10 seconds
```
### dict time
Python dict data types:
```python
momenter.times(time={"year": 2018, "month": 12, "day": 24, "hour": 14, "minute": 22, "second": 14})
# {'year': 2018, 'month': 12, 'day': 24, 'hour': 14, 'minute': 22, 'second': 14}
```
### Get your date
Get your date:
```python
momenter.mydate(2007, 25, 5) # 2007.25.5
momenter.mydate(2007, "false", 5) # 2007.5
```
### Current year, month and day
To know the current year, month, and day, use the `nowyear()`, `nowmonth()`, and `nowday()` methods:
```python
momenter.nowyear() # 2021
momenter.nowmonth() # 4
momenter.nowday() # Sunday
```
### Formatting times 
To display the desired numbers in time:
```python
momenter.transform(365, "year") # 1 year
momenter.transform(365, "month") # 12 months
momenter.transform(365, "week") # 52.142857142857146 weeks
momenter.transform(365, "day") # 365.0 days
```
### Validation
Returns `true` or `false` value.
```python
momenter.isvalid(7>12) # false
momenter.isvalid(5=5) # true
```
### Clone
To get the values ​​you need to use the `clone()` method:
```python
a = 18
momenter.clone(a) # 18
```
### UTC
Get UTC:
```python
momenter.utc() # 2021-04-25 13:01:54.547693
```
### Array
Use the `toArray()` method to array a given date.
```python
momenter.toArray([2007, 25, 5]) # 2007 / 25 / 5 
```
### Unix timestamp
To know the Unix time, use the `unix()` method:
```python
momenter.unix(5) # 1619379180
```
### Millisecond
To view the current milliseconds:
```python
momenter.millisecond() # 1619368076475
```
### Second
To view the current seconds:
```python
momenter.second() # 55
```
### Minute
To view the current minutes:
```python
momenter.minute() # 43
```
### Hour
To view the current hours:
```python
momenter.hour() # 21
```
### Get
To view all current time types:
```python
momenter.get("day") # Monday
momenter.get("week") # 17
momenter.get("month") # 04
momenter.get("year") # 2021
momenter.get("millisecond") # 1619415502716
momenter.get("second") # 22
momenter.get("minute") # 38
momenter.get("hour") # 10
```
### Set
To set times:
```python
momenter.set("month", 5) # May
momenter.set("date", 25) # 25
momenter.set("second", 30) # 30
momenter.set("minute", 40) # 40
momenter.set("hour", 20) #  20
```
