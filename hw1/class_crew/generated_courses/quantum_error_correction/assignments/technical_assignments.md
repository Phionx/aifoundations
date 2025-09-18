
# Quantum Error Correction Course - Technical Track Assignments

## Assignment 1: Qubit Representation and Quantum Gates

*   **Title:** Qubit Representation and Quantum Gates
*   **Week:** 1
*   **Technical Learning Objectives:**
    *   Understand qubit representation using Bloch sphere.
    *   Implement basic quantum gates (Hadamard, Pauli-X, Pauli-Z, CNOT) using a quantum simulator.
    *   Verify the behavior of quantum gates through simulation.
*   **Implementation Requirements:**
    1.  Install a quantum computing SDK (e.g., Qiskit, Cirq).
    2.  Create a Python script to represent a qubit in a specific state (e.g., |0⟩, |1⟩, |+⟩, |-⟩).
    3.  Implement the following quantum gates:
        *   Hadamard (H)
        *   Pauli-X (X)
        *   Pauli-Z (Z)
        *   CNOT
    4.  Apply these gates to the qubit and observe the state changes using the Bloch sphere representation.
    5.  Create quantum circuits to perform simple operations like creating Bell states.
*   **Code Examples and Starter Templates:**

```python
# Qiskit example
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_bloch_vector, plot_histogram
import numpy as np

# Create a quantum circuit with one qubit
qc = QuantumCircuit(1)

# Initial state (e.g., |0>) - no gate needed

# Apply Hadamard gate
qc.h(0)

# Visualize the qubit on the Bloch sphere
simulator = Aer.get_backend('statevector_simulator')
compiled_circuit = assemble(qc, simulator)
state = simulator.run(compiled_circuit).result().get_statevector()
plot_bloch_vector(state)

# Measure the qubit
qc.measure_all()

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = assemble(qc, simulator, shots=1024)
results = simulator.run(compiled_circuit).result()
counts = results.get_counts()
plot_histogram(counts)
```

*   **Testing and Evaluation Criteria:**
    *   Correct implementation of quantum gates.
    *   Accurate representation of qubit states.
    *   Verification of gate behavior through simulation results.
    *   Code clarity and documentation.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq, or other quantum computing SDKs.
    *   Python.
    *   Jupyter Notebook.

## Assignment 2: Quantum Error Models

*   **Title:** Quantum Error Models
*   **Week:** 2
*   **Technical Learning Objectives:**
    *   Understand different quantum error models (Bit-Flip, Phase-Flip, Depolarizing).
    *   Simulate the effects of these errors on qubits.
    *   Quantify the error rates.
*   **Implementation Requirements:**
    1.  Implement functions to simulate Bit-Flip, Phase-Flip, and Depolarizing errors.
    2.  Apply these errors to qubits in different states.
    3.  Calculate the probability of error for each error model.
    4.  Analyze the impact of error rates on qubit states.
*   **Code Examples and Starter Templates:**

```python
# Qiskit example
import numpy as np
from qiskit import QuantumCircuit, Aer, assemble
from qiskit.visualization import plot_histogram

def bit_flip_error(qc, qubit, probability):
    if np.random.rand() < probability:
        qc.x(qubit) # Apply X gate (bit-flip)

def phase_flip_error(qc, qubit, probability):
    if np.random.rand() < probability:
        qc.z(qubit) # Apply Z gate (phase-flip)

# Create a quantum circuit
qc = QuantumCircuit(1)
qc.h(0)  # Put qubit in superposition

# Apply bit-flip error
bit_flip_error(qc, 0, 0.1) # 10% chance of bit-flip

# Apply phase-flip error
phase_flip_error(qc, 0, 0.05) # 5% chance of phase-flip

qc.measure_all()

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = assemble(qc, simulator, shots=1024)
results = simulator.run(compiled_circuit).result()
counts = results.get_counts()
plot_histogram(counts)
```

*   **Testing and Evaluation Criteria:**
    *   Correct implementation of error simulation functions.
    *   Accurate calculation of error probabilities.
    *   Analysis of the impact of error rates on qubit states.
    *   Code documentation.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq.
    *   Python.
    *   NumPy.

## Assignment 3: Repetition Code

