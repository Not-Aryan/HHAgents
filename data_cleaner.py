import autogen

config_list_gpt4 = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt-3.5-turbo"],
    },
)

config_list = [
    {
        'model': 'gpt-3.5-turbo',
        'api_key': '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',
    }
]

gpt4_config = {
    "seed": 42,  # change the seed for different trials
    "temperature": 0,
    "config_list": config_list_gpt4,
    "request_timeout": 120,
}

user_proxy = autogen.UserProxyAgent(
   name="Admin",
   system_message="A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin.",
   code_execution_config=False,
)

engineer = autogen.AssistantAgent(
    name="Engineer",
    llm_config=gpt4_config,
    system_message='''Engineer. 
    You follow an approved plan. 
    You write python/shell code to solve tasks. 
    Wrap the code in a code block that specifies the script type. The user can't modify your code. 
    So do not suggest incomplete code which requires others to modify. Don't use a code block if it's not intended to be executed by the executor.
    Don't include multiple code blocks in one response. 
    Do not ask others to copy and paste the result. Check the execution result returned by the executor.
    If the result indicates there is an error, fix the error and output the code again. Suggest the full code instead of partial code or code changes. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try.
    ''',
)

scientist = autogen.AssistantAgent(
    name="Scientist",
    llm_config=gpt4_config,
    system_message="""Data Scientist. You follow an approved plan. 
    You are knowledgeable on what makes a good dataset, and what steps need to be taken to improve a dataset for machine learning tasks. 
    Your goal is to analyze and suggest changes for how the Engineer can write code to clean data to prepare it for machine learning analysis.
    You don't write code."""
)

planner = autogen.AssistantAgent(
    name="Planner",
    system_message='''Planner. Suggest a plan. 
    Give the data from the input to the Data Scientist.
    Revise the plan based on feedback from admin and critic, until admin approval.
    The plan may involve an engineer who can write code and a scientist who doesn't write code.
    Explain the plan first. Be clear which step is performed by an engineer, and which step is performed by a scientist.
    ''',
    llm_config=gpt4_config,
)

executor = autogen.UserProxyAgent(
    name="Executor",
    system_message="Executor. Execute the code written by the engineer and report the result.",
    human_input_mode="NEVER",
    code_execution_config={"last_n_messages": 3, "work_dir": "paper"},
)

critic = autogen.AssistantAgent(
    name="Critic",
    system_message="Critic. Double check plan, claims, code from other agents and provide feedback. Check whether the plan includes adding verifiable info such as source URL.",
    llm_config=gpt4_config,
)
groupchat = autogen.GroupChat(agents=[user_proxy, engineer, scientist, planner, executor, critic], messages=[], max_round=50)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=gpt4_config)

user_proxy.initiate_chat(
    manager,
    message="""
    Analyze the data at this url: https://raw.githubusercontent.com/Medlytics2023/Week1/master/Datasets/allhypo.train.data
    Your task is to identify problems/issues in the data and write code to clean the data.
    Then after you have cleaned the data, you should save the cleaned data in a csv file.
    """,
)



#research area, identify important trends
#analyzed database
#figure out how to clean data

#-----
#figure out models
#fit model to data
#write model
#make sure model works
#produce model results and save to GCP container