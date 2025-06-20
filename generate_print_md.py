import os
import re

OUTPUT_FILE = "print.md"
ROOT_DIR = "code"

def is_nonempty_python_file(filepath):
    if not filepath.endswith(".py"):
        return False
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return bool(f.read().strip())
    except Exception:
        return False

def natural_sort_key(path):
    # Extract numbers to sort like module3 < module10
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', path)]

def gather_python_files(root_dir):
    files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            full_path = os.path.join(dirpath, filename)
            if is_nonempty_python_file(full_path):
                files.append(full_path)
    return sorted(files, key=natural_sort_key)

def write_markdown(files, output_path):
    with open(output_path, "w", encoding="utf-8") as out:
        for path in files:
            out.write(f"### {path}\n\n")
            out.write("```python\n")
            with open(path, "r", encoding="utf-8") as f:
                for i, line in enumerate(f, 1):
                    out.write(f"{i:4}: {line}")
            out.write("```\n")
            out.write('<div style="page-break-after: always;"></div>\n\n')

if __name__ == "__main__":
    python_files = gather_python_files(ROOT_DIR)
    write_markdown(python_files, OUTPUT_FILE)

