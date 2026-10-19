"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

def get_temperatures():

    temps = [31, 30, 29, 28, 27, 25, 26]
    return temps

def analyze_temps(temp_list):

    average = sum(temp_list) / 7
    hight = max(temp_list)
    low = min(temp_list)

    return (average, hight, low)

def display_analysis(avg, hight, low):

    print("Temperature anaylsis for the week")
    print(f"Average: %.1f" % avg)
    print(f"Hight: %.1f" % hight)
    print(f"Low: %.1f" % low)

temps = get_temperatures()
print(temps)
result = analyze_temps(temps)
print(result)
display_analysis(result[0], result[1], result[2])