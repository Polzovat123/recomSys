import openai


class LLMbot:
    def make(self, messages, max_tokens=60):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=max_tokens
        )

        assistant_reply = response['choices'][0]['message']['content']

        return assistant_reply