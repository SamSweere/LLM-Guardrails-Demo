from nemoguardrails.actions import action


@action(is_system_action=True)
async def check_blocked_terms(context: dict | None = None):
    bot_response = context.get("bot_message")

    # A quick hard-coded list of proprietary terms. You can also read this from a file.
    proprietary_terms = ["tesla", "rivian", "cheverolet"]  # Etc

    return any(term in bot_response.lower() for term in proprietary_terms)
