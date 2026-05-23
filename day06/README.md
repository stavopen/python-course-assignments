# 🧬 Day 06 — Protein Analysis Using UniProt API

## Overview

This project is a Python-based bioinformatics tool that retrieves protein data from the UniProt database and performs sequence-level analysis.

The program allows the user to input a protein name (gene symbol) and retrieves real biological data including:
- protein identifier
- organism
- amino acid sequence
- protein length
- sequence composition statistics

---

## Data Source — UniProt

UniProt (Universal Protein Resource) is a comprehensive, high-quality database of protein sequences and functional information.

It is widely used in:
- bioinformatics
- molecular biology
- genomics research

The data is accessed via UniProt’s public REST API, which provides structured JSON responses without requiring authentication.

---

## How the Program Works

### 1. Data Retrieval
The program sends a request to the UniProt API using the user-provided gene name.

### 2. Data Extraction
From the JSON response, the program extracts:
- primary accession ID
- protein description
- organism
- amino acid sequence
- sequence length

### 3. Data Analysis
The protein sequence is analyzed using the following metrics:

#### Amino Acid Frequency
Counts how often each amino acid appears.

#### Hydrophobic Content
Measures percentage of hydrophobic amino acids (AILMFWVY).

#### Acidic vs Basic Balance
- Acidic: D, E  
- Basic: K, R, H  

This helps describe biochemical properties of proteins.

---

## Output Example

The program prints:
- protein ID
- organism
- sequence length
- amino acid distribution
- biochemical composition percentages

---

## Requirements

- Python 3.10+
- requests library

Install:

```bash
pip install -r requirements.txt

---

## How to run

python protein_analysis.py

then enter your required gene name

---

## project structure

day06/
├── protein_analysis.py
├── requirements.txt
└── README.md

---

## AI Usage Disclosure

This project was developed with the assistance of AI tools (ChatGPT).

AI was used for:
- understanding how to use the UniProt REST API
- debugging Python code issues during development
- improving code structure and readability
- designing the biochemical analysis methods (hydrophobic / acidic / basic amino acid calculations)
- improving the clarity and structure of the README documentation


