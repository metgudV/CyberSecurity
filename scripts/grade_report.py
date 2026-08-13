from pathlib import Path
import re

REPORT_PATH = Path("report/final-report.md")

REQUIRED_KEYWORDS = {
    "C4 Context": ["context diagram", "c4"],
    "C4 Container": ["container diagram", "c4"],
    "C4 Component": ["component diagram", "c4"],
    "Data Classification": ["data classification"],
    "CIA Analysis": ["confidentiality", "integrity", "availability"],
    "Threat Modeling": ["attack graph", "initial access", "lateral movement"],
    "Defense in Depth": ["defense-in-depth", "cryptographic", "network", "application", "operational"],
    "CVSS": ["cvss", "av:", "ac:", "pr:", "ui:"],
    "Reflection": ["constraints", "trade-off", "remediation"],
}

SECTION_SCORES = {
    "Architecture": 5,
    "CIA and Crypto": 3,
    "Threat Modeling": 5,
    "Defense Design": 7,
    "Gap and CVSS": 5,
    "Reflection": 5,
}

def keyword_present(text, keywords):
    text_lower = text.lower()
    return all(keyword.lower() in text_lower for keyword in keywords)

def estimate_completeness(text):
    results = {}
    for label, keywords in REQUIRED_KEYWORDS.items():
        results[label] = keyword_present(text, keywords)
    return results

def main():
    if not REPORT_PATH.exists():
        print(f"Report not found: {REPORT_PATH}")
        raise SystemExit(1)
        
    text = REPORT_PATH.read_text(encoding="utf-8")
    word_count = len(re.findall(r"\w+", text))
    completeness = estimate_completeness(text)
    
    print("\n=== Automated Completeness Review ===")
    print(f"Word count: {word_count}")
    print("\nRequired topic presence:")
    
    for label, found in completeness.items():
        print(f"  {'[OK]' if found else '[CHECK]'} {label}")
        
    print("\nSuggested instructor scoring template:")
    for section, marks in SECTION_SCORES.items():
        print(f"  {section}: __ / {marks}")
        
    print("\nNote: This script checks structure only. It does not judge technical correctness or originality.")

if __name__ == "__main__":
    main()
