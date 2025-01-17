import os

from hide import model
from hide_overrides.hide_client import HideClient

OPENAI_API_KEY = ""
HIDE_BASE_URL = "http://localhost:8080"
PROJECT_GIT_URL = "https://github.com/hide-org/math-api.git"

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

hc = HideClient(base_url=HIDE_BASE_URL)
project = hc.create_project(
    repository=model.Repository(url=PROJECT_GIT_URL),
)

print (f"Project ID: {project.id}")

file = hc.get_file(
    project_id=project.id,
    path="my_tiny_service/api/routers/maths.py"
)

print(file)

# toolkit = Toolkit(project=project, client=hc)
# lc_toolkit = toolkit.as_langchain()
# repository = Repository(url=PROJECT_GIT_URL)
# print(repository)
# project = hc.get_project(repository=repository)

# print(f"Project ID: {project.id}")

# toolkit = Toolkit(project=project.id, client=hc)
# tools = toolkit.get_tools()

# for tool in tools:
#     print("Name:", tool.name)
#     print("Description:", tool.description)
#     print("Args:", tool.args)
#     print("")

# llm = ChatOpenAI(model="gpt-4o")
# prompt = hub.pull("hwchase17/openai-tools-agent")
# agent = create_tool_calling_agent(llm, tools, prompt)
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# response = agent_executor.invoke({"input": "Run the tests for the math service"})
# print("")
# print(response["output"])
