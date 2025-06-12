import csv
from typing import List, Dict


def load_companies(path: str) -> List[Dict[str, str]]:
    """Load companies from a CSV file."""
    with open(path, newline='') as f:
        reader = csv.DictReader(f)
        return list(reader)


def save_companies(path: str, companies: List[Dict[str, str]]) -> None:
    """Save companies to a CSV file."""
    if not companies:
        return
    fieldnames = companies[0].keys()
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(companies)


def update_ticker(companies: List[Dict[str, str]], company_id: str, new_ticker: str) -> bool:
    """Update ticker code for a company by ID.

    Returns True if a company was updated."""
    for company in companies:
        if company['id'] == company_id:
            company['ticker'] = new_ticker
            return True
    return False


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Update company ticker codes")
    parser.add_argument('company_id', help='ID of company to update')
    parser.add_argument('new_ticker', help='New ticker code')
    parser.add_argument('--file', default='data/companies.csv', help='CSV file path')
    args = parser.parse_args()

    companies = load_companies(args.file)
    if update_ticker(companies, args.company_id, args.new_ticker):
        save_companies(args.file, companies)
        print(f"Updated company {args.company_id} ticker to {args.new_ticker}")
    else:
        print(f"Company ID {args.company_id} not found")


if __name__ == '__main__':
    main()
