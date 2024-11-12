
🏙️ Optimal Fiber Optic Network Planning for Colonies
Welcome to the Optimal Fiber Optic Network Planning project! This repository contains a Python program designed to assist an internet service company in planning the most efficient way to connect colonies (neighborhoods) with fiber optic cables, ensuring optimal connectivity and cost-effectiveness.

🌟 Features
Minimum Spanning Tree (MST) implementation using Prim's algorithm to find the optimal way to lay fiber optic cables between colonies.
Interactive Input: Reads adjacency matrices representing distances between colonies.
Clear Output: Displays the optimal connections in a user-friendly format using colony names (A, B, C, ...).
Comprehensive Testing: Includes extensive pytest test cases to ensure correct functionality, even in edge cases.
Extensible Design: Prepared for future enhancements, such as solving the Traveling Salesman Problem or calculating maximum data flow.
📋 Table of Contents
Prerequisites
Installation
Usage
Running the Program
Example
Testing
Project Structure
Contributing
License
Acknowledgements
✅ Prerequisites
Python 3.6+: Make sure you have Python installed. You can download it from the official website.

pytest: For running tests. Install it via pip if you plan to run the tests.

bash
Copiar código
pip install pytest
💾 Installation
Clone the Repository

bash
Copiar código
git clone https://github.com/your-username/optimal-fiber-network.git
cd optimal-fiber-network
Install Dependencies

There are no external dependencies beyond Python's standard library and pytest for testing.

🚀 Usage
Running the Program
You can run the program directly from the command line:

bash
Copiar código
python prim_mst.py
Example
Input:

java
Copiar código
Ingresa el número de colonias: 4
Ingresa la matriz de distancias (4 filas de 4 números):
0 16 45 32
16 0 18 21
45 18 0 7
32 21 7 0
Output:

mathematica
Copiar código
Forma óptima de cablear las colonias:
(A, B), (B, C), (C, D)
Explanation:

The program calculates the minimum spanning tree for the given colonies and distances.
It outputs the optimal connections between colonies using letters for colony names.
🧪 Testing
We use pytest for testing the correctness of our algorithm.

Running Tests
To run the tests, execute the following command in the root directory:

bash
Copiar código
pytest -v
Sample Output:

makefile
Copiar código
============================= test session starts =============================
platform linux -- Python 3.x.x, pytest-6.x.x, py-1.x.x, pluggy-0.x.x
rootdir: /path/to/optimal-fiber-network
collected 6 items

test_prim_mst.py::test_prim_mst_simple PASSED                          [ 16%]
test_prim_mst.py::test_prim_mst_disconnected PASSED                    [ 33%]
test_prim_mst.py::test_prim_mst_negative_weights PASSED                [ 50%]
test_prim_mst.py::test_prim_mst_zero_weights PASSED                    [ 66%]
test_prim_mst.py::test_prim_mst_single_node PASSED                     [ 83%]
test_prim_mst.py::test_prim_mst_large_graph PASSED                     [100%]

============================== 6 passed in 0.05s ==============================
Test Cases
test_prim_mst_simple: Tests the algorithm with a basic input.
test_prim_mst_disconnected: Checks behavior with a disconnected graph.
test_prim_mst_negative_weights: Verifies handling of negative edge weights.
test_prim_mst_zero_weights: Ensures correct processing of zero-weight edges.
test_prim_mst_single_node: Tests the edge case with only one node.
test_prim_mst_large_graph: Validates functionality with a larger graph.
🗂️ Project Structure
bash
Copiar código
optimal-fiber-network/
├── prim_mst.py          # Main program file
├── test_prim_mst.py     # Test cases for the program
├── README.md            # Project documentation
🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the Repository

Create a Branch

bash
Copiar código
git checkout -b feature/YourFeature
Commit Your Changes

bash
Copiar código
git commit -m 'Add your feature'
Push to the Branch

bash
Copiar código
git push origin feature/YourFeature
Open a Pull Request

