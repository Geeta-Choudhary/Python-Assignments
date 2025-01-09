people = {
	'John': {'age': 45, 'city': 'New York'},
	'Mike': {'age': 22, 'city': 'Los Angeles'},
	'Sarah': {'age': 32, 'city': 'New York'},
	'Anna': {'age': 28, 'city': 'Chicago'}
}
# Loop through each person in the dictionary
for name, value in people.items():
    # Check if the person lives in New York and is over 30 years old
    if value['city'] == 'New York' and value['age'] > 30:
        print(name)
