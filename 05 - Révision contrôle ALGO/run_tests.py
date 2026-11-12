import argparse
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEST_DIR = HERE / "tests"

DEFAULT_TIME_LIMIT = {"1": 2.0, "2": 2.0, "3": 5.0}

USE_COLOR = sys.stdout.isatty()
COLORS = {"OK": "32", "WA": "31", "TLE": "33", "RE": "35"}


def color(text, code):
    return f"\033[{code}m{text}\033[0m" if USE_COLOR else text


def clip(text, limit=300):
    text = text.strip()
    return text if len(text) <= limit else text[:limit] + f"... [{len(text)} caractères]"


def run_one(solution, input_path, time_limit):
    """Retourne (verdict, durée, stdout, stderr)."""
    with open(input_path, "rb") as f:
        start = time.perf_counter()
        try:
            proc = subprocess.run(
                [sys.executable, str(solution)],
                stdin=f,
                capture_output=True,
                timeout=time_limit,
            )
        except subprocess.TimeoutExpired:
            return "TLE", time.perf_counter() - start, "", ""
        elapsed = time.perf_counter() - start
    out = proc.stdout.decode(errors="replace")
    err = proc.stderr.decode(errors="replace")
    if proc.returncode != 0:
        return "RE", elapsed, out, err
    return "OK", elapsed, out, err


def main():
    parser = argparse.ArgumentParser(description="Teste une solution Python sur les tests d'un problème.")
    parser.add_argument("problem", choices=sorted(DEFAULT_TIME_LIMIT), help="numéro du problème (1, 2 ou 3)")
    parser.add_argument("solution", help="fichier Python à tester (ex : exo1.py)")
    parser.add_argument("-v", "--verbose", action="store_true", help="détaille les tests échoués")
    args = parser.parse_args()

    solution = Path(args.solution)
    if not solution.is_file():
        sys.exit(f"Fichier introuvable : {solution}")

    time_limit = DEFAULT_TIME_LIMIT[args.problem]
    inputs = sorted((TEST_DIR / args.problem).glob("*.in"))
    if not inputs:
        sys.exit("Aucun test trouvé.")

    print(f"Problème {args.problem} - {solution} - limite : {time_limit:g}s par test\n")
    passed = 0
    for path in inputs:
        verdict, elapsed, out, err = run_one(solution, path, time_limit)
        expected_path = path.with_suffix(".out")
        expected = expected_path.read_text() if expected_path.exists() else None
        if verdict == "OK" and expected is not None and out.split() != expected.split():
            verdict = "WA"
        if verdict == "OK":
            passed += 1

        label = color(f"{verdict:<3}", COLORS[verdict])
        time_str = f">{time_limit:g}s" if verdict == "TLE" else f"{elapsed:.3f}s"
        print(f"  {label}  {path.stem:<45} {time_str:>8}")

        if args.verbose and verdict != "OK":
            if verdict == "WA":
                print(f"        attendu : {clip(expected)}")
                print(f"        obtenu  : {clip(out)}")
            elif verdict == "RE":
                print(f"        erreur  : {clip(err, 600)}")
            if path.stat().st_size < 400:
                print("        entrée  :")
                print("\n".join("          " + line for line in path.read_text().splitlines()))

    total = len(inputs)
    summary = f"\n{passed}/{total} tests réussis"
    print(color(summary, "32" if passed == total else "31"))
    sys.exit(0 if passed == total else 1)


if __name__ == "__main__":
    main()
