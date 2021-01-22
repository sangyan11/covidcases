from covid import Covid
covid=Covid()
y=input()
cases=covid.get_status_by_country_name(y)
for x in cases:
          print(x,":",cases[x])


