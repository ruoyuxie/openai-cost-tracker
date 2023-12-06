## Installation
```pip install openai-cost-tracker```

## Usage

Use the ```query_openai``` function as a drop-in replacement for openAI's completion functions, such as ```openai.Completion.create()```. The ```query_openai``` will return the same response as the original function, but will also print the cost of the request. 

Turn on ```simulation``` to test the cost of a request without actually sending it to OpenAI. Turn on ```print_cost``` to print the cost of each request.

```import openai 
from openai_cost_tracker import query_openai

openai.api_key = <YOUR_OPENAI_API_KEY>

message = [
    {'role': 'user', 'content': "Ned had 15 video games but 6 of them weren't working. If he wanted to sell the working games for $7 each, how much money could he earn?"}
    ]

response = query_openai(
    model="gpt-4-1106-preview",  # gpt-4-1106-preview,  gpt-3.5-turbo-1106,  gpt-4
    messages=message, 
    max_tokens=5,
    simulation=True,
    print_cost=True 
)     

print(response["choices"][0]["message"]["content"])
```

## Output
```
Input tokens: 43 | Output tokens: 5 | Cost: $0.0006 | Total: $0.0006
Ned started with
```
## Notes
- The cost of the request is calculated based on the number of tokens in the input and output using the OpenAI tokenization scheme. This is an approximation of the actual cost.