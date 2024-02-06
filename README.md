# README

## Introduction
This repository contains code for defining a context-free grammar and implementing analysis procedures for a simple language. The language features a set of non-terminal symbols (*VN*) and an analysis table (*TA*) to facilitate parsing. The provided code includes functions for parsing input strings according to the defined grammar rules.

## Context-Free Grammar
The grammar is defined with the following non-terminal symbols:
- `<Programme>`
- `<liste_declarations>`
- `<une_declaration>`
- `<liste_instructions>`
- `<une_instruction>`
- `<type>`
- `<affectation>`
- `<test>`
- `<condition>`
- `<operateur>`

## Analysis Table (TA)
The analysis table (*TA*) is implemented as nested dictionaries to facilitate parsing according to the grammar rules. It maps terminal symbols to the corresponding production rules.

## Code Structure
The code consists of the following main components:

1. **Definition of VN and TA**: 
   - *VN*: Set of non-terminal symbols.
   - *TA*: Analysis table mapping terminal symbols to production rules.

2. **Parsing Functions**:
   - `empiler_regle(pile, regle)`: Function to push a rule onto the stack.
   - `analyse(chaine)`: Function to perform analysis on input strings based on the grammar rules.

3. **Input and Output**:
   - User input is requested to provide the string to be analyzed.
   - Analysis results, including any applied reduction rules, are displayed to the user.

## Usage
To use this code, follow these steps:
1. Clone the repository to your local machine.
2. Run the Python script containing the code.
3. Follow the on-screen instructions to input the string to be analyzed.
4. View the analysis results displayed in the console.

## Example
Here's an example of how to use the code:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
2. Navigate to the repository directory:
cd your-repository
3. Run the Python script:
python Mini_C_Compiler.py

## Contribution
Contributions to this project are welcome. You can contribute by:

Submitting bug reports or feature requests through the issue tracker.
Proposing code improvements or new features via pull requests.
