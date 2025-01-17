import os

import requests
import hide
# from hide.client.hide_client import HideClient
# from langchain import hub
# from langchain.agents import AgentExecutor, create_tool_calling_agent
# from langchain_openai import ChatOpenAI
# from langchain import hub
# from langchain.agents import AgentExecutor, create_tool_calling_agent
# from langchain_openai import ChatOpenAI
# from hide.toolkit import Toolkit
from hide.toolkit import Toolkit
from typing import Optional
from hide import model
from hide.devcontainer.model import DevContainer
from hide.client.hide_client import HideClientError

def create_project(
        self,
        repository: model.Repository,
        devcontainer: Optional[DevContainer] = None,
        languages: Optional[list[model.Language]] = None,
    ) -> model.Project:
        request = model.CreateProjectRequest(
            repository=repository, devcontainer=devcontainer, languages=languages
        )
        print("request", request)
        response = requests.post(
            f"{self.base_url}/projects",
            json=request.model_dump(exclude_unset=True, exclude_none=True),
        )
        print("response", response)
        if not response.ok:
            raise HideClientError(response.text)
        
        # Ensure the response includes the repository
        response_data = response.json()
        if 'repository' not in response_data:
            response_data['repository'] = repository  # Add the repository to the response

        print("validate response", response_data)
        return model.Project.model_validate(response_data)


OPENAI_API_KEY = ""
HIDE_BASE_URL = "http://localhost:8080"
PROJECT_GIT_URL = "https://github.com/hide-org/math-api.git"

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

hc = hide.Client(base_url=HIDE_BASE_URL)
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
