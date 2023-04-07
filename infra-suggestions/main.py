# Import necessary modules
import argparse

# Define command line arguments
parser = argparse.ArgumentParser(description='Get help optimizing your infrastructure systems. Fill out the .env file with keys for integrations and OpenAI to run the script.')
parser.add_argument('--technology', type=str, required=True, help='The technology to use. Currently only PostgreSQL is supported as a value.')
parser.add_argument('--goal', type=str, required=True, help='The goal to achieve, e.g. "reduce latency".')

def process_request(technology, goal):
  import openai
  import langchain
  import os
  import json
  from dotenv import load_dotenv

  from data_processing import format_metrics
  from external_apis import datadog
  from llm_integration import prompt_generator

  load_dotenv()
  OPENAI_API_KEY = os.getenv('OPENAI_KEY')

  # Config
  metric_data = json.dumps(format_metrics.get_formatted_metrics(technology))

  # Basic use case - calling LLM on some input
  from langchain.llms import OpenAI
  llm = OpenAI(model_name="text-davinci-003", temperature=1, max_tokens=1000)
  prompt = prompt_generator.construct_prompt(technology, goal, metric_data)
  response = llm(prompt)
  return response

# Define main function
def main(args):
    # Call the process_request function with the provided arguments
    response = process_request(args.technology, args.goal)
    # Print the response
    print(response)

# Parse command line arguments and run main function
if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
