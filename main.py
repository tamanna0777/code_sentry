import os

from google import genai
from google.genai import types

from tools import scan_vulnerabilities
from prompts import SYSTEM_PROMPT


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


query = input("Question: ")

print("\nPaste code snippet (type END on a new line to finish):")

lines = []

while True:
    line = input()

    if line == "END":
        break

    lines.append(line)

code = "\n".join(lines)

message = f"""
User Question:
{query}

Code Snippet:
{code}
"""


try:
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=message,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=[scan_vulnerabilities]
        )
    )

    print("\n===== SECURITY REVIEW =====\n")
    print(response.text)

except Exception as e:
    print("\nError occurred:")
    print(str(e))

except Exception as e:
    print("\nError occurred:")
    print(str(e))
    print("\nIf this is a 503 error, the Gemini service is temporarily overloaded.")