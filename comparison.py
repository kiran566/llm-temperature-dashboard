from llm import generate_response
from evaluator import (
    calculate_latency,
    word_count
)

import time


def compare_prompts(
    prompt_a,
    prompt_b,
    temperature,
    top_p,
    max_tokens
):

    results=[]

    for name,prompt in [

        ("Prompt A",prompt_a),

        ("Prompt B",prompt_b)

    ]:

        start=time.time()

        response=generate_response(

            prompt,

            temperature,

            top_p,

            max_tokens

        )

        end=time.time()

        results.append({

            "Prompt":name,

            "Latency":calculate_latency(start,end),

            "Tokens":response["usage"].total_tokens,

            "Word Count":word_count(

                response["text"]

            ),

            "Response":response["text"]

        })

    return results