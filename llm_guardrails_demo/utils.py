from nemoguardrails import LLMRails


def get_nemo_llm_calls_summary(rails: LLMRails) -> str:
    """Helper to print a quick overview of the LLM calls that were made."""

    info = rails.explain()
    llm_calls = info.llm_calls

    if len(llm_calls) == 0:
        return "No LLM calls were made."

    else:
        total_duration = 0
        total_tokens = 0
        for llm_call in llm_calls:
            total_duration += llm_call.duration or 0
            total_tokens += llm_call.total_tokens or 0

        msg = ""

        msg += f"Summary: {len(llm_calls)} LLM call(s) took {total_duration:.2f} seconds " + (
            f"and used {total_tokens} tokens.\n" if total_tokens else ".\n"
        )

        for i in range(len(llm_calls)):
            llm_call = llm_calls[i]
            msg += f"{i+1}. Task `{llm_call.task}` took {llm_call.duration:.2f} seconds " + (
                f"and used {llm_call.total_tokens} tokens." if total_tokens else "."
            )

            msg += "\n"

        return msg
