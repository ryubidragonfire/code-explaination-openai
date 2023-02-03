import openai

def prompt_api(engine, prompt, temperature, max_tokens, top_p, frequency_penalty, presence_penalty, best_of, stop):
  response = openai.Completion.create(
    engine=engine,
    prompt=prompt,
    temperature=temperature,
    max_tokens=max_tokens,
    top_p=top_p,
    frequency_penalty=frequency_penalty, 
    presence_penalty=presence_penalty,
    best_of=best_of,
    stop=stop)
  return(response)

def get_response(response):
  response_text = response['choices'][0]['text']
  return response_text

def format_output(prompt_postfix, response):
    output = prompt_postfix + get_response(response)
    return output
