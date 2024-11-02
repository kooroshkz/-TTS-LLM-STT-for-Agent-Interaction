import openai

openai.api_key = 'your_openai_api_key_here'

def get_openai_response(user_input):
    """
    Get a response from OpenAI's API based on user input.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message['content'].strip()
