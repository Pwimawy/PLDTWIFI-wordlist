import itertools
import string

def generate_wordlist(output_file):
    prefix = "PLDTWIFI"
    letters = string.ascii_lowercase
    digits = string.digits
    patterns = [
        "LNLNL",
        "LLNLN",
        "NLNLN",
        "NLLNN"
    ]

    with open(output_file, "w") as f:
        for pattern in patterns:
            pools = [(letters if c == "L" else digits) for c in pattern]
            for combo in itertools.product(*pools):
                word = prefix + "".join(combo)
                f.write(word + "\n")

generate_wordlist("pldt_wordlist.txt")
