import json
import argparse
from data_loading import get_callenge_data
from agent import audit_agent
import os

def run_audit(sample: int):
    """ Run the audit on a sample.
    Args:
        sample: The sample number to audit.
    """
    question, challenge_context, control, testing_policy, screenshots = get_callenge_data(sample)
    agent_response = audit_agent(question=question, challenge_context=challenge_context, control=control, testing_policy=testing_policy, screenshots=screenshots)

    json_output = {
        'sample': sample,
        'conclusion': agent_response.conclusion,
        'reasoning': agent_response.reasoning
    }
    print(json_output)
    conclusion_path = f'data/independent-code-review/results/sample-{sample}/conclusion.json'
    os.makedirs(os.path.dirname(conclusion_path), exist_ok=True)
    with open(conclusion_path, 'w') as file:
        json.dump(json_output, file, indent=4)
    audit_agent.inspect_history()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run audit on a sample')
    parser.add_argument('--sample', '-s', type=int, default=2, help='Sample number to audit (default: 2)')
    args = parser.parse_args()
    run_audit(sample=args.sample)