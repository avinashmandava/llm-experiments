# llm-graph-explore-cmd
commandline tool to enter one starting prompt to an LLM, and explore the topic by selecting from suggested successive follow-up prompts

# How it works

This is just a commandline version of something someone already built that I saw on twitter: https://twitter.com/hturan.

- User inputs one prompt
- llm-graph-explore-cmd calls OpenAI API and gets an initial response back
- llm-graph-explore-cmd, without more user input, sends back a static prompt asking for three follow-up questions based on the last response, and presents the list to the user in a numbered list.
- User enters the number of the follow-up they want to ask, and the loop repeats.
