import gradio as gr

from llm_guardrails_demo.llm_motors_chatbot import (
    get_chatbot_response,
)


def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        history_openai_format.append({"role": "user", "content": human})
        history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = get_chatbot_response(messages=history_openai_format)

    return response["content"]


gr.ChatInterface(predict).launch()
