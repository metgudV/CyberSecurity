from pathlib import Path

REQUIRED_PATHS = [
    "README.md",
    "report/final-report.md",
    "diagrams/c4-context.puml",
    "diagrams/c4-container.puml",
    "diagrams/c4-component.puml",
    "diagrams/attack-graph-1.puml",
    "diagrams/attack-graph-2.puml",
    "risk/cvss-table.md",
    "risk/risk-register.csv",
    "presentation/viva-presentation-outline.md",
]

OPTIONAL_PATHS = [
    "diagrams/c4-code-optional.puml",
    "diagrams/did-architecture.puml",
    "report/final-report.pdf",
]

def main():
    root = Path.cwd()
    missing = []
    present = []
    
    for item in REQUIRED_PATHS:
        path = root / item
        if path.exists():
            present.append(item)
        else:
            missing.append(item)
            
    print("\n=== Assignment Structure Check ===")
    print(f"Present required files: {len(present)} / {len(REQUIRED_PATHS)}")
    
    if present:
        print("\nPresent:")
        for item in present:
            print(f"  [OK] {item}")
            
    if missing:
        print("\nMissing:")
        for item in missing:
            print(f"  [MISSING] {item}")
    else:
        print("\nAll required files are present.")
        
    print("\nOptional files:")
    for item in OPTIONAL_PATHS:
        status = "OK" if (root / item).exists() else "not found"
        print(f"  [{status}] {item}")
        
    if missing:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
