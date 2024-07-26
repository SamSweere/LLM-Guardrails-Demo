from pathlib import Path

from nemoguardrails import LLMRails, RailsConfig

from llm_guardrails_demo.logger import logger
from llm_guardrails_demo.utils import get_nemo_llm_calls_summary

config = RailsConfig.from_path(str(Path(__file__).parent / "config"))
rails = LLMRails(config)


def get_chatbot_response(messages):
    logger.info(f"Received messages: {messages}")
    response = rails.generate(messages=messages)

    logger.info(f"Response: {response}")
    logger.debug(get_nemo_llm_calls_summary(rails))
    info = rails.explain()
    for call in info.llm_calls:
        logger.debug(f"LLM Call: {call}")

    return response


def get_welcome_message():
    welcome_message = (
        "Welcome 👋. I'm Yann LeCruise, your virtual assistant. "
        + "I'm here to answer any questions you may have about LLMotors. How could I assist you today?"
    )

    return welcome_message


if __name__ == "__main__":
    conversation_history = []

    # Include the welcome message at the start of the conversation
    welcome_message = get_welcome_message()
    print(f"Assistant: {welcome_message}")
    conversation_history.append({"role": "assistant", "content": welcome_message})

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Goodbye!")
            break

        conversation_history.append({"role": "user", "content": user_input})
        response = get_chatbot_response(conversation_history)
        conversation_history.append({"role": "assistant", "content": response["content"]})

        print(f"Assistant: {response['content']}")
