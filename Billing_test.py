
# ---------------
        
from datetime import datetime
import sys
import os

def create_log_file(log_file_path, log_entries):

    # You have to give your local log file path [yours path : r'C:\\Users\\91938\\OneDrive\\Desktop\\test\\Fair_billing.txt']

    with open(r'C:\\Users\\91938\\OneDrive\\Desktop\\test\\Fair_billing.txt', 'w') as file:
        for entry in log_entries:
            file.write(f"{entry}\n")

def calculate_sessions(log_file_path):
    #Store session start times
    session_start_times = {}
    
    # Store session end times
    session_end_times = {}
    
    # Store the number of sessions and total duration for each user
    user_sessions = {}

    # The earliest start time and latest end time in the log file
    earliest_start_time = None
    latest_end_time = None

    with open(log_file_path, 'r') as file:
        for line in file:
           
            try:
                timestamp, user, action = line.strip().split(' ')
            except ValueError:
                continue  # Ignore invalid lines without a valid timestamp, username, and action

            
            time_format = '%H:%M:%S'
            current_time = datetime.strptime(timestamp, time_format)

            # Update earliest start time and latest end time
            if earliest_start_time is None or current_time < earliest_start_time:
                earliest_start_time = current_time
            if latest_end_time is None or current_time > latest_end_time:
                latest_end_time = current_time

            # Check if it's the start or end of a session
            if action.lower() == 'start':
                session_start_times[user] = current_time
            elif action.lower() == 'end':
                session_end_times[user] = current_time

    # Assume missing "End" entries
    for user in session_start_times:
        if user not in session_end_times:
            session_end_times[user] = latest_end_time

    # Assume missing "Start" entries
    for user in session_end_times:
        if user not in session_start_times:
            session_start_times[user] = earliest_start_time

    # Calculate the number of sessions and total duration for each user
    for user in session_start_times:
        start_time = session_start_times[user]
        end_time = session_end_times[user]
        duration = (end_time - start_time).total_seconds()

        # Update user_sessions dictionary
        user_sessions[user] = (user_sessions.get(user, (0, 0)))
        user_sessions[user] = (user_sessions[user][0] + 1, user_sessions[user][1] + duration)

    return user_sessions


def write_summary_to_log(log_file_path, user_sessions):
    with open(log_file_path, 'a') as file:
        file.write("\nUser_name:Session:Total_Time\n")
        for user, (num_sessions, total_duration) in user_sessions.items():
            file.write(f"{user} {num_sessions} {int(total_duration)}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("logs")
        sys.exit(1)

    log_file_path = sys.argv[1]
    log_entries = []

    print("Enter log entries (press Enter to finish):")
    while True:
        timestamp = datetime.now().strftime('%H:%M:%S')
        user = input("Enter username: ")
        action = input("Enter action (Start/End): ")
        
        log_entries.append(f"{timestamp} {user} {action}")

        cont = input("Do you want to enter another log entry? (y/n): ")
        if cont.lower() != 'y':
            break

    # Create the log file, You have to give your local log file file path [yours path : ] 
    create_log_file(r'C:\\Users\\91938\\OneDrive\\Desktop\\test\\Fair_billing.txt', log_entries)

    user_sessions = calculate_sessions(log_file_path)

    # Print the report
    for user, (num_sessions, total_duration) in user_sessions.items():
        print(f"{user}: {num_sessions} sessions, {int(total_duration)} seconds total duration")

    # You have to give your local log file file path [ yours path : r'C:\\Users\\91938\\OneDrive\\Desktop\\test\\Fair_billing.txt']

    write_summary_to_log(r'C:\\Users\\91938\\OneDrive\\Desktop\\test\\Fair_billing.txt', user_sessions)






    


