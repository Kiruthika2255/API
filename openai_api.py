import openai

openai.api_key='API key'

response=openai.Completion.complete(
    engine='Davinci',
    prompt='write a poem about love',
    max_depth=100,
    temperature=0.8# to specifies the randomness of the generated text.
    
    )

if response['choise'][0]['status']=='completed':
    generated_text=response['choices'][0]['text'].strip()
    print(generated_text)
else:
    print('api request fails',response['error'])