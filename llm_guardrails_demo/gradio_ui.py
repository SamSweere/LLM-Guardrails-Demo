import gradio as gr

from llm_guardrails_demo.llm_motors_chatbot import (
    get_chatbot_response,
)


def predict(message, history):
    history_openai_format = []
    for human, assistant in history:
        if human is not None:
            history_openai_format.append({"role": "user", "content": human})
        if assistant is not None:
            history_openai_format.append({"role": "assistant", "content": assistant})
    history_openai_format.append({"role": "user", "content": message})

    response = get_chatbot_response(messages=history_openai_format)

    return response["content"]


welcome_message = (
    "Welcome 👋. I'm Yann LeCruise, your virtual assistant. "
    + "I'm here to answer any questions you may have about LLMotors. How could I assist you today?"
)

chatbot = gr.Chatbot(value=[(None, welcome_message)], height=700)
gr.ChatInterface(fn=predict, title="LLM Guardrails Demo", chatbot=chatbot).launch()
