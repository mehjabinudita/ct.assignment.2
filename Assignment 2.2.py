sec=int(input("Enter seconds:"))
h=sec//3600
sec2=sec%3600
min=sec2//60
sec3=sec2%60
print(sec, "Seconds is",h,"hours,",min,"minutes,",sec3,"seconds")