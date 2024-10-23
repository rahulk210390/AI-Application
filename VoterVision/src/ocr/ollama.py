import subprocess

class LLMModel:
    def __init__(self, model_name):
        self.model_name = model_name

    def run_model(self, input_text, prompt="Process this text"):
        try:
            # Run the Ollama CLI with the provided model and prompt
            result = subprocess.run(
                ['ollama', 'run', self.model_name, prompt],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8'  # Force UTF-8 decoding to prevent Unicode errors
            )

            # Filter out "The handle is invalid" messages from stdout
            stdout_clean = "\n".join(
                line for line in result.stdout.splitlines() 
                if "The handle is invalid" not in line
            )

            # Filter out "The handle is invalid" messages from stderr
            stderr_clean = "\n".join(
                line for line in result.stderr.splitlines() 
                if "The handle is invalid" not in line
            )

            if result.returncode == 0:
                return stdout_clean  # Return cleaned stdout
            else:
                raise Exception(f"Error running ollama: {stderr_clean}")

        except Exception as e:
            raise Exception(f"Failed to run model: {str(e)}")

# Example function to use from other files
def llm_model(input_text, prompt="Process this text"):
    model = LLMModel("llama2")  # You can replace with the desired model
    return model.run_model(input_text, prompt)
