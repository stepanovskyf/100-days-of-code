sum_all = input("How much is a bill? ")
tip = input("How much do you want to tip? ")
num_people = input("How many people are paying? ")
tip_mult = ("1." + str(tip))
tip_mult = float(tip_mult)
one_person = round(float(sum_all)*tip_mult/float(num_people), 2)
one_person = "{:.2f}".format(one_person)
print(f"How much should each person pay is {one_person}")