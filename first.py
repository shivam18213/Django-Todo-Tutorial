import os
import openai
openai.organization = "org-LHRXlsWHTCRnjRhZaxVEXx8M"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Engine.list()