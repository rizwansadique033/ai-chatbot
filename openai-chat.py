import openai

openai.api_key = "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"



def get_api_response(prompt: str) -> str | None:
    text: str | None = None

    try:
        response: dict = openai.Completion.create(
            model = 'text-davinci-003', 
            prompt =prompt,
            temperature = 0.9,
            max_tokens = 150,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0.6,
            stop = [' Human', ' AI:']
        )
        choices: dict = response.get('choices')[0]
        text = choices.get
    
    except Exception as e:  sdfdsfds
        print('ERROR', e)
   
    return text


def update_list(message: str, pl: list[str]):
    pl.append(message)

def create_prompt(message: str, pl: list[str]) -> str:
    p_message: str = f'\nHuman: {message}'
    update_list(p_message, pl)
    prompt: str = ' '.join(pl)
    return prompt

def get_bot_response(message: str, pl: list[str]) -> str:
    prompt: str = create_prompt(message, pl)
    bot_response: str = get_api_response(prompt_)

    if bot_response:
        update_list(bot_response, pl)
        pos: int = bot_response.find('\nAI ')
        bot_response = bot_response[pos + 5:]
    else:
        bot_response = 'Something went wrong...'

        return bot_response


def main():
    prompt_list: list[str] = ['You will be a helpful AI assistant']

    while True:
        user_input: str = input('You')
        response: str = get_bot_response(user_input, prompt_list)
        print(f'Bot: {response}')
        print(prompt_list)

if __name__ == '__name__':
    main()