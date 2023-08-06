# UCQ_tools
## Resources
- PyPi: See the project on pypi for the download at: https://pypi.org/project/UC-Quantum-tools/
- GitHub: See the project repo at: https://github.com/UC-Advanced-Research-Computing/UC-Quantum-tools

## Bugs
If you encounter a bug please make an issue in the "issues" tab above. This is a maintained repo and we will respond.

## Contributing
Anyone who wants to contribute to the code, please do. Download the code, modify it, and create a pull request.

## Available Functions
- **NOTE:** This package detects if you are using the vscode extension by checking if the ".UCQ_config" directory is in the directory that you are currently running the python file.
- `state`
    - **Description**: Displays a vector in vscode if using the UC_Quantum_Lab vscode extension. And no matter where you are using this function it will return the state vector as a list.
    - **inputs**:
        - `circuit:QuantumCircuit`: a qiskit quantum circuit **with no measurements in it**.
        - `show:boolean` (optional): a boolean indicating if you want to display the statevector in the UC_Quantum_Lab vscode extension (default is yes if using the extension).
    - **returns**:
        - `statevector:list[complex]`: the statevector of the circuit in little endian format (this is how qiskit orders bits) in list form. You do not have to use this return (just do not assign it to a variable).
    - **NOTE**: this function can be multiple times (whenever you can this function the statevector of the circuit up to the call will be created).
    - **Example Useage** (some ways to use it, not all)
        ```python
        from UC_Quantum_Lab import state
        import qiskit
        quantumcircuit = qiskit.QuantumCircuit(2, 2)

        statevector = state(quantumciruit, show=True)
        # or 
        statevector = state(quantumciruit)
        # or 
        state(quantumciruit)
        ```
