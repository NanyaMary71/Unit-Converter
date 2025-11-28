# Unit-Converter
https://roadmap.sh/projects/unit-converter
Unit Converter Web App

A simple and beginner-friendly web application built with Flask that allows users to convert between units of length, weight, and temperature.

Users can input a value, choose the units to convert from and to, and instantly view the converted value—all handled on the server side.

📌 Features

Convert between length units
(millimeter, centimeter, meter, kilometer, inch, foot, yard, mile)

Convert between weight units
(milligram, gram, kilogram, ounce, pound)

Convert between temperature units
(Celsius, Fahrenheit, Kelvin)

Simple and clean user interface

Three separate pages for each measurement type

Backend logic handled using Python + Flask

No database required

📁 Project Structure
unit_converter/
│
├── app.py
├── templates/
│   ├── base.html
│   ├── length.html
│   ├── weight.html
│   ├── temperature.html
│
└── static/
    └── style.css

🚀 Getting Started
1. Clone the repository
git clone https://github.com/your-username/unit-converter.git
cd unit-converter

2. Create virtual environment (optional but recommended)
python -m venv venv


Activate it:

Windows:

venv\Scripts\activate


macOS / Linux:

source venv/bin/activate

3. Install dependencies
pip install flask

▶️ Running the Application

Start the Flask development server:

python app.py


Then open your browser and visit one of the pages:

http://127.0.0.1:5000/length
http://127.0.0.1:5000/weight
http://127.0.0.1:5000/temperature

🧠 How the App Works

Each page displays a form where the user:

Enters a numeric value

Selects the unit to convert from

Selects the unit to convert to

Submits the form

The server processes the conversion and displays the result on the same page

All conversion logic—length, temperature, weight—is written in app.py.

🧩 Technologies Used

Python

Flask

HTML5

CSS3

📸 Screenshots (Optional)

You may include screenshots of your UI here once your app is running.

📌 Future Improvements (Optional)

Add conversions for volume, speed, time, pressure, etc.

Add a JavaScript version (no page reload)

Add a single dashboard with all unit converters

Add dark mode

📜 License

This project is open-source and free to use for learning purposes.
