from autogen import AssistantAgent, UserProxyAgent, config_list_from_json

config_list = config_list_from_json(env_or_file="OAI_CONFIG_LIST")

# llm_config = {"config_list": config_list, "seed": 42, "request_timeout": 120}

assistant = AssistantAgent(
        "assistant", 
        llm_config={"config_list": config_list}
)

user_proxy = UserProxyAgent("user_proxy", 
    code_execution_config={"work_dir": "coding"}
)

user_proxy.initiate_chat(assistant, message="")
