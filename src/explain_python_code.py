import os
import os
import openai
from dotenv import load_dotenv
from utils import prompt_api, get_response, format_output

# Set up Azure OpenAI
load_dotenv()
openai.api_type = "azure"
openai.api_base = "https://tutorial-openai-01-2023.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")

# create prompt
prompt_postfix = """ 
###
Here's what the above code is doing:
1.
"""

# set file directory
file_dir = '../gpt-discord-bot/src/'

# get list of files
file_list = os.listdir(file_dir)

for fn in file_list:
    # read from file
    fname = os.path.join(file_dir, fn); print(fname)
    f = open(fname, "r")
    code = f.read()

    # build input
    prompt = code +  prompt_postfix

    # Configure hyper-parameters
    engine="text-davinci-003"  # note that text-davinci-x responds better than code-davinci-x
    prompt=prompt
    temperature=0 # [0, 1]
    max_tokens=300
    top_p=1
    frequency_penalty=0 # [0, 2]
    presence_penalty=0 # [0, 2]
    best_of=1
    stop=["###"]

    # make a request to api
    response = prompt_api(engine, prompt, temperature, max_tokens, top_p, frequency_penalty, presence_penalty, best_of, stop)

    # format output
    output = format_output(prompt_postfix, response)

    # write output to file
    output_file_dir = "./output/explain_python_code/"
    fname_out = os.path.join(output_file_dir, fn + '.output'); print(fname_out)
    output_file = open(fname_out, "w")
    output_file.write(output)
    output_file.close()