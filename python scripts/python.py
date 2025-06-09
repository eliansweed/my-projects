from datetime import datetime, timedelta

#names
def generate_names(num_people):
    names = []
    for i in range(num_people):
        name = input(f"Enter the name of person {i+1}: ")
        names.append(name)
    return names

#When everyone finish
def calculate_start_end_times(current_day, end_day, num_people, names, start_hour, end_hour):
    start_datetime = datetime.now().replace(hour=start_hour.hour, minute=start_hour.minute) + timedelta(days=current_day-1)
    end_datetime = datetime.now().replace(hour=end_hour.hour, minute=end_hour.minute) + timedelta(days=end_day-1)
    total_hours = (end_datetime - start_datetime).days * 24 + (end_datetime - start_datetime).seconds // 3600
    hours_per_person = total_hours / num_people

    print("Start and end times per person:")
    for i in range(num_people):
        name = names[i]
        person_start_datetime = start_datetime + timedelta(hours=i * hours_per_person)
        person_end_datetime = person_start_datetime + timedelta(hours=hours_per_person)
        print(f"{name}: {person_start_datetime.strftime('%H:%M')} - {person_end_datetime.strftime('%H:%M')}")

# names + hour input
current_day = int(input("Enter the current day (1-31): "))
end_day = int(input("Enter the end day (1-31): "))
num_people = int(input("Enter the number of people: "))
names = generate_names(num_people)
start_hour = datetime.strptime(input("Enter the start hour (HH:MM): "), "%H:%M")
end_hour = datetime.strptime(input("Enter the end hour (HH:MM): "), "%H:%M")

#here calculate
calculate_start_end_times(current_day, end_day, num_people, names, start_hour, end_hour)