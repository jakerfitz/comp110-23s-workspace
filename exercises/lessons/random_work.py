def closest_match(input_str):
    workout_types = ["arms/shoulders", "arnold switch", "legs/cardio", "chest/tri", "back/bi"]
    min_diff = float("inf")
    closest_match = None
    for workout in workout_types:
        diff = sum([1 for a, b in zip(input_str, workout) if a != b])
        if diff < min_diff:
            min_diff = diff
            closest_match = workout
    return closest_match

def suggest_workout(past_workouts, current_date):
    last_5_days = [w[1] for w in past_workouts[-5:]]
    upper_body_count = 0
    lower_body_count = 0
    for workout, date in past_workouts:
        if workout in ["arms/shoulders", "arnold switch", "chest/tri", "back/bi"]:
            upper_body_count += 1
        else:
            lower_body_count += 1
    if not past_workouts or current_date not in last_5_days:
        return "legs/cardio"
    if upper_body_count > lower_body_count:
        return "legs/cardio"
    if past_workouts[-1][0] in ["chest/tri", "back/bi"] and past_workouts[-1][1] == current_date:
        return "legs/cardio"
    return "arms/shoulders"

def main():
    past_workouts = []
    print("Enter a past workout (or type 'done' if done inputting past workouts):", end=" ")
    workout = input().strip().lower()
    while workout != "done":
        if workout not in ["arms/shoulders", "arnold switch", "legs/cardio", "chest/tri", "back/bi"]:
            workout = closest_match(workout)
        if not workout:
            print("Invalid workout input, please try again.")
            print("Enter a past workout (or type 'done' if done inputting past workouts):", end=" ")
            workout = input().strip().lower()
            continue
        print("Enter the current date in the format MM-DD (or type 'done' if done inputting past workouts):", end=" ")
        date = input().strip().lower()
        if date != "done":
            if len(date) == 3:
                date = "0" + date
            past_workouts.append((workout, date))
        print("Enter a past workout (or type 'done' if done inputting past workouts):", end=" ")
        workout = input().strip().lower()
    print("Enter the current date in the format MM-DD (or type 'done' if done inputting past workouts):", end=" ")
    current_date = input().strip().lower()
    if current_date != "done":
        if len(current_date) == 3:
            current_date = "0" + current_date
        suggested_workout = suggest_workout(past_workouts, current_date)
        print("Suggested workout:", suggested_workout)

if __name__ == '__main__':
    past_workouts = []
    workout = input("Enter a past workout (or type 'done' if done inputting past workouts): ")
    while workout.lower() != "done":
        date = input("Enter the date of the workout in the format MM-DD: ")
        if date.lower() != "done":
            past_workouts.append((workout, date))
        workout = input("Enter a past workout (or type 'done' if done inputting past workouts): ")

    current_date = input("Enter the current date in the format MM-DD: ")
    if current_date.lower() == "done":
        print("Exited input process.")
        exit()
    suggested_workout = suggest_workout(past_workouts, current_date)
    print("Today's suggested workout:", suggested_workout) 