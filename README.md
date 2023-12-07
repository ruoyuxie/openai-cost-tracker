# OpenAI Cost Tracker
A simple light weight wrapper for OpenAI's API that tracks the cost of each request. It also provides simulation mode to test the cost of a request without actually sending it to OpenAI. 


## Installation
```python
pip install openai-cost-tracker
```


## Usage
Import the ```query_openai``` function from ```openai_cost_tracker```:
    
```python
from openai_cost_tracker import query_openai
```


Use ```query_openai``` function as a drop-in replacement for openAI's completion function, such as ```openai.Completion.create()```. The ```query_openai``` will return the same response as the original function, but will also print the cost of the request. 

Turn on ```simulation``` to test the cost of a request without actually sending it to OpenAI. Turn on ```print_cost``` to print the cost of each request.

```python
import openai 
from openai_cost_tracker import query_openai

openai.api_key = "<YOUR_OPENAI_API_KEY_HERE>"

prompt = "Hello World!"  # your prompt here

response = query_openai(
    model="gpt-4-1106-preview",  # support gpt-4-1106-preview,  gpt-3.5-turbo-1106,  gpt-4
    messages=[{'role': 'user', 'content': prompt}],            
    max_tokens=5,
    # rest of your OpenAI params here ...
    simulation=True,  # set to True to test the cost of a request without actually sending it to OpenAI 
    print_cost=True   # set to True to print the cost of each request
)     

print(response["choices"][0]["message"]["content"])
```


## Output
```
Input tokens: 10 | Output tokens: 5 | Cost: $0.0003 | Total: $0.0003
Hello! How can I
```


## Notes
- The cost of the request is calculated based on the number of tokens in the input and output using the OpenAI tokenization scheme. This is an approximation of the actual cost.
