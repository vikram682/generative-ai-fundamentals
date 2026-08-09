# AI Study Assistant using Generative AI

This project is for the Edquest assignment **Exploring Generative AI and AI Fundamentals**.

## Features
- Explain a topic
- Summarize notes
- Generate quiz questions
- Create a study plan

## Technology
Python + OpenAI Python SDK + OpenAI Responses API.

## Setup
1. Install Python 3.10+.
2. Run `pip install -r requirements.txt`.
3. Set your API key as an environment variable. Never put the key in the code or GitHub.
4. Run `python app.py`.

Windows PowerShell:
`$env:OPENAI_API_KEY="your_api_key_here"`

macOS/Linux:
`export OPENAI_API_KEY="your_api_key_here"`

Optional:
`export OPENAI_MODEL="gpt-5"`

## Example
Choose `1` and enter `Explain the OSI model`.
The application sends the instruction to the GPT model and prints a student-friendly explanation.

## Learning outcomes
Generative AI, prompt engineering, Python programming, API integration, basic evaluation and secure API-key handling.
