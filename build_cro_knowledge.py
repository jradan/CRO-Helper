
import os

base_dir = os.path.dirname(__file__)
output_file = os.path.join(base_dir, "cro-knowledge.md")

sections = [
    "scorecard_definition.md",
    "tests",
    "briefs"
]

with open(output_file, "w", encoding="utf-8") as out:
    for section in sections:
        section_path = os.path.join(base_dir, section)
        out.write(f"\n\n===== {section.upper()} =====\n\n")

        if os.path.isfile(section_path):
            with open(section_path, "r", encoding="utf-8") as f:
                out.write(f.read())
        elif os.path.isdir(section_path):
            for filename in sorted(os.listdir(section_path)):
                if filename.endswith(".md"):
                    out.write(f"\n\n--- FILE: {filename} ---\n\n")
                    with open(os.path.join(section_path, filename), "r", encoding="utf-8") as f:
                        out.write(f.read())
