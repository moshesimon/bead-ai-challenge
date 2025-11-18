import os
from tools import get_ImageInput

def get_callenge_data(sample: int):
    challenge_context = """
    ## Background

    Many tasks in the world of auditing require verifying that a specific policy or procedure has been followed. 
    To assess this, the auditor selects a random sample and collects evidence to verify whether the requirements are met for each.

    ## The Task

    We have taken one particular example of this: a control that ensures systems can't be changed unless a set of prerequisites is true. 
    You are provided with the control description, control attributes, and a few evidence samples, in this case, screenshots of GitHub pull requests showing the changes made.

    ## Expected Output

    * For each sample and control attribute provide a response that includeds the assements and contexual details of how the conclussion was formed. Inlcude evidence by referring to the relevant image paths that back up your points.
    * The assessment can be SUCCESS, FAIL, FURTHER_EVIDENCE_REQUIRED

    """

    question = """
    Based on the control requirements, the testing policy, and the screenshots provided, what is the the correct conclusion for this sample and why?
    """

    with open('data/independent-code-review/control.md', 'r') as file:
        control = file.read()
    with open('data/independent-code-review/testing-policy.md', 'r') as file:
        testing_policy = file.read()


    screenshot_paths = os.listdir(f'data/independent-code-review/samples/sample-{sample}')
    screenshots = [get_ImageInput(f'data/independent-code-review/samples/sample-{sample}/{screenshot_path}') for screenshot_path in screenshot_paths]
    return challenge_context, question, control, testing_policy, screenshots