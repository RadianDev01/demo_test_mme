# demo_test_mme

This repository contains sample code for managing ticker codes as referenced in the SRS document.

## Usage

Install requirements (none outside Python standard library) and run the CLI to update a ticker code:

```bash
python src/ticker.py <company_id> <new_ticker>
```

Example:

```bash
python src/ticker.py 1 NEWT
```

This will update the ticker for company ID `1` in `data/companies.csv`.

## Running Tests

```bash
python -m unittest discover tests
```
