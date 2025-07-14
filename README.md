# Build Your First MCP Server: Unit Converter

This AI tool helps with basic unit conversions such as distance, temperature, weight, and volume. The codebase here defines a minimal MCP server that exposes these as callable tools for any AI agent that supports MCP (Model Context Protocol).

The server can be tested easily using Claude Desktop or any compatible client.

---

## Setup steps

1. **Install Claude Desktop**  
   (Used here to test the MCP tool server.)

2. **Install uv**  
   ```bash
   pip install uv

3. **Initialize your project directory**
   ```bash
   uv init unit-converter-mcp
   cd unit-converter-mcp

4. **Add MCP CLI to your project**

    ```bash
    uv add "mcp[cli]"

5. **Fix any type errors (if needed)**
    Some users may get type-related errors. Run:
    ```bash
    pip install --upgrade typer

6. **Write your code**
    Add your MCP server code to main.py. This project includes:

    km_to_miles(km)

    celsius_to_fahrenheit(celsius)

    kg_to_pounds(kg)

    liters_to_gallons(liters)

7. **Install the MCP server locally**
    Inside your project directory, run:

    ```bash
    uv run mcp install main.py

8. **Restart Claude Desktop**
    Kill any running instance of Claude from Task Manager (or Activity Monitor), then reopen Claude Desktop.

9. **Test your server**
    Claude Desktop will now detect your tool server and show all available tools automatically.

