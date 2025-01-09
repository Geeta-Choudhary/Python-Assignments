import os

def menu():
    print("""
    Menu:
    1. Open File
    2. Read File
    3. Write to File
    4. Write a Line to File
    5. Read a Line from File
    6. Close File
    7. Rename File
    8. Exit
    """)

# Initialize file pointer
fp = None

while True:
    menu()
    choice = input("Enter your choice (1-8): ")

    if choice == "1":  # Open File
        filename = input("Enter the file name to open: ")
        try:
            fp = open(filename, "r+")
            print(f"File '{filename}' opened successfully.")
        except FileNotFoundError:
            print("File not found! Please try again.")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "2":  # Read File
        if fp:
            content=fp.read()
            print("File Content:")
            print(content)
        else:
            print("No file is open. Please open a file first.")

    elif choice == "3":  # Write to File
        if fp:
            content = input("Enter content to write: ")
            fp.write(content)
            fp.flush()
            print("Content written successfully.")
        else:
            print("No file is open. Please open a file first.")

    elif choice == "4":  # Write a Line to File
        if fp:
            line = input("Enter a line to write: ")
            fp.write(line + "\n")
            fp.flush()
            print("Line written successfully.")
        else:
            print("No file is open. Please open a file first.")

    elif choice == "5":  # Read a Line from File
        if fp:
            fp.seek(0)  # Move to the start of the file
            print("First Line:", fp.readline())
        else:
            print("No file is open. Please open a file first.")

    elif choice == "6":  # Close File
        if fp:
            fp.close()
            fp = None
            print("File closed successfully.")
        else:
            print("No file is open.")

    elif choice == "7":  # Rename File
        old_name = input("Enter the current file name: ")
        new_name = input("Enter the new file name: ")
        try:
            os.rename(old_name, new_name)
            print(f"File renamed to '{new_name}'.")
        except FileNotFoundError:
            print("File not found! Please try again.")
        except Exception as e:
            print(f"Error: {e}")

    elif choice == "8":  # Exit
        if fp:
            fp.close()
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")


