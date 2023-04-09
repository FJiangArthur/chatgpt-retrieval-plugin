import logging
import openai
from chat_utils import ask
OPENAI_API_KEY = "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"
DATABASE_INTERFACE_BEARER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxODQxOTYiLCJuYW1lIjoiQXJ0IEppYW5nIiwiaWF0IjoxNTE2MjM5MDIyfQ.0fWdbCeNyrKRcJWwGrs1mdgVhlU1iVNVJ0JMWnhQmdI"

if __name__ == "__main__":
    while True:
        user_query = input("Enter your question: ")
        openai.api_key = OPENAI_API_KEY
        logging.basicConfig(level=logging.WARNING,
                            format="%(asctime)s %(levelname)s %(message)s")
        print(ask(user_query))
