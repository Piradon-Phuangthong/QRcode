import qrcode

# Step 1: Take input from the user
website = input("Enter the website URL to generate a QR code: ")

# Step 2: Generate the QR Code
qr = qrcode.QRCode(
    version = 1, # Controls the size of the QR Code
    error_correction = qrcode.constants.ERROR_CORRECT_L, # Erro correction level
    box_size = 10, # Size of each box in the QR code grid
    border = 1, # Thickness of the border (minimum = 4)
)

qr.add_data(website) # Add the input website to the QR code
qr.make(fit=True) # Optimise the QR code for the input data

# Step 3: Create the QR code image
qr_code_image = qr.make_image(fill_color = "black", back_color = "white")

# Step 4: Save the QR code as an image file
qr_code_image.save("qr_code.png")
print("QR code save as 'qr_code.png'.")