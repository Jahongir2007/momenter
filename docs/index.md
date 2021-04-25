### Momenter v1.0.1
### Importting Momenter

Import Mometer:
```python
import momenter
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
```python
momenter.between(600, 1600, "YYYY") # 1000 years
momenter.between(4, 5, "MM") # 1 month
momenter.between(11, 14, "DD") # 3 days
momenter.between(32, 44, "HH") # 12 hours
momenter.between(22, 34, "mm") # 12 minutes
momenter.between(4, 14, "SS") # 10 seconds
```
### dict time
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
