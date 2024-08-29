import pandas as pd
import pywhatkit 
import time

def extract_phone_numbers(excel_file, column_name):
    # Read the Excel file
    df = pd.read_excel(excel_file, dtype=str)
    
    # Extract the phone numbers from the specified column
    phone_numbers = df[column_name].tolist()
    
    return phone_numbers

# Function to send image and wait for confirmation
def send_image_with_confirmation(phone_number, image_path, caption, wait_time):
    # Send the image
    pywhatkit.sendwhats_image(phone_number, image_path, caption, 10)
    
    # Wait for the specified duration to ensure the message is sent
    print(f"Sent image to {phone_number}. Waiting for {wait_time} seconds...")
    time.sleep(wait_time)

# Example usage
excel_path = r"file.xlsx"
column_name = 'contact'  # Change this to the name of the column that contains phone numbers
image_path = "vote.jpg"
caption = " "
wait_time = 15
  # Adjust this time as needed for the sending process to complete

# Extract phone numbers
phone_numbers = extract_phone_numbers(excel_path, column_name)

# Send image to each phone number and wait for confirmation
for number in phone_numbers:
    send_image_with_confirmation(number, image_path, caption, wait_time)
    print(f"Image sent to {number}")
