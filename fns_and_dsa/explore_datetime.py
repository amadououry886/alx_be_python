from datetime import datetime, timedelta

def display_current_datetime():
    


    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time
    print(f"Current date and time: {formatted_date}")


def calculate_future_date():
    

    try:
        # Prompt the user to enter the number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()  # Get the current date
        future_date = current_date + timedelta(days=days_to_add)  # Calculate the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Please enter a valid integer for the number of days.")

def main():
    
    display_current_datetime()  # Display the current date and time
    calculate_future_date()  # Calculate and display the future date

if __name__ == "__main__":
    main()
