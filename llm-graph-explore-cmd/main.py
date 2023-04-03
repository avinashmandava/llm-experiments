# Typer app for asking an LLM one question and then exploring the tree of suggested follow-up questions
import typer
import openai
import json
from dotenv import load_dotenv
import os
from rich import print

# CONFIG
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')
max_tokens = 400

#DB
last_assistant_response = ""
system_prompt = "You are a helpful assistant."
static_prompt = '''
    Come up with three follow-up questions to your last response.
    In your next response, print only the follow-up questions, do not include the answers.
    Structure the response as a list of JSON objects, with no other content in the response other than the list.
    '''

# Get a response from the llm given a prompt
def get_llm_response(prompt: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=max_tokens,
        messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
    )
    return response["choices"][0]["message"]["content"]

# Generate a list of questions based on the last prompt
def generate_questions(last_assistant_response: str, static_prompt: str):
    questions = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=max_tokens,
        messages=[
                {"role": "system", "content": system_prompt},
                {"role": "assistant", "content": last_assistant_response},
                {"role": "user", "content": static_prompt}
            ]
    )
    return questions["choices"][0]["message"]["content"]

# main function that loops through the logic of asking a question and then exploring the tree of suggested follow-up questions.
def main(prompt: str = typer.Option(..., prompt=True)):
    print(f"[blue][bold]Starting Question:[/bold] {prompt}[/blue]")
    while True:
        response = get_llm_response(prompt)
        last_assistant_response = response
        print(f"[green][bold]GPT Response:[/bold] {response}[/green]")
        question_list = generate_questions(last_assistant_response, static_prompt)
        questions = json.loads(question_list)
        print(f"[yellow][bold]Here are some follow-up questions[/bold]:[/yellow]")
        for x in range(0,len(questions)):
            print(f"[yellow][bold]{x+1}.[/bold] {questions[x]['question']}[/yellow]")
        selection = typer.prompt("Enter the number of the follow-up question you want to ask")
        selection = int(selection.strip(" ").strip("."))
        prompt = questions[selection-1]["question"]
        print(f"[blue][bold]New Question:[/bold] {prompt}[/blue]")

if __name__ == "__main__":
    typer.run(main)
