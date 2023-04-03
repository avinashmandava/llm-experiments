# llm-graph-explore-cmd
commandline tool to enter one starting prompt to an LLM, and explore the topic by selecting from suggested successive follow-up prompts

# Usage

From the `llm-graph-explore-cm/` directory, run `python main.py`

# How it works

This is just a commandline version of something someone already built that I saw on twitter: https://twitter.com/hturan.

- User inputs one prompt
- llm-graph-explore-cmd calls OpenAI API and gets an initial response back
- llm-graph-explore-cmd, without more user input, sends back a static prompt asking for three follow-up questions based on the last response, and presents the list to the user in a numbered list.
- User enters the number of the follow-up they want to ask, and the loop repeats.

# Current limitations

- Still figuring out how to correctly prompt GPT to return the list of follow-up questions with the right structure every time, haven't decided the best way to deal with that variance (few shot prompt with chat completeion, instructGPT, etc all options).
- Can't go "back"
- Only stores the context of the last GPT response, could be better if it stores a longer context to avoid repeating questions, content.
- UX improvements around colors, etc.
