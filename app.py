import os
from openai import OpenAI

MODEL = os.getenv("OPENAI_MODEL", "gpt-5")

def main():
    print("\n=== AI Study Assistant ===")
    print("1. Explain a topic")
    print("2. Summarize notes")
    print("3. Generate quiz questions")
    print("4. Make a study plan")
    choice = input("\nChoose an option (1-4): ").strip()

    tasks = {
        "1": "Explain the topic step-by-step with a simple example.",
        "2": "Summarize the provided notes into concise exam-ready points.",
        "3": "Create 5 multiple-choice questions with answers and short explanations.",
        "4": "Create a practical study plan with daily tasks based on the topic."
    }
    if choice not in tasks:
        print("Invalid choice.")
        return

    text = input("\nEnter your topic/notes: ").strip()
    if not text:
        print("Please enter some text.")
        return

    key = os.getenv("OPENAI_API_KEY")
    if not key:
        print("Error: set OPENAI_API_KEY before running the program.")
        return

    client = OpenAI(api_key=key)
    prompt = f"""You are an AI Study Assistant for college students.
Task: {tasks[choice]}
User input:
{text}

Give a clear, accurate and student-friendly answer. Use headings and bullet points where useful."""
    response = client.responses.create(model=MODEL, input=prompt)
    print("\n--- AI Response ---\n")
    print(response.output_text)

if __name__ == "__main__":
    main()
