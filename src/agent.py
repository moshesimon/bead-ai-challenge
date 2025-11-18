
from tools import crop_and_zoom
from models import Audit
import dspy
import os
from dotenv import load_dotenv
load_dotenv()

dspy.configure(lm=dspy.LM('openai/gpt-5', api_key=os.getenv("OPENAI_API_KEY")))
audit_agent = dspy.ReAct(signature=Audit, tools=[crop_and_zoom])