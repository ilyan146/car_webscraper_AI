import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

# get API url and key from .env
api_url = os.getenv("API_URL")
api_key = os.getenv("API_KEY")


def simple_gpt_bot():
    # Create client
    client = AzureOpenAI(
        azure_endpoint=api_url, api_key=api_key, api_version="2024-05-01-preview"
    )
    while True:
        user_input = input("you: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            print("Exiting...")
            break

        # Generate a response using LLM
        response = client.chat.completions.create(
            model="gpt-4o-mini", messages=[{"role": "system", "content": user_input}]
        )

        chatbot_reply = response.choices[0].message.content
        # print reply
        print(f"Chatbot: {chatbot_reply}")


if __name__ == "__main__":
    simple_gpt_bot()
    print("Chatbot exited.")
