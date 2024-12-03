
import requests
import average_of_wind as av
from datetime import datetime
import if_system as if_sys
import str_manipulation as str_man


def extract_info_from_json(url):


    current_date = datetime.now().strftime('%Y-%m-%d')

    # Sending a GET request to the API.
    response = requests.get(url)

    # Checking the correctness of the request.
    if response.status_code == 200:

        # Receiving the content as JSON.
        data = response.json()
        forecast_data = data["data"][current_date]
        country_info = forecast_data["country"]
        daily_info = forecast_data["daily"]

    else:

        print(f"Request failed with status code: {response.status_code}")

    # the type of average is tuple
    average = av.average_wind(data)

    #Pass the description of the illustration's mood to a function that formats the paragraph neatly and appropriately.
    description = str_man.str_manipulations(country_info.get("description", "N/A"))



    # Format the data into a message
    message = (
        f"Forecast Day: {country_info.get('forecast_day', 'N/A')}\n"
        f"Description: {description}\n"
        f"Minimum Temperature: {daily_info.get('minimum_temperature', 'N/A')}\n"
        f"Maximum Temperature: {daily_info.get('maximum_temperature', 'N/A')}\n"
        
        
        # There may be situations where the average wind gust is unavailable or incomplete, 
        # but the function ensures that partial information is still processed and displayed.
        f"{average[0] if average else 'N/A'} {average[1] if average else ''}\n"
        f"Item of clothing: {if_sys.ifs(average[1]) if average else 'N/A' }\n"
        
        f"Maximum UVI: {daily_info.get('maximum_uvi', 'N/A')}"
    )

    return message



