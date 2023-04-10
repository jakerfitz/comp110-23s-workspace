from collections import defaultdict

# Initialize a dictionary to store the assignments by day
assignments = defaultdict(list)

# Loop until the user wants to stop adding assignments
while True:
    day = input("Enter day of the week (Enter 'q' to quit): ")
    if day.lower() == 'q':
        break
    
    class_name = input("Enter class name: ")
    description = input("Enter assignment description: ")
    
    # Add the assignment to the list for the specified day
    assignments[day].append((class_name, description))

# Sort the assignments for each day by class name
for day, day_assignments in assignments.items():
    print(f"\n{day}:")
    day_assignments.sort(key=lambda x: x[0])
    for class_name, description in day_assignments:
        print(f"{class_name}: {description}")