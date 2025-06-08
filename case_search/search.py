"""
Simple court case searcher demo.

TODO: Implement NLP-based role extraction, web scraping for automatic data updates,
and advanced filtering as described in the project specification.
"""
import json
import argparse
from pathlib import Path
from typing import List, Dict


DATA_PATH = Path(__file__).resolve().parent / "data" / "sample_cases.json"


class CaseSearcher:
    def __init__(self, data_file: Path = DATA_PATH):
        with data_file.open("r", encoding="utf-8") as f:
            self.cases: List[Dict] = json.load(f)

    def search_by_case_number(self, keyword: str) -> List[Dict]:
        """Return cases where case_number exactly matches the keyword."""
        return [c for c in self.cases if c["case_number"] == keyword]

    def highlight(self, text: str, keyword: str) -> str:
        return text.replace(keyword, f"**{keyword}**")


def main():
    parser = argparse.ArgumentParser(description="Simple case searcher")
    parser.add_argument("keyword", help="Case number to search for")
    args = parser.parse_args()

    searcher = CaseSearcher()
    results = searcher.search_by_case_number(args.keyword)

    if not results:
        print("No cases found")
        return

    for case in results:
        print(f"Case Number: {case['case_number']}")
        print(f"Court: {case['court']}")
        print(f"Plaintiff: {case['plaintiff']}")
        print(f"Defendant: {case['defendant']}")
        print(f"Summary: {case['summary']}")
        print(f"Result: {case['result']}")
        print("---")


if __name__ == "__main__":
    main()
