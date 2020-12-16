deposit_sum = float(input())
deposit_period = int(input())
years_percent = float(input())

#сума = депозирана сума + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

result_sum = deposit_sum + deposit_period * ((deposit_sum*years_percent/100)/12)

print(result_sum)
