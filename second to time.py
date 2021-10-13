print("please enter your seconds:")
sec = int(input('seconds= '))
hour = sec // 3600
minute = (sec - 3600 * hour) // 60
second = (sec - 3600 *hour) - 60 * minute
print("time= ", hour,':', minute,':', second )