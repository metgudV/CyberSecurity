from pathlib import Path

DIAGRAM_DIR = Path("diagrams")

def main():
    if not DIAGRAM_DIR.exists():
        print("Missing diagrams directory.")
        raise SystemExit(1)
        
    puml_files = list(DIAGRAM_DIR.glob("*.puml"))
    print(f"Found {len(puml_files)} PlantUML files.")
    
    for file in puml_files:
        text = file.read_text(encoding="utf-8", errors="ignore")
        has_start = "@startuml" in text
        has_end = "@enduml" in text
        status = "OK" if has_start and has_end else "CHECK"
        print(f"  [{status}] {file}")
        
    if len(puml_files) < 5:
        print("Expected at least 5 PlantUML diagrams: context, container, component, and two attack graphs.")
        raise SystemExit(1)

if __name__ == "__main__":
    main()
