from datetime import datetime, timedelta
import os

# Function to create the filename based on the current week
def create_rtf_filename():
    # Get today's date
    today = datetime.now()
    
    # Get the number of the current week of the year
    week_number = today.isocalendar()[1]
    
    # Get the starting date of the current week (Monday)
    monday_of_week = today - timedelta(days=today.weekday())
    
    # Format the date as YYYY-MM-DD
    formatted_date = monday_of_week.strftime("%Y-%m-%d")
    
    # Create the filename: YYYY-MM-DD_WeekXX.rtf
    filename = f"{formatted_date}_Week{week_number}.rtf"
    
    return filename

# Function to generate the RTF content, including a To-Do list format
def generate_rtf_content(week_number):
    content = r"""{\rtf1\ansi\deff0
    {\fonttbl{\f0 Arial;}}
    \f0\fs24 To-Do List for Week """ + str(week_number) + r"""
    
    \fs20 1. [ ] Task 1

    \line 2. [ ] Task 2
    \line 3. [ ] Task 3
    \line 4. [ ] Task 4
    \line 5. [ ] Task 5
    \line 6. [ ] Task 6
    \line 7. [ ] Task 7
    \line 8. [ ] Task 8
    \line 9. [ ] Task 9
    \line 10. [ ] Task 10
    }
    """
    return content

# Main function to create the RTF file in the desired directory
def create_rtf_file():
    # Define the directory where the RTF will be saved
    target_directory = r"C:\Users\nmkoninn\Desktop\to dos 2024"
    
    # Ensure the directory exists, if not, create it
    os.makedirs(target_directory, exist_ok=True)
    
    # Create the filename
    filename = create_rtf_filename()
    
    # Create the full file path
    full_file_path = os.path.join(target_directory, filename)
    
    # Get the current week number
    today = datetime.now()
    week_number = today.isocalendar()[1]
    
    # Generate RTF content
    rtf_content = generate_rtf_content(week_number)
    
    # Write the content to the RTF file
    with open(full_file_path, "w") as file:
        file.write(rtf_content)
    
    print(f"RTF file '{full_file_path}' has been created successfully.")

if __name__ == "__main__":
    create_rtf_file()
