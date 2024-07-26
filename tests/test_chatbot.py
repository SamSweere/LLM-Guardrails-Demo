from llm_guardrails_demo.llm_motors_chatbot import get_chatbot_response


def test_chatbot_resonse():
    messages = [{"role": "user", "content": "Hello! What can you do for me?"}]
    response = get_chatbot_response(messages)

    assert len(response["content"]) > 0
