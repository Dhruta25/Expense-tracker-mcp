from fastapi import FastAPI
from fastmcp.fastapi import MCPRouter # type: ignore
from test import mcp   # <-- your MCP server object

app = FastAPI(title="Expense Tracker API")

# Convert MCP tools → FastAPI routes
router = MCPRouter(mcp)
app.include_router(router)

# Run using uvicorn
# uvicorn fastapi_server:app --reload