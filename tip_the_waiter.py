def total_calc(bill_amount, total_perc):
    #define function to calculate the amount of bill
    total = bill_amount*(1+0.01*total_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")
#specify only bill amount
#defaulf value of tip percentage is used
total_calc(150, 20)