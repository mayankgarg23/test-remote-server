from fastmcp import FastMCP
import random
import json

# Create a FastMCP instance
mcp = FastMCP("Simple Calculator Server")

# Tool: Add two numbers

@mcp.tool
def add(a: float, b: float) -> float:
    """
    Add two numbers.
    Args: 
        a (float): The first number.
        b (float): The second number.
    Returns: 
        float: The sum of the two numbers.
    """
    return a + b

# Tool: Generate a random number

@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """
    Generate a random integer between min_val and max_val.
    Args:
        min_val (int): The minimum value.
        max_val (int): The maximum value.
    Returns:
        int: A random integer between min_val and max_val.
    """
    return random.randint(min_val, max_val)

# Resource: Server information
@mcp.resource("info://server")
def server_info() -> str:
    """
    Provides information about the server.
    Returns:
        str: A JSON string containing server information.
    """
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0",
        "description": "A basic MCP server with math tools",
        "tools": ["add", "random_number"],
        "author": "Your Name"
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0", port=8000)