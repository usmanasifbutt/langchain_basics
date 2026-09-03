from langchain.tools import tool, ToolRuntime

from schemas.weather import UserContext

@tool("get_location", description="Get location of the user from context")
def get_location(runtime: ToolRuntime[UserContext]):
    return runtime.context.location