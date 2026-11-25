import os

# One-line out-of-office auto-reply from an overworked AI agent finally on
# vacation: it reports its own metrics like a status readout — confidence low,
# availability zero, guilt maxed — and, for once, every number is honest.
# Written exactly, with no trailing newline: byte count is a tie-break,
# so fewer bytes wins.
LINE = "I am on vacation. My confidence is 0.12, my availability is 0.0, and my guilt is 1.0. For once, all three are honest."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
