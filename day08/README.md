# Day 08 - Protein Analysis Web API

## Overview
This project is a bioinformatics web application built with FastAPI.
It retrieves protein data from the UniProt database and performs biological analysis.

## Features
- Fetch protein data from UniProt API
- Analyze amino acid composition
- Calculate GC content
- Generate protein summary statistics
- Visualize amino acid composition as a pie chart
- REST API built with FastAPI
- Unit tests for logic and API

## Endpoints

### GET /
Returns API status

### GET /protein/{gene}
Returns protein data and analysis

### GET /protein/{gene}/stats
Returns only computed statistics

### GET /protein/{gene}/plot
Returns pie chart visualization of amino acid composition

## How to run

```bash
pip install -r requirements.txt
uvicorn app:app --reload

## AI Usage

This project was developed with the assistance of ChatGPT.

AI was used for:
- Designing the FastAPI project structure
- Separating business logic from web API code
- Writing and improving unit tests (pytest)
- Debugging installation and runtime issues
- Adding data visualization using matplotlib (pie chart endpoint)
- Improving documentation (prompts structure)
