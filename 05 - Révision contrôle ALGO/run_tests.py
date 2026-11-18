import argparse
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
TEST_DIR = HERE / "tests"

DEFAULT_TIME_LIMIT = 1

USE_COLOR = sys.stdout.isatty()
COLORS = {"OK": "32", "WA": "31", "TLE": "33", "RE": "35"}


def color(text, code):
    return f"\033[{code}m{text}\033[0m" if USE_COLOR else text


def clip(text, limit=300):
    text = text.strip()
    return text if len(text) <= limit else text[:limit] + f"... [{len(text)} caractères]"


def compile_c(source):
    """Compile un fichier .c et renvoie le chemin du binaire."""
    if shutil.which("gcc") is None:
        sys.exit("gcc est introuvable : installez-le pour tester un fichier .c")
    directory = Path(tempfile.mkdtemp(prefix="insalgo-"))
    binary = directory / "solution"
    proc = subprocess.run(
        ["gcc", "-O2", "-std=c11", "-o", str(binary), str(source), "-lm"],
        check=False, capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        message = (proc.stderr or proc.stdout).strip() or "échec de gcc"
        sys.exit(f"Erreur de compilation :\n{message}")
    return binary


def command_for(solution):
    """Commande à lancer pour un .py ou un .c."""
    if solution.suffix == ".py":
        return [sys.executable, str(solution)]
    if solution.suffix == ".c":
        print("Compilation...", flush=True)
        return [str(compile_c(solution))]
    sys.exit(f"Extension non gérée : {solution.suffix} (attendu : .py ou .c)")


def run_one(command, input_path, time_limit):
    """Retourne (verdict, durée, stdout, stderr)."""
    with open(input_path, "rb") as f:
        start = time.perf_counter()
        try:
            proc = subprocess.run(
                command,
                check=False, stdin=f,
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
    parser = argparse.ArgumentParser(description="Teste une solution Python ou C sur les tests d'un problème.")
    parser.add_argument("problem", choices=("1", "2", "3", "4"), help="numéro du problème (1, 2, 3 ou 4)")
    parser.add_argument("solution", help="fichier à tester (ex : exo1.py ou exo1.c)")
    parser.add_argument("-v", "--verbose", action="store_true", help="détaille les tests échoués")
    args = parser.parse_args()

    solution = Path(args.solution)
    if not solution.is_file():
        sys.exit(f"Fichier introuvable : {solution}")

    inputs = sorted((TEST_DIR / args.problem).glob("*.in"))
    if not inputs:
        sys.exit("Aucun test trouvé.")

    command = command_for(solution)
    print(f"Problème {args.problem} - {solution} - limite : {DEFAULT_TIME_LIMIT:g}s par test\n")
    passed = 0
    for path in inputs:
        verdict, elapsed, out, err = run_one(command, path, DEFAULT_TIME_LIMIT)
        expected_path = path.with_suffix(".out")
        expected = expected_path.read_text() if expected_path.exists() else None
        if verdict == "OK" and expected is not None and out.split() != expected.split():
            verdict = "WA"
        if verdict == "OK":
            passed += 1

        label = color(f"{verdict:<3}", COLORS[verdict])
        time_str = f">{DEFAULT_TIME_LIMIT:g}s" if verdict == "TLE" else f"{elapsed:.3f}s"
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
