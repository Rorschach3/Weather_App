
## Project Description

A basic Weather App created with two Python-based frameworks, Tkinter and Flask.

Tkinter is a standard GUI (Graphical User Interface) library in Python used for creating desktop applications. It provides a variety of widgets like buttons, labels, text boxes, and menus, allowing developers to design interactive and user-friendly interfaces.

Flask is a micro web framework in Python that is used to build web applications and APIs. It's lightweight and flexible, offering developers control over how they want to structure their applications. Flask supports extensions for database integration, form handling, authentication, and more, making it a popular choice for both simple and complex web projects.

This app uses OpenWeatherMap.org for retrieving real-time weather data based on user input.

Choose to either run the app using Flask or Tkinter. The user enters a city, and the app retrieves weather data using OpenWeatherMap's APIs. The information returned includes temperature, "feels like" temperature, high and low temperatures, and humidity. The Tkinter app retrieves a 3-day weather forecast, while the Flask app retrieves a 5-day weather forecast.

On the info button there is a short description of PM Accelerator, you can find more info on PM Accelerator on its Linkedin page:

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/school/productmanagerinterview/about/)
*********

#### Instructions: 

What We’re Looking For:

Make a weather app that:
Let users enter a city and get the current weather.
Shows the weather clearly, with any details you think are useful.

Extras (NOT required. But If You’re Up for It):
Add a 5-day forecast.
Let users see the weather based on their location.
Use icons or images to make the weather info look cool.

Again, use whatever technology stack you like!

*********
## Run Locally

### 1. Clone the project

```bash
  git clone https://github.com/Rorschach3/Weather_App.git
```

### 2. Go to the project directory

```bash
  cd Weather_App
```

### 3. Install VirtualEnv

```bash
  pip install virtualenv
```

### 4. creating virtualenv

```bash
  virtualenv env
```


### 5. Activating virtual environment\

``` bash
  source env/bin/activate 
```

### 6. Install requirements

```bash
  pip install -r requirements.txt
```

#### 7. Go to [OpenWeatherMap.org](https://openweathermap.org/api) and create an account to generate your own API Key. Once you copy your API Key rename both ".env.example" files to just ".env". then paste the API key and replace the text "paste your openweather api key here."

## 8. Choose Flask or Tkinter Weather_App

### 9. Tkinter

```bash
  cd tikinter
```

### 10. Run the Weather_App

```bash
  python weather_app.py
```

## OR

### 9. Flask

```bash
  cd flask
```

### 10. Run the App

```bash
  python app.py
```

*********

## Usage/Examples

Below is a link to a short video explaining the process of creating this weather app as well as deployment and usage.  

[Youtube Link](https://youtu.be/8jGxz7ASyd0)