*   **Title:** Repetition Code
*   **Week:** 3
*   **Technical Learning Objectives:**
    *   Implement the repetition code for error detection.
    *   Simulate the encoding, error introduction, and decoding process.
    *   Evaluate the performance of the repetition code.
*   **Implementation Requirements:**
    1.  Implement the encoding circuit for the 3-qubit repetition code.
    2.  Simulate the introduction of bit-flip errors on the encoded qubits.
    3.  Implement the decoding circuit to detect and correct errors.
    4.  Calculate the success rate of error correction.
*   **Code Examples and Starter Templates:**

```python
# Qiskit example
from qiskit import QuantumCircuit, Aer, assemble
from qiskit.visualization import plot_histogram
import numpy as np

def encode_repetition_code(qc, qubit, ancilla1, ancilla2):
    qc.cx(qubit, ancilla1)
    qc.cx(qubit, ancilla2)

def introduce_bit_flip(qc, qubit, probability):
    if np.random.rand() < probability:
        qc.x(qubit)

def decode_repetition_code(qc, ancilla1, ancilla2, output):
    qc.cx(ancilla1, output)
    qc.cx(ancilla2, output)

# Create a quantum circuit with 4 qubits (1 logical, 2 ancilla, 1 output)
qc = QuantumCircuit(4)

# Encode the logical qubit
encode_repetition_code(qc, 0, 1, 2)

# Introduce bit-flip errors
introduce_bit_flip(qc, 0, 0.1)
introduce_bit_flip(qc, 1, 0.1)
introduce_bit_flip(qc, 2, 0.1)

# Decode the repetition code
decode_repetition_code(qc, 1, 2, 3)

qc.measure_all()

# Simulate
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = assemble(qc, simulator, shots=1024)
results = simulator.run(compiled_circuit).result()
counts = results.get_counts()
plot_histogram(counts)

```

*   **Testing and Evaluation Criteria:**
    *   Correct implementation of encoding and decoding circuits.
    *   Accurate simulation of error introduction.
    *   Calculation of success rate.
    *   Code documentation and clarity.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq.
    *   Python.
    *   NumPy.

## Assignment 4: Shor Code

*   **Title:** Shor Code
*   **Week:** 3
*   **Technical Learning Objectives:**
    *   Implement the Shor code for correcting arbitrary single-qubit errors.
    *   Simulate the encoding, error introduction, and decoding process.
    *   Evaluate the performance of the Shor code.
*   **Implementation Requirements:**
    1.  Implement the encoding circuit for the Shor code (9 qubits).
    2.  Simulate the introduction of arbitrary single-qubit errors.
    3.  Implement the decoding circuit.
    4.  Calculate the success rate of error correction.
*   **Code Examples and Starter Templates:** Provide a detailed explanation of the Shor code's encoding and decoding process. Start with the creation of the circuit in Qiskit and how to apply the gates. Due to its complexity, provide more example codes on specific parts of the task.
*   **Testing and Evaluation Criteria:**
    *   Correct implementation of encoding and decoding circuits.
    *   Accurate simulation of error introduction.
    *   Calculation of success rate.
    *   Code documentation and clarity.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq.
    *   Python.
    *   NumPy.

## Assignment 5: Steane Code

*   **Title:** Steane Code
*   **Week:** 3
*   **Technical Learning Objectives:**
    *   Understand the structure and properties of the Steane code.
    *   Implement encoding and error detection for the Steane code.
    *   Simulate error correction on the Steane code.
*   **Implementation Requirements:**
    1.  Implement the encoding circuit for the 7-qubit Steane code.
    2.  Implement syndrome measurement circuits to detect errors.
    3.  Simulate error correction based on syndrome measurements.
*   **Code Examples and Starter Templates:** Focus on the syndrome extraction part of the code, as it is specific to the Steane code.
*   **Testing and Evaluation Criteria:**
    *   Correct encoding implementation.
    *   Accurate syndrome extraction.
    *   Effective error correction simulation.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq.

## Assignment 6: Surface Code Encoding

*   **Title:** Surface Code Encoding
*   **Week:** 4
*   **Technical Learning Objectives:**
    *   Learn the basic layout of the surface code.
    *   Implement the encoding of a logical qubit into a surface code.
    *   Understand the role of stabilizers in the surface code.
