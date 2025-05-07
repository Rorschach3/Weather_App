<!-- Project Title -->

<p align="center">
  <img src="https://github.com/user-attachments/assets/9677be95-dc22-4c8c-9890-745a7fa8d332" alt="Weather App Screenshot" width="600"/>
</p>

# Weather App

A dual-interface weather application built with **Python**, offering both a **Flask**-powered web UI and a **Tkinter** desktop GUI. It fetches real-time and forecast data from OpenWeatherMap’s API, displaying temperature, “feels like” values, highs/lows, and humidity. The Tkinter version shows a 3-day forecast; the Flask version extends to 5 days.

---

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Live Demo & Screenshot](#live-demo--screenshot)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Running the App](#running-the-app)

   * [Tkinter GUI](#tkinter-gui)
   * [Flask Web App](#flask-web-app)
7. [Usage](#usage)
8. [Credits](#credits)

---

## Features

* **City Search**: Enter any city to retrieve current weather.
* **Detailed Metrics**: Displays temperature, “feels like,” high/low, humidity.
* **3-Day vs. 5-Day Forecast**:

  * Tkinter GUI → 3-day forecast
  * Flask Web UI → 5-day forecast
* **Location Info**: (Optional) Can be extended to auto-detect user location.
* **Extensible Design**: Icons, geolocation, and additional data layers easily integrated.

---

## Tech Stack

| Component        | Framework / Library |
| ---------------- | ------------------- |
| Web Framework    | Flask               |
| Desktop GUI      | Tkinter             |
| HTTP Requests    | `requests`          |
| Environment Vars | `python-dotenv`     |
| API              | OpenWeatherMap      |
| Language         | Python 3.x          |

---

## Live Demo & Screenshot

Watch the usage video and deployment walkthrough:

[▶ View on YouTube](https://youtu.be/8jGxz7ASyd0)

**Web UI Screenshot**

<p align="center">
  <img src="https://github.com/user-attachments/assets/9677be95-dc22-4c8c-9890-745a7fa8d332" alt="Weather App Screenshot" width="600"/>
</p>

---

## Installation

```bash
# 1. Clone the repo
git clone https://github.com/Rorschach3/Weather_App.git
cd Weather_App

# 2. (Optional) Create virtual environment
python3 -m venv env
source env/bin/activate    # Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Configuration

1. Sign up at [OpenWeatherMap.org](https://openweathermap.org/api).
2. Copy your **API Key**.
3. Rename both `.env.example` files (in the root, `flask/`, and `tkinter/` folders) to `.env`.
4. Inside each `.env`, replace:

   ```
   OPENWEATHER_API_KEY="paste your openweather api key here"
   ```

---

## Running the App

Choose your preferred interface:

### Tkinter GUI

```bash
cd tkinter
python weather_app.py
```

### Flask Web App

```bash
cd flask
python app.py
```

Open the Flask UI at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Usage

1. Launch the chosen interface.
2. Enter a **city name** in the input field.
3. Submit to view current conditions and forecast.
4. (Tkinter) Browse the 3-day forecast.
5. (Flask) Navigate the 5-day forecast cards.

---

## Credits

* Developed by **Daniel Hernandez**
* Based on requirements from PM Accelerator:
  [![LinkedIn](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge\&logo=linkedin\&logoColor=white)](https://www.linkedin.com/school/productmanagerinterview/about/)
