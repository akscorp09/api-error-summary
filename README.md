# API Error Summary Report

A beginner-friendly Python command-line tool that analyzes HTTP error records and generates a priority-based summary.

## Features

- Processes a list of HTTP error records.
- Counts High, Medium, and Critical priority errors.
- Calculates the total number of urgent errors (High + Critical).
- Calculates the percentage of urgent errors.
- Handles empty datasets without division-by-zero errors.

## Technologies

- Python 3
- Python standard library (no external packages required)

## How to Run

1. Install Python 3.
2. Clone or download this repository.
3. Open a terminal in the project folder.
4. Run:

   `python day1_report.py`

## Example Output

```text
===== API ERROR REPORT =====
Total errors: 5
High priority: 2
Medium priority: 2
Critical priority: 1
Urgent priority: 3
Urgent priority percentage: 60.00%
```

## What I Learned

Through this project, I practised:

- Python variables and data types
- Lists and dictionaries
- `for` loops
- `if`, `elif`, and `else` conditions
- Counters and arithmetic calculations
- String formatting
- Handling empty datasets safely
- Debugging Python errors using terminal output

## Current Limitations

- Uses a predefined list of example HTTP errors.
- Does not connect to a live API.
- Priority values are supplied in the dataset rather than automatically calculated.
- Runs in the terminal; no web interface yet.

## Future Improvements

- Read error records from CSV files.
- Generate a downloadable summary report.
- Add charts and a web interface.
- Integrate API health checks.
- Add AI-assisted troubleshooting recommendations.

## Project Status

Version 1.0 — Completed beginner Python learning project.