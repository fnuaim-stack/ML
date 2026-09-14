# Weather Dashboard

A comprehensive weather dashboard built with Python and Jupyter Notebooks that fetches real-time weather data from the OpenWeatherMap API.

## Features

✨ **Core Features:**
- Real-time weather data for any city worldwide
- Current weather conditions (temperature, humidity, wind, pressure)
- 5-day weather forecast with detailed predictions
- Interactive visualizations and plots
- Multi-city weather comparison
- Weather statistics and analytics
- Responsive error handling

📊 **Visualizations:**
- Temperature trends with min/max ranges
- Humidity levels over time
- Wind speed analysis
- Precipitation forecasts
- Multi-city comparison charts

## Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Notebook or JupyterLab
- Internet connection for API calls

### Installation

1. Clone or download the repository:
```bash
git clone https://github.com/fnuaim-stack/ML.git
cd ML
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Get your API key:
   - Visit [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Generate an API key

4. Set up your API key:
   - Create a `.env` file in the project directory:
   ```
   OPENWEATHERMAP_API_KEY=your_api_key_here
   ```
   - Or directly in the notebook: `API_KEY = 'your_api_key_here'`

5. Launch Jupyter:
```bash
jupyter notebook
```

6. Open `weather_dashboard.ipynb` and start exploring!

## Usage

### Basic Usage

```python
# Import the dashboard function
from weather_dashboard import weather_dashboard

# Get weather for a city
weather_dashboard('London')
```

### Compare Multiple Cities

```python
from weather_dashboard import compare_cities

cities = ['London', 'New York', 'Tokyo', 'Sydney']
comparison = compare_cities(cities)
```

### Customize Units

```python
# Use Fahrenheit instead of Celsius
weather_dashboard('New York', units='imperial')
```

## API Reference

### Main Functions

#### `get_current_weather(city, api_key, units='metric')`
Fetch current weather data for a specific city.

**Parameters:**
- `city` (str): City name
- `api_key` (str): OpenWeatherMap API key
- `units` (str): 'metric' for Celsius or 'imperial' for Fahrenheit

**Returns:**
- JSON response with current weather data

#### `get_forecast(city, api_key, units='metric')`
Fetch 5-day forecast data for a city.

**Parameters:**
- `city` (str): City name
- `api_key` (str): OpenWeatherMap API key
- `units` (str): Temperature units

**Returns:**
- JSON response with forecast data

#### `weather_dashboard(city, api_key)`
Run the complete weather dashboard for a city.

**Parameters:**
- `city` (str): City name
- `api_key` (str): OpenWeatherMap API key

#### `compare_cities(cities, api_key)`
Compare current weather across multiple cities.

**Parameters:**
- `cities` (list): List of city names
- `api_key` (str): OpenWeatherMap API key

**Returns:**
- Pandas DataFrame with comparison data

## Data Returned

### Current Weather
- City and country
- Temperature (current, feels like, min, max)
- Humidity and pressure
- Wind speed
- Cloud coverage
- Weather description
- Timestamp

### Forecast Data
- Temperature forecasts
- Humidity predictions
- Wind speed projections
- Precipitation amounts
- Cloud coverage
- Weather conditions

## Customization

### Change Display Units
Edit the `DEFAULT_UNITS` variable:
```python
DEFAULT_UNITS = 'imperial'  # For Fahrenheit
```

### Add More Visualizations
Extend the `plot_forecast()` function to add:
- Pressure trends
- Cloud coverage charts
- UV index tracking
- Sunrise/sunset times

### Enable Caching
Uncomment the caching code to store results and reduce API calls

## Examples

### Example 1: Weekly Weather Check
```python
weather_dashboard('Paris')
```

### Example 2: Compare Vacation Destinations
```python
compare_cities(['Barcelona', 'Rome', 'Athens', 'Istanbul'])
```

### Example 3: Temperature Analysis
```python
forecast_data = get_forecast('London')
forecast_df = parse_forecast(forecast_data)
print(forecast_df['temperature'].describe())
```

## Troubleshooting

### "API key not found"
- Ensure `API_KEY` variable is set correctly
- Check your .env file exists and is formatted correctly

### "City not found"
- Verify the city name is spelled correctly
- Use English names for cities
- Try adding country code (e.g., 'London,UK')

### "Request timeout"
- Check your internet connection
- The API might be temporarily unavailable
- Retry after a few moments

### "Rate limit exceeded"
- Free tier allows 60 calls per minute
- Wait a minute before making more requests
- Consider upgrading your plan

## API Limits

**Free Tier:**
- 60 calls/minute
- Forecast data every 3 hours
- 5-day forecasts maximum
- Current weather only

**Paid Tiers:** Available with higher limits

## Future Enhancements

🎯 Planned Features:
- [ ] Historical weather data analysis
- [ ] Weather alerts and notifications
- [ ] Interactive web dashboard (with Streamlit)
- [ ] Air quality index integration
- [ ] Map-based visualization
- [ ] Severe weather warnings
- [ ] Precipitation probability charts
- [ ] Database integration for data logging

## Resources

- [OpenWeatherMap API Docs](https://openweathermap.org/api)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)
- [Jupyter Documentation](https://jupyter.org/)

## License

This project is open source. Feel free to use and modify for your needs.

## Support

For issues or questions:
1. Check the Troubleshooting section
2. Review the OpenWeatherMap API documentation
3. Create an issue in the repository

---

**Happy Weather Tracking!** 🌤️⛅🌈
