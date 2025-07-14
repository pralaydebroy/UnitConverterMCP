from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("UnitConverterMCP")

# Tool: Convert kilometers to miles
@mcp.tool()
def km_to_miles(km: float) -> str:
    """Convert kilometers to miles"""
    miles = km * 0.621371
    return f"{km} kilometers is equal to {miles:.2f} miles."

# Tool: Convert Celsius to Fahrenheit
@mcp.tool()
def celsius_to_fahrenheit(celsius: float) -> str:
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return f"{celsius}°C is equal to {fahrenheit:.2f}°F."

# Tool: Convert kilograms to pounds
@mcp.tool()
def kg_to_pounds(kg: float) -> str:
    """Convert kilograms to pounds"""
    pounds = kg * 2.20462
    return f"{kg} kilograms is equal to {pounds:.2f} pounds."

# Tool: Convert liters to gallons
@mcp.tool()
def liters_to_gallons(liters: float) -> str:
    """Convert liters to US gallons"""
    gallons = liters * 0.264172
    return f"{liters} liters is equal to {gallons:.2f} gallons."

# Resource: Greeting
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}! Welcome to the Unit Converter MCP server."

if __name__ == "__main__":
    mcp.run()
