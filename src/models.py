import dspy
from typing import Literal

class ImageInput(dspy.Signature):
    image: dspy.Image = dspy.InputField()
    image_path: str = dspy.InputField()
    height: int = dspy.InputField(description="The height of the image")
    width: int = dspy.InputField(description="The width of the image")

class Audit(dspy.Signature):
    challenge_context: str = dspy.InputField(description="The context of the challenge")
    question: str = dspy.InputField(description="The question to answer")
    control: str = dspy.InputField(description="The control to audit")
    testing_policy: str = dspy.InputField(description="The testing policy to audit")
    screenshots: list[ImageInput] = dspy.InputField(description="The screenshots to audit")
    conclusion: Literal['SUCCESS', 'FAIL', 'FURTHER_EVIDENCE_REQUIRED'] = dspy.OutputField(description="The conclusion of the audit")
    reasoning: str = dspy.OutputField(description="The reasoning of conclusion of the audit. Please include the evidence that was used to form the conclusion in the form of image paths.")
