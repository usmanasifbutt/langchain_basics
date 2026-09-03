import requests
from fastmcp import FastMCP


mcp  = FastMCP(name="Weather MCP")


@mcp.tool("get_weather", description="Get weather for a location")
def get_weather(location: str) -> dict:
    """Get weather for a given location."""
    response = requests.get(f"https://wttr.in/{location}?format=j1")
    return response.json()


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)