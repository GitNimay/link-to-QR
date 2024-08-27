import os

# Prompt the user for a custom link
link = input("Enter the link you want to convert to a QR code: ")

# Ask the user if they want to save the QR code
save_qr = input("Do you want to save the QR code? (y/n): ").strip().lower()

# Default save path
save_path = r"make a dir and give its path to save genrated QR"

if save_qr == 'y':
    # Ensure the directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Prompt for the file name
    file_name = input("Enter the name for the QR code image (without extension): ")
    
    # Full path to save the QR code image
    file_path = os.path.join(save_path, f"{file_name}.png")
    
    # Command to generate QR code using curl and save it
    curl_command = f'curl "https://qrenco.de/{link}" -o "{file_path}"'
    
    # Execute the command in cmd and save the QR code
    os.system(f'start cmd /k "{curl_command}"')
    
    # Confirmation message
    print(f"QR code saved as {file_path}")

else:
    # Command to generate and display QR code using curl
    curl_command = f'curl "https://qrenco.de/{link}"'
    
    # Execute the command in cmd and display the QR code
    os.system(f'start cmd /k "{curl_command}"')