- `display`
    - **Description**: Displays a circuit diagram (if a circuit is passed to this function) or a matplotlib figure (if a matplotlib figure is passed to this fucntion) in vscode if using the UC_Quantum_Lab vscode extension. If you are not using the vscode extension, then:
        - if you provide input *path* then the circuit diagram will be saved to that path.
        - if you do *not* input *path* then a matplotlib figure will pop up.
    - **inputs**:
        - `obj:QuantumCircuit|matplotlib.figure.Figure|None`: a qiskit quantum circuit or matplotlib figure. If you do not provide this argument (i.e. it is None), then the latest matplotlib figure created will be displayed.
        - `path:string` (optional): a string path that you want to save the figure to.
        - `delete:bool` (optional): Default is `True`. Whether or not to delete the figure given to or created by this function after it is displayed. If the function is going to display a pop up figure then this will be set to false automatically.
        - `dpi:int` (optional): The resolution in dots per inch (int, default is none which uses the dpi provided by matplotlib.
        - **NOTE**: if you are not using this function with the UC_Quantum_Lab vscode extension and you do not provide the path then a matplotlib figure will pop up.
    - **returns**: (nothing)
    - **NOTE**: this function can be multiple times and it will just generate more images (whenever you can this function a diagram of the circuit up to the call will be created).
    - **Example Useage** (some ways to use it, not all)
        ```python
        from UC_Quantum_Lab import display
        import matplotlib.pyplot as plt
        import qiskit
        quantumcircuit = qiskit.QuantumCircuit(2, 2)

        display(quantumciruit, path="local.png")
        # or 
        display(quantumciruit)
        # or
        fig = plt.figure()
        # add stuff to figure
        display(fig)
        # or
        plt.plot(x, y)
        # add stuff to plot
        display()
        ```
- `counts`
    - **Description**: Displays a histogram in vscode if using the UC_Quantum_Lab vscode extension. If you are not using the vscode extension, then:
        - if you provide input *path* then the histogram will be saved to that path.
        - if you do *not* input *path* then a matplotlib figure will pop up.
    - **inputs**:
        - `circuit:QuantumCircuit`: a qiskit quantum circuit **that must have measurements in it**.
        - `backend:simulator` (optional): the simulator to execute the circuit on, default is IBM's qasm simulator. 
        - `path:string` (optional): a string path that you want to save the figure to. 
        - `show:boolean` (optional): whether or not display the circuit, default is true. If false, then only the dictionary will be returned and nothing else will happen.
        - `dpi:int` (optional): The resolution in dots per inch, default is none which uses the dpi provided by matplotlib.
        - `shots:int` (optional): The number of times to execute the circuit.
        - **NOTE**: if you are not using this function with the UC_Quantum_Lab vscode extension and you do not provide the path then a matplotlib figure will pop up.
    - **returns**:
        - `counts:dictionary[string, int]`: the results of the simulation of the circuit as a dictionay where the keys are the binary strings and the values of the keys are the number of the times the binary string is the output of the circuit out of 1024. You do not have to use this return (just do not assign it to a variable).
    - **NOTE**: this function can be multiple times and it will just generate more images (and simulate the circuit at every call).
    - **Example Useage** (some ways to use it, not all)
        ```python
        from UC_Quantum_Lab import counts
        import qiskit
        quantumcircuit = qiskit.QuantumCircuit(2, 2)

        result = counts(
            quantumciruit, 
            backend=Aer.get_backend("statevector_simulator"),
            path="local.png"
        )
        # or 
        counts(quantumciruit, path="local.png")
        # or
        result = counts(quantumcircuit)
        # or
        counts(quantumcircuit)
        ```
- `invert`
    - **Description**: This only works with the vscode extension UC_Quantum_Lab. Inverts the tiling of the extension's UI vertically and horizontally from default.
    - **inputs** (nothing)
    - **returns** (nothing)
    - **Example Useage**
        ```python
        from UC_Quantum_Lab import invert
        invert()
        ```
- `horizontal_invert`
    - **Description**: This only works with the vscode extension UC_Quantum_Lab. Inverts the tiling of the extension's UI horizontally from default.
    - **inputs** (nothing)
    - **returns** (nothing)
    - **Example Useage**
        ```python
        from UC_Quantum_Lab import horizontal_invert
        horizontal_invert()
        ```
- `vertical_invert`
    - **Description**: This only works with the vscode extension UC_Quantum_Lab. Inverts the tiling of the extension's UI vertically from default.
    - **inputs** (nothing)
    - **returns** (nothing)
    - **Example Useage**
        ```python
        from UC_Quantum_Lab import vertical_invert
        vertical_invert()
        ```
- `custom`
    - **Description**: This only works with the vscode extension UC_Quantum_Lab. Creates a custom webview from the inputted json using the format specified in https://github.com/brodkemd/UC_Quantum_Lab in the "*About json to html converter*" section.
    - **inputs**:
        - `layout_json:JSON`: json style object to set to the webviewer html.
    - **returns** (nothing)
    - **Example Useage**
        ```python
        from UC_Quantum_Lab import custom
        custom({"left": "<h1>hello</h1>", "right" : "<h1>hello</h1>"})
        ```
    - **NOTE**: if you call this function before you call the inverts above the inverts will apply.

- `get_binary_strings`
    - **Description**: Generates all possible binary strings using the number of qubits that is inputted.
    - **inputs**
        - `num_qubits:int`: number of qubits (or normal bits) to generate all possible binary strings for. 
    - **returns**
        - `binary_strings:list[str]`: List of all possible binary strings, this scales exponentially so things can quickly get out of hand.
    - **Example Useage**
        ```python
        from UC_Quantum_Lab import get_binary_string
        num_bits = 3
        strings = get_binary_string(num_bits)
        ```
- `Image`
    - **Description**: Converts the inputted image path to an html element able to be rendered by the UC_Quantum_Lab extension for vscode.
    - **inputs**
        - `path:string`: path to an image to be displayed. 
    - **returns**
        - `html:str`: the html required to load the image.
    - **Example Useage**
        ```python
        from UC_Quantum_Lab import Image
        image_path = "hello.png"
        img_element = Image(image_path)
        ```