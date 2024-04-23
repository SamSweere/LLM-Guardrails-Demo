from pathlib import Path

from nemoguardrails import LLMRails, RailsConfig

from llm_guardrails_demo.logger import logger
from llm_guardrails_demo.utils import get_nemo_llm_calls_summary

config = RailsConfig.from_path(str(Path(__file__).parent / "config"))
rails = LLMRails(config)


def get_chatbot_response(messages):
    response = rails.generate(messages=messages)

    logger.debug(get_nemo_llm_calls_summary(rails))
    # info.print_llm_calls_summary()
    return response


if __name__ == "__main__":
    messages = [{"role": "user", "content": "Hello! What can you do for me?"}]
    response = get_chatbot_response(messages)

    print(response["content"])
