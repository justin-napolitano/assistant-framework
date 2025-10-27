from typing import Optional
from pydantic import BaseModel, Field
from langchain.tools import StructuredTool
from services.weather_client import weather_today

class WeatherInput(BaseModel):
    city: Optional[str] = Field(None, description="City name, e.g., Orlando")
    state: Optional[str] = Field(None, description="State or region code, e.g., FL")

def _weather_tool(city: Optional[str] = None, state: Optional[str] = None) -> str:
    return weather_today(city, state)

weather_tool = StructuredTool.from_function(
    name="weather_today",
    description="Get today's concise weather summary for a city and state.",
    args_schema=WeatherInput,
    func=_weather_tool,
)
