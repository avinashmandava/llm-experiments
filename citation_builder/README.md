# Citation Builder

Simple script that takes a word document, extracts all the footnotes, and generates bibliographic citations.

# Instructions

## Set up .env file
- Create a `.env` fil in this directory (`citation_builder`)
- Add the following to the `.env` file and replace the placeholder values with your data:
`OPENAI_API_KEY="you_api_key"`
`DATA_DIR="data"`

## Add files
- Create a `data/` directory in this directory (`citation_builder`)
- Add your word files to the `data/` directory you just created.

## Run the program

Run the file, replacing `word_filename` with the name of the file you want to extract footnotes and create a bibliography for.
`python main.py word_filename`

Your list of citations will print to the terminal output.