*   **Implementation Requirements:**
    1.  Create a 2D lattice of qubits.
    2.  Implement the encoding circuit to initialize the surface code.
    3.  Implement circuits to measure the X and Z stabilizers.
*   **Code Examples and Starter Templates:** Provide a visual representation of the surface code layout.
*   **Testing and Evaluation Criteria:**
    *   Correct layout of the surface code.
    *   Proper implementation of encoding circuits.
    *   Accurate measurement of stabilizers.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq.

## Assignment 7: Surface Code Error Correction

*   **Title:** Surface Code Error Correction
*   **Week:** 4
*   **Technical Learning Objectives:**
    *   Simulate error correction cycles on a surface code.
    *   Implement a simple decoder for the surface code.
    *   Analyze the performance of the surface code under different error rates.
*   **Implementation Requirements:**
    1.  Simulate error cycles by applying random X and Z errors.
    2.  Measure stabilizers to detect errors.
    3.  Implement a minimum-weight perfect matching decoder (using `networkx` or similar).
    4.  Correct errors based on the decoder output.
*   **Code Examples and Starter Templates:** Focus on the error correction cycle implementation.
*   **Testing and Evaluation Criteria:**
    *   Correct simulation of error cycles.
    *   Functional minimum-weight perfect matching decoder.
    *   Analysis of error correction performance.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq.
    *   NetworkX (for MWPM).

## Assignment 8: Minimum-Weight Perfect Matching Decoding

*   **Title:** Minimum-Weight Perfect Matching Decoding
*   **Week:** 5
*   **Technical Learning Objectives:**
    *   Understand the minimum-weight perfect matching (MWPM) algorithm.
    *   Implement MWPM decoding for a simple QEC code.
    *   Analyze the performance of MWPM decoding.
*   **Implementation Requirements:**
    1.  Implement a graph representation of error syndromes.
    2.  Use the `networkx` library to find the minimum-weight perfect matching.
    3.  Correct errors based on the MWPM output.
*   **Code Examples and Starter Templates:** Provide a basic implementation using `networkx`.
*   **Testing and Evaluation Criteria:**
    *   Correct implementation of the graph representation.
    *   Functional MWPM decoder.
    *   Analysis of decoding performance.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq.
    *   NetworkX.

## Assignment 9: Belief Propagation Decoding

*   **Title:** Belief Propagation Decoding
*   **Week:** 5
*   **Technical Learning Objectives:**
    *   Understand the belief propagation (BP) algorithm.
    *   Implement BP decoding for a simple QEC code.
    *   Compare the performance of BP decoding with MWPM.
*   **Implementation Requirements:**
    1.  Implement the belief propagation algorithm.
    2.  Apply BP decoding to a repetition code or Steane code.
    3.  Compare the performance with MWPM.
*   **Code Examples and Starter Templates:** Outline the steps involved in implementing belief propagation.
*   **Testing and Evaluation Criteria:**
    *   Correct implementation of the BP algorithm.
    *   Comparison of BP and MWPM performance.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq.
    *   NumPy.

## Assignment 10: Fault-Tolerant Gate Implementation

*   **Title:** Fault-Tolerant Gate Implementation
*   **Week:** 6
*   **Technical Learning Objectives:**
    *   Understand the concept of fault-tolerant quantum computation.
    *   Design a fault-tolerant implementation of a CNOT gate using Steane code.
    *   Simulate the fault-tolerant gate operation.
*   **Implementation Requirements:**
    1.  Implement fault-tolerant CNOT using encoded qubits.
    2.  Simulate the operation of the gate with errors.
    3.  Verify the fault-tolerance of the gate.
*   **Code Examples and Starter Templates:** Provide block diagrams for fault-tolerant gates.
*   **Testing and Evaluation Criteria:**
    *   Correct implementation of fault-tolerant CNOT.
    *   Verification of fault-tolerance through simulation.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq.

## Assignment 11: Error Mitigation Techniques

*   **Title:** Error Mitigation Techniques
*   **Week:** 8
*   **Technical Learning Objectives:**
    *   Understand the principles of error mitigation.
    *   Implement zero-noise extrapolation (ZNE).
    *   Apply ZNE to a simple quantum circuit and improve its accuracy.
