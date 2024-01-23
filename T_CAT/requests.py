import openai
from openai import OpenAI
from config.settings import OPENAI_API_KEY, OPENAI_MODEL
from T_CAT.utils import create_message
import T_CAT.consts as consts

class OpenAIRequest:

    def __init__(self, request):
            self.input_message = request["input_message"]
            self.add_message = request["add_message"]

    def get_output_message(self):
        "contentを組み立て、リクエストを送る。結果を返す"
        content = create_message(self.input_message, self.add_message)
        output_message = self.call_api(content)
        return output_message

    def call_api(self, content):
        """
        request
        """
        client = OpenAI(
            api_key = OPENAI_API_KEY,
        )

        try:

            chat_completion = client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[{"role": "user", "content": content}],    # TODO: contentが配列の場合
                max_tokens=consts.MAX_TOKENS,
                # stream=True,  # これをTrueにすると、流れるようにメッセージが表示できる。
            )
            """ stream=True,
            for chunk in chat_completion:
                if chunk.choices[0].delta.content is not None:
                    print(chunk.choices[0].delta.content)
            """
            response = chat_completion.choices[0].message.content
            return response
        

        except openai.APIConnectionError as e:
            return "The server could not be reached. %s", e.__cause__

        except openai.RateLimitError as e:
            return "A 429 status code was received; we should back off a bit. %s", e.__cause__

        except openai.APIStatusError as e:
            return "Another non-200-range status code was received.status_code: %s, response: %s", e.status_code, e.response