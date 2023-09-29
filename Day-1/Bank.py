total_amount=int(input("principle:"))
i=int(input("rate of interest:"))
m5=int(input("amount withdrawn:"))
m9=int(input("amount added:"))
intrest_upto_5months=(total_amount*4/12*i)/100;
intrest_upto_9months=((total_amount-m5)*4/12*i)/100;
remaining_months=((total_amount-m5+m9)*4/12*i)/100;
print((total_amount-m5+m9)+intrest_upto_5months+intrest_upto_9months+remaining_months)