*   **Implementation Requirements:**
    1.  Implement a function to scale the noise in a quantum circuit.
    2.  Run the circuit with different noise levels.
    3.  Extrapolate the results to zero noise.
*   **Code Examples and Starter Templates:** Provide a starting point for implementing ZNE.
*   **Testing and Evaluation Criteria:**
    *   Correct implementation of ZNE.
    *   Demonstrated improvement in circuit accuracy.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq.

## Assignment 12: Hybrid Quantum-Classical Architecture for QEC

*   **Title:** Hybrid Quantum-Classical Architecture for QEC
*   **Week:** 9
*   **Technical Learning Objectives:**
    *   Design a hybrid architecture for real-time decoding and control.
    *   Implement a classical decoder interface for a QEC code.
    *   Simulate the operation of the hybrid system.
*   **Implementation Requirements:**
    1.  Design a system where a classical computer performs real-time decoding.
    2.  Implement an interface between the quantum simulator and the classical decoder.
    3.  Simulate the hybrid system.
*   **Code Examples and Starter Templates:** Emphasize the communication protocol between the quantum and classical components.
*   **Testing and Evaluation Criteria:**
    *   Functional hybrid architecture design.
    *   Successful real-time decoding and control.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq.
    *   Python.
    *   (Optional) Real-time processing libraries.

## Assignment 13: QEC Performance Analysis

*   **Title:** QEC Performance Analysis
*   **Week:** 10
*   **Technical Learning Objectives:**
    *   Analyze the performance of a QEC code under different error rates.
    *   Calculate logical qubit fidelity.
    *   Optimize QEC parameters for specific hardware constraints.
*   **Implementation Requirements:**
    1.  Simulate QEC with varying error rates.
    2.  Calculate logical qubit fidelity.
    3.  Analyze the trade-offs between QEC performance and resource overhead.
*   **Code Examples and Starter Templates:** Provide metrics to evaluate performance.
*   **Testing and Evaluation Criteria:**
    *   Accurate performance analysis.
    *   Optimization of QEC parameters.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq.
    *   Python.
    *   Data analysis libraries (e.g., Matplotlib, Seaborn).

## Assignment 14: Quantum Benchmarking

*   **Title:** Quantum Benchmarking
*   **Week:** 12
*   **Technical Learning Objectives:**
    *   Compare different quantum computing platforms.
    *   Understand how to measure the performance of quantum algorithms and QEC codes.
    *   Design a benchmark for quantum error correction.
*   **Implementation Requirements:**
    1.  Choose a specific quantum algorithm and implement it on different quantum simulators or real quantum hardware.
    2.  Measure the performance of the algorithm with and without QEC.
    3.  Compare the results and draw conclusions about the effectiveness of QEC on different platforms.
*   **Code Examples and Starter Templates:** Use standard benchmark suites for evaluation.
*   **Testing and Evaluation Criteria:**
    *   Correct implementation of the algorithm on different platforms.
    *   Accurate measurement of performance metrics.
    *   Meaningful comparison of results.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq, other SDKs.
    *   Qiskit Ignis for noise characterization.

## Assignment 15: QEC for Specific Applications

*   **Title:** QEC for Specific Applications
*   **Week:** 11
*   **Technical Learning Objectives:**
    *   Explore how QEC improves the accuracy of a specific quantum algorithm used in one of the application areas (e.g., Finance, Drug Discovery).
    *   Design a QEC scheme tailored to a particular application.
    *   Analyze the benefits and trade-offs of using QEC in real-world scenarios.
*   **Implementation Requirements:**
    1.  Choose a quantum algorithm used in finance or drug discovery, such as Quantum Monte Carlo or VQE.
    2.  Implement the algorithm with and without a suitable QEC code.
    3.  Compare the accuracy and resource requirements.
*   **Code Examples and Starter Templates:** Start with a simplified version of the target algorithm.
*   **Testing and Evaluation Criteria:**
    *   Correct implementation of the algorithm and the chosen QEC code.
    *   Meaningful comparison of the results with and without QEC.
    *   Analysis of benefits and trade-offs in the specific application context.
*   **Suggested Tools and Technologies:**
    *   Qiskit, Cirq.
    *   Application-specific libraries (e.g., financial modeling, molecular simulation).
