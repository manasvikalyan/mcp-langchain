from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def add(a: int, b: int) -> int:
    """_summary_
    Add two numbers
    """
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    Subtract two numbers
    """
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers
    """
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> int:
    """
    Divide two numbers
    """
    return a / b

@mcp.tool()
def power(a: int, b: int) -> int:
    """
    Raise a number to the power of another number
    """
    return a ** b  

if __name__ == "__main__":
    mcp.run(transport="stdio")

# stdio is a transport that allows the MCP server to communicate with the client over the standard input and output streams.
# with the help of stdio we can run the server in the terminal and the client can be a python script that uses the MCP client to interact with the server.