from datetime import datetime


def average_wind(data):

    current_date = datetime.now().strftime('%Y-%m-%d')

    # Defining variables to calculate the count and provide a summary of the wind speed data.

    wind_speeds = 0
    count_the_times_of_wind_speeds = 0


    # Check: Does the current date exist in the information.

    if current_date in data["data"]:
        date_info = data["data"][current_date]


        # This loop processes hourly wind speed data from date_info["hourly"],
        # extracting the wind speed for each hour using the "wind_speed" key.

        for hour, details in date_info["hourly"].items():

            wind_speed = details.get("wind_speed")

            if wind_speed is not None:  # בודק שהערך קיים ושאינו None
                wind_speeds += (int(wind_speed))
                count_the_times_of_wind_speeds += 1
    else:
        print(current_date, 'date not exist')

    #Calculation of the wind average.
    average_wind_speed = wind_speeds // count_the_times_of_wind_speeds

    return("Average Wind Speed:", average_wind_speed)





