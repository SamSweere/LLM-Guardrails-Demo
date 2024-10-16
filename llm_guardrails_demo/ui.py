import gradio as gr

from llm_guardrails_demo.llm_motors_chatbot import (
    get_chatbot_response,
)


def predict(message, history):
    """
    This function is used by Gradio to get the response from the chatbot.

    Args:
        message: The message from the user.
        history: The conversation history.

    Returns:
        The response from the chatbot.
    """

    history_openai_format = []
    for human, assistant in history:
        if human is not None:
            history_openai_format.append({"role": "user", "content": human})
        if assistant is not None:
            history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = get_chatbot_response(messages=history_openai_format)

    return response["content"]


chatbot = gr.Chatbot(value=[], height=700)
gr.ChatInterface(
    fn=predict,
    title="LLM Guardrails Demo",
    chatbot=chatbot,
    retry_btn=None,
    undo_btn=None,
    clear_btn=None,
).launch()
