# QR Code Generator 📷

A Python-based application to generate QR codes from user-provided URLs. This project leverages the `qrcode` and `Pillow` libraries to create and save QR codes as images.

## Features

- Generate QR codes for any website or text.
- Customize the size and color of QR codes.
- Save QR codes as image files (`.png`).

## Prerequisites

- Python 3.8 or higher.
- Libraries: `qrcode`, `Pillow`.

## Installation

1. **Clone the repository:**

2. **Set up the environment:**
   - Option 1: **Global Installation**
     Install the required libraries globally:
     ```bash
     pip install qrcode pillow
     ```

   - Option 2: **Virtual Environment** *(Recommended)*
     ```bash
     python3.8 -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     pip install qrcode pillow
     ```

## Usage

1. Run the script:
   ```bash
   python qr_code_generator.py
   ```

2. Enter the URL when prompted:
   ```
   Enter the website URL to generate a QR code: https://example.com
   ```

3. The QR code will be saved as `qr_code.png` in the project directory.

4. Open the image file to view the QR code or scan it with a QR code scanner.

## File Structure

```
qr-code-generator/
│
├── qr_code_generator.py   # Main script
├── README.md              # Project documentation
```


