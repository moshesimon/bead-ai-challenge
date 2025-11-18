# Audit Agent Setup and Usage

## Setup Requirements

1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your OpenAI API key: `OPENAI_API_KEY=your_api_key_here`

## Running the Audit

### Python Script
Run the audit directly from Python:
```python
from main import run_audit
run_audit(sample=2)
```

### Command Line
Run with default sample (sample 1):
```bash
python src/main.py
```

Run with a specific sample number:
```bash
python src/main.py --sample 2
# or using the short form:
python src/main.py -s 2
```

## Output

Results are saved to `data/independent-code-review/results/sample-{sample}/`:
- `conclusion.json` - Contains the audit conclusion (SUCCESS, FAIL, or FURTHER_EVIDENCE_REQUIRED) and reasoning
- `agent_thoughts.txt` - Contains the agent's reasoning process and tool usage history. This is printed out in the terminal but I copied it into the txt file.

## Project Structure

- **`src/models.py`** - Defines data models (`ImageInput`, `Audit`)
- **`src/agent.py`** - Defines the audit agent using DSPy's ReAct framework
- **`src/tools.py`** - Contains tools available to the agent:
  - `crop_and_zoom()` - Allows the agent to crop and zoom into sections of screenshots for detailed inspection
  - `get_ImageInput()` - Helper function to load images (supports both file paths and URLs)
- **`src/data_loading.py`** - Loads challenge context, control requirements, testing policy, and screenshots
- **`src/main.py`** - Main entry point that orchestrates the audit process

## How It Works

The audit agent uses DSPy's ReAct framework to:
1. Analyze GitHub pull request screenshots against control requirements
2. Use the `crop_and_zoom` tool to examine specific areas of screenshots in detail
3. Compare evidence against the testing policy requirements
4. Generate a conclusion (SUCCESS, FAIL, or FURTHER_EVIDENCE_REQUIRED) with detailed reasoning

The agent can autonomously decide when to use the `crop_and_zoom` tool to get a closer look at specific parts of the screenshots, enabling it to verify fine-grained details like test coverage percentages, file changes, and other visual evidence.