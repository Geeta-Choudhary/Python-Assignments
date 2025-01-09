def vowel_counter():
    count = 0
    s=input('Enter a string: ').strip().lower()
    for char in s:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            count += 1
    if count>0:
        print(f"Number of vowels in string [{s}] is:{count}")
    else:
        print(f"No vowels present in string [{s}]")

if __name__ == '__main__':
    vowel_counter()
