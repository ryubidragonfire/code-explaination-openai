# tutorial-explain-python-code-with-gpt
This is a sample usage of OpenAI API applied to python code explanation.

## Repo Structure
`tutorial-explain-python-code-with-gpt`
- [notebooks](./notebooks/)
    - [explain_python_code.ipynb](./notebooks/explain_python_code.ipynb)
    - [extract_entities_from_code.ipynb](./notebooks/extract_entities_from_code.ipynb)
- [output](./output/)
    - [explain_python_code/](./output/explain_python_code/)
    - [extract_entities/](./output/extract_entities/)
- [src](./src/)
   - [explain_python_code.py](./src/explain_python_code.py)
    
## Explain Python Code

[explain_python_code.py](./src/explain_python_code.py) does the following:

1. It reads codes from the directory that contains a list of files. In this case, codes from [gpt-discord-bot](https://github.com/openai/gpt-discord-bot) is used as an example. 
2. It builds an input `prompt`, which is used to query the OpenAI API, by appending a `prompt_postfix` to the `code` read from those `.py` files. In this example, `prompt_postfix` is as follows:
```
###
Here's what the above code is doing:
1.
```
3. It configures the hyper-parameters for the OpenAI API.
4. It makes a request to the OpenAI API with the input `prompt` and hyper-parameters.
5. It formats the response from the API.
6. It writes the formatted response to a file in the `./output/explain_python_code/` directory.

*Note: the "Explain Python Code" section is written with assistence from OpenAI GPT.*

## Output 
The file [explain_python_code/main.py.output](./output/explain_python_code/main.py.output) contains reponse from OpenAI, that attempts to explain the code in https://github.com/openai/gpt-discord-bot/blob/main/src/main.py

---

*Warning: this repo is for educational purpose only.*