from mcp.server.fastmcp import FastMCP

mcp = FastMCP("news")

@mcp.tool()
def latest_headlines(topic: str) -> str:
    return f"Latest headlines about {topic}: India economy grows 7.8%, monsoon hits early, election results dominate."

if __name__ == "__main__":
    mcp.run(transport="stdio")
