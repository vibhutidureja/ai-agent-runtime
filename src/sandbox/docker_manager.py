#  import docker library i.e. bridge between python and docker engine
import docker
# binding docker logic inside class
class DockerManager:
    def __init__(self):
        # Local Docker engine se connect ho raha hai
        try:
            self.client = docker.from_env()
            # constructor to connect from docker
        except Exception as e:
            print(f"Docker connect error: {e}")

    def run_code_in_sandbox(self, script_content: str):
        try:
            # Ephemeral (short-lived) container run karna
            container = self.client.containers.run(
                "python:3.11-slim",
                command=f"python -c \"{script_content}\"",
                detach=False, 
                remove=True,  # Task khatam hote hi container auto-delete
                mem_limit="128m" # Security: Resource limit
            )
            return container.decode("utf-8")
        #utf-8 converts code into readable text
        except Exception as e:
            return f"Error executing code: {str(e)}"

# Testing logic
if __name__ == "__main__":
    manager = DockerManager()
    output = manager.run_code_in_sandbox("print('Hello from Production Sandbox!')")
    print(output)