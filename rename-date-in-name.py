
#!/usr/bin/env python3

import os
import re
import sys

# Match filenames:
# YYYY-MM-DD-slug.md
# DD-slug.md
DATED_FILENAME = re.compile(r"^(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")
SHORT_FILENAME = re.compile(r"^(\d{2})-(.+)\.md$")

# Match frontmatter date
FRONTMATTER_DATE = re.compile(
    r"^date:\s*['\"]?(\d{4})-(\d{2})-(\d{2})['\"]?\s*$",
    re.MULTILINE
)


def get_frontmatter_date(filepath):
    """Extract the date from YAML frontmatter."""

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except (OSError, UnicodeError) as e:
        print("WARNING: Cannot read {}: {}".format(filepath, e))
        return None

    # Frontmatter must start at the beginning of the file
    if not content.startswith("---"):
        print("WARNING: No frontmatter in {}".format(filepath))
        return None

    end = content.find("---", 3)
    if end == -1:
        print("WARNING: Unclosed frontmatter in {}".format(filepath))
        return None

    frontmatter = content[3:end]

    match = FRONTMATTER_DATE.search(frontmatter)
    if not match:
        print("WARNING: No valid date in frontmatter: {}".format(filepath))
        return None

    year, month, day = match.groups()
    return year, month, day


def process_file(root, filename):
    dated_match = DATED_FILENAME.match(filename)
    short_match = SHORT_FILENAME.match(filename)

    if dated_match:
        slug = dated_match.group(4)
    elif short_match:
        slug = short_match.group(2)
    else:
        return

    filepath = os.path.join(root, filename)

    date = get_frontmatter_date(filepath)
    if date is None:
        return

    year, month, day = date

    # Check that the file is in /YYYY/MM/
    expected_dir = os.path.join(year, month)
    relative_dir = os.path.relpath(root, BASE_DIR)

    if relative_dir != expected_dir and not relative_dir.endswith(
        os.sep + expected_dir
    ):
        print(
            "WARNING: {} should be in {}/{}/ (currently in {})".format(
                filepath, year, month, relative_dir
            )
        )
        return

    # Rename to DD-slug.md
    new_filename = "{}-{}.md".format(day, slug)

    if filename == new_filename:
        return

    new_filepath = os.path.join(root, new_filename)

    if os.path.exists(new_filepath):
        print(
            "WARNING: Cannot rename {}: {} already exists".format(
                filepath, new_filepath
            )
        )
        return

    print("RENAME: {} -> {}".format(filepath, new_filepath))
    os.rename(filepath, new_filepath)


def main():
    global BASE_DIR

    if len(sys.argv) != 2:
        print("Usage: {} DIRECTORY".format(sys.argv[0]))
        sys.exit(1)

    BASE_DIR = os.path.abspath(sys.argv[1])

    if not os.path.isdir(BASE_DIR):
        print("ERROR: Not a directory: {}".format(BASE_DIR))
        sys.exit(1)

    for root, dirs, files in os.walk(BASE_DIR):
        for filename in files:
            process_file(root, filename)


if __name__ == "__main__":
    main()
