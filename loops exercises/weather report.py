
# The variable data contains 24 temperature readings from 24 hours
# Every 4 characters equals one hundredth degree Celsius reading,
# ie "2150" to 21.50 ° C
# Measurements are 00:00 hours to full hours from 23:00

# Display the report in the console in the following format:
# <hour>: <tabulator><degrees with precision to second decimal place><degree sign>C

# For reads equal to or equal to 20°C, add "<tabulator>!"
# For events equal to, or equal to, 18,5°C, add an exclamation mark

# Please do not copy the degree sign. Try using unicode sign \u00b0

# The target result is below

data = "215021482120211921002076207620502065202020152010200520002001199319901950183417501744186019462010"

for x in range(24):
    if x < 10:
        hour = f"0{x}:00"
    else:
        hour = f"{x}:00"
    temperature = int(data[x*4:(x+1)*4])/100
    print(f"{hour}: {temperature:.2f}\u00b0C{' !!' if temperature<= 18.5 else ' !' if temperature<= 20 else ''}")


"""
00:00:	21.50°C
01:00:	21.48°C
02:00:	21.20°C
03:00:	21.19°C
04:00:	21.00°C
05:00:	20.76°C
06:00:	20.76°C
07:00:	20.50°C
08:00:	20.65°C
09:00:	20.20°C
10:00:	20.15°C
11:00:	20.10°C
12:00:	20.05°C
13:00:	20.00°C	!
14:00:	20.01°C
15:00:	19.93°C	!
16:00:	19.90°C	!
17:00:	19.50°C	!
18:00:	18.34°C	!!
19:00:	17.50°C	!!
20:00:	17.44°C	!!
21:00:	18.60°C	!
22:00:	19.46°C	!
23:00:	20.10°C
"""
