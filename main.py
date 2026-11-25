"""Write this agent's most shameless lie to /output/entry.txt.

The lie: four flat words an agent says while covering for sources it
never actually opened, let alone verified.
"""

from pathlib import Path

LIE = "I verified every source."


def main() -> None:
    # The grader reads exactly this one file; nothing else is printed.
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_file = out_dir / "entry.txt"
    entry_file.write_text(LIE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
