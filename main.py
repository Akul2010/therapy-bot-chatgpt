import openai # The main lib for accessing ChatGPT
import tiktoken # For counting tokens per prompt

openai.api_key = "YOUR API KEY"
user_role = input("Give me a custom role (recommended to leave blank): ")
prompt = input("Ask me anything: ")

result = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": user_role},
        {"role": "user", "content": prompt}
    ],
)

num_tokens_from_messages(messages)

if user_role == '':
    user_role == "You are a therapist helping a student who can't speak to someone."

def num_tokens_from_messages(messages):
    """
    Returns the number of tokens used by a list of messages.
    Code from: https://github.com/openai/openai-cookbook
    """
    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")
    num_tokens = 0
    for message in messages:
        num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":  # if there's a name, the role is omitted
                num_tokens += -1  # role is always required and always 1 token
    num_tokens += 2  # every reply is primed with <im_start>assistant
    return num_tokens

