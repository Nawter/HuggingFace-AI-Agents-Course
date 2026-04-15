from mcp.server.fastmcp import FastMCP

mcp = FastMCP("TestServer")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.tool()
def greet(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}! Welcome to the MCP world."

if __name__ == "__main__":
    mcp.run(transport="sse")