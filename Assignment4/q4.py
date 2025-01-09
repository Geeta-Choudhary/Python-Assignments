skills_A = {'Python', 'Java', 'SQL'}
skills_B = {'Python', 'HTML', 'CSS'}
print(skills_A,skills_B)
inter=skills_A&skills_B
print(f"Intersection of two sets :{inter}")
deffer=skills_A-skills_B
print(f"Difference of two sets i.e Skills unique to skills_A:{deffer}")
deffer2=skills_B-skills_A
print(f"Difference of two sets  i.e Skills unique to skills_B:{deffer2}")
deffer1=skills_A^skills_B
print(f"Symmetric Difference of two sets :{deffer1}")
un=skills_A|skills_B
print(f"Union of two sets :{un}")

print()
#print(skills_B.difference(skills_A))


