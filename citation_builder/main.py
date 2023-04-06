from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser, OutputFixingParser
from langchain.document_loaders import UnstructuredWordDocumentLoader
from pydantic import BaseModel, Field, validator
from typing import List
from dotenv import load_dotenv
import json
import os
import validators
import docx
from lxml import etree

# CONFIG
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DATA_DIR = os.getenv('DATA_DIR')
system_message = "You are a helpful research assistant. Your job is to take a list of footnotes from research papers and create a bibtex-style list of citations for all sources in the list of footnotes."
chat = ChatOpenAI(model_name="gpt-3.5-turbo")

class Citations(BaseModel):
    citations: List[str] = Field(description="Python list of all bibtex-formatted citations extracted from the supplied list of footnotes")

def extract_footnotes(doc_path):
    footnotes = []
    doc = docx.Document(doc_path)

    for part in doc.part.related_parts.values():
        if part.content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.footnotes+xml':
            footnotes_xml = part.blob
            root = etree.fromstring(footnotes_xml)
            namespace = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
            footnote_elems = root.findall('.//w:footnote', namespace)

            for footnote_elem in footnote_elems:
                footnote_text = ''
                for elem in footnote_elem.iter():
                    if elem.tag.endswith('}t'):
                        if elem.text:
                            footnote_text += elem.text
                if footnote_text:
                    footnotes.append(footnote_text)
    return footnotes

def get_citations(footnotes: List):
  # Your code goes here

  parser = PydanticOutputParser(pydantic_object=Citations)

  prompt = PromptTemplate(
    template = "Take the folllowing list of footnotes, extract all the source info, and construct a list of bibliographic citations. Do it the same way bibtex would do it. And present the citations to me in a python list:\n{footnotes}\n{format_instructions}",
    input_variables = ["footnotes"],
    partial_variables = {"format_instructions": parser.get_format_instructions()}
  )
  input = prompt.format_prompt(footnotes=footnotes)
  messages = [
    SystemMessage(content=system_message),
    HumanMessage(content=input.to_string())
  ]
  output = chat(messages).content
  print(output)
  try:
    parser.parse(output)
    output = json.loads(output)
  except:
    new_parser = OutputFixingParser.from_llm(parser=parser, llm=chat)
    new_parser.parse(output)
    output = json.loads(output)
  return output

def main():
  file_path = f"{DATA_DIR}/Conclusion2.0.docx"
  footnotes = extract_footnotes(file_path)
  footnotes = footnotes[:5]
  citations = get_citations(footnotes)

if __name__ == "__main__":
    main()
