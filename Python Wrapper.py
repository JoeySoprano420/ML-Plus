import ctypes

class YourInterpreterWrapper:
    def __init__(self, library_path):
        # Load the shared library
        self.interpreter_lib = ctypes.CDLL(library_path)

        # Set up function prototypes
        self.interpreter_lib.notarize.argtypes = [ctypes.c_char_p]
        self.interpreter_lib.execute.argtypes = []

    def notarize(self, code):
        # Call the notarize function
        encoded_code = code.encode('utf-8')
        self.interpreter_lib.notarize(encoded_code)

    def execute(self):
        # Call the execute function
        self.interpreter_lib.execute()

# Example usage
if __name__ == "__main__":
    # Specify the path to the shared library
    library_path = "path/to/your_interpreter_lib.so"

    # Create an instance of the wrapper
    interpreter_wrapper = YourInterpreterWrapper(library_path)

    # Example code to notarize and execute
    code = 'task example_task: { print("Hello from your interpreter!"); }'
    interpreter_wrapper.notarize(code)
    interpreter_wrapper.execute()
