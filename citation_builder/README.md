# Citation Builder

Simple script that takes a word document, extracts all the footnotes, and generates bibliographic citations following Chicago Manual of Style format.

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

Your list of citations will be saved in a file called `data/citations.txt`

# Limitations

This doesnt always work. The amount of context in a real dissertation with a lot of footnotes is huge. Also, the best we can do is instruct GPT to format in chicago manual of style format. It doesnt always get it right. When we see errors in response formats we do a retry which often fixes things. But the script could break if the data comes back misformatted (e.g. it's not JSON) twice in a row, despite the formatting prompt.

It also cant remember a lot of context. Even just the extracted citations is too much context to feed back into the model. So you may end up with situations where you reference a paper in a footnote in one area early in the text, and then you do a shorthand reference later on. And the shorthand reference will get picked up, for example:

"McCormick, Origins, p. 102"

when the real citation is:

Michael McCormick, The Origins of the European Economy (Cambridge: Cambridge University Press, 2001).

There are ways to improve this, for example storing each citation as memory, and doing a similarity search every time a new citation is extracted by the LLM to determine if the new citation should be discarded as a duplicate. This is an area of exploration for future efforts, but it's probably easier for the individual to just go into the output file and delete the duplicates they find.



