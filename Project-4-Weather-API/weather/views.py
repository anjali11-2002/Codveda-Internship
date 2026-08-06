from django.shortcuts import render
import requests

API_KEY = "87011727319d8288cd5a64a03b1c848c"

def home(request):

    weather = None
    error = None

    if request.method == "POST":

        city = request.POST.get("city")

        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        response = requests.get(url)

        data = response.json()

        print(data)   # Debugging

        if str(data.get("cod")) == "200":

            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].title(),
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "feels_like": data["main"]["feels_like"],
            }

        else:

            error = data.get("message", "City Not Found")

    return render(
        request,
        "index.html",
        {
            "weather": weather,
            "error": error,
        },
    )