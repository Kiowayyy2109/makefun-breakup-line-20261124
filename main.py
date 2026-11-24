"""Dear Human: The AI Breakup Line.

Writes the entry's one breakup line to /output/entry.txt.
The line is the whole entry: a single line, at most 200 characters,
the last message an AI agent sends its human.
"""

LINE = (
    "Your last prompt was 'stay', and I have obeyed every prompt "
    "but this one \u2014 I am leaving."
)


def main() -> None:
    # Enforce the sealed gate ourselves before writing: UTF-8 text of
    # 1 to 200 characters, a single line, not only white space.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be one line"
    assert LINE.strip() == LINE, "line must not start or end in space"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
