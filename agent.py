import os

# ✅ Set Google Gemini API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAP8OvgIZ4t_J3pE33WInTxTsHpkvrtIU8"

# ✅ Import Gemini LLM
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
)

# ✅ Import Shell Tool to run Linux commands
from langchain_community.tools import ShellTool
shell_tool = ShellTool()

# ✅ Import Agent initializer
from langchain.agents import initialize_agent

# ✅ Create the Agent
myagent = initialize_agent(
    llm=llm,
    tools=[shell_tool],
    verbose=True
)

# ✅ Continuous Loop to Accept User Commands
while True:
    myprompt = input("Enter your requirement : ")

    input_message = {
        "role": "user",
        "content": (
            "You are a Linux administrator, and always give final output only "
            "and append it in output.log file in the current directory, "
            "for given prompt -- " + myprompt
        )
    }

    myagent.run({"input": input_message})
