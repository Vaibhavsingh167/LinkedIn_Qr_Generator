# 🔗 LinkedIn QR Code Generator (Flask)

A simple Flask web application that takes a LinkedIn profile URL, validates it, and generates a downloadable QR code for easy sharing.

## Features

- Validates LinkedIn URLs (with `http/https`, `linkedin.com`, `www.`, and subdomains)
- Generates QR code images using the `qrcode` library
- Displays and offers QR code download
- Responsive design and accessibility-friendly
- Basic sanitization and clear error messages

## Installation

1. **Clone the repo**
    ```bash
    git clone https://github.com/yourname/linkedin-qr-generator.git
    cd linkedin-qr-generator
    ```
2. **Create & activate venv**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Mac/Linux
    venv\\Scripts\\activate  # Windows
    ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

Visit http://127.0.0.1:5000 in your browser, paste a LinkedIn URL, and get your QR code!

## Project Structure
linkedin_qr_generator/
├── .gitignore
├── requirements.txt
├── app.py
├── templates/
├── static/
└── README.md
