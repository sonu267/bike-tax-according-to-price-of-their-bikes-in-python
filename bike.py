bike = int(input("enter cost of your bike (in ruppes) : "))
# print("your bike seems to be costly")
if (bike>100000 ):
    print("road tax to be paid for your bike is \"15% \" ")
if (bike > 50000 and bike<=100000 ):
    print("road tax to be paid for your bike is \"10% \" ")
if (bike<= 50000):
    print("road tax to be paid for your bike is \"5% \" ")