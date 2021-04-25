import momenter

momenter.format("YYYY MM DD HH MM SS")
momenter.format("YYYY MM DD HH MM")
momenter.format("YYYY MM DD HH")
momenter.format("YYYY MM DD")
momenter.format("YYYY MM")
momenter.format("YYYY")
momenter.format("MM")
momenter.format("DD")
momenter.format("HH")
momenter.format("MM")
momenter.format("SS")
momenter.format("h:m")
momenter.format("h:m:s")
momenter.format("m/d/y")

momenter.calendar()

momenter.moment()

momenter.between(600, 1600, "YYYY")
momenter.between(4, 5, "MM")
momenter.between(11, 14, "DD")
momenter.between(32, 44, "HH")
momenter.between(22, 34, "mm")
momenter.between(4, 14, "SS")

momenter.times(time={"year": 2018, "month": 12, "day": 24, "hour": 14, "minute": 22, "second": 14})

momenter.mydate(2007, "false", "false")

momenter.nowyear()
momenter.nowmonth()
momenter.nowday()
momenter.transform(365, "year")
momenter.transform(365, "month")
momenter.transform(365, "week")
momenter.transform(365, "day")

momenter.isvalid(7>12)
