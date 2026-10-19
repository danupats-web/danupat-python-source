"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
phone = input("Enter your phone: ")

check_n = False
for char in name:
    if char.isalpha() or char.isspace():
        check_name = True
    else:
        check_name = False
        break

check_a = False
if 18 <= age <= 65:
    check_age = True

check_p = False
if phone.isdigit() and len(phone) == 10:
    check_phone = True

print("\nValidation Results: ")
if check_n:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid")

if check_a:
    print(f"Age: Valid {age} years old")
else:
    print("Age: Invalid")

if check_p:
    print(f"Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid")

print("\nFormatted Information:")
print(f"Name: {name.upper()}")
if 18 <= age <= 30:
    print("Age group: Young Adult (18-30)")
elif 31 <= age <= 60:
    print("Age group: Adult (31-60)")
else:
    print("Age group: Senior")

print(f"Phone: +91 {phone}")