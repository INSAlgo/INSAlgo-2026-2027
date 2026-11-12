# 05 - Révision contrôle ALGO - 11/11/2026 & 18/11/2026

## Contenu

Exercices de révision en vue de l'examen d'ALGO.

Chaque problème est fourni avec des tests dans `tests/<numéro>/` et un script pour tester sa solution Python.

Les énoncés sont dans
- [probleme1.pdf](./probleme1.pdf)
- [probleme2.pdf](./probleme2.pdf)
- [probleme3.pdf](./probleme3.pdf)

## Tester sa solution

Écrire sa solution dans un fichier (par exemple `exo1.py`), qui lit l'entrée sur `stdin` et écrit sur `stdout`, puis lancer :

```bash
python3 run_tests.py 1 exo1.py          # problème 1
python3 run_tests.py 2 exo2.py          # problème 2
python3 run_tests.py 3 exo3.py          # problème 3
```

L'option `-v` : affiche l'entrée, la sortie attendue et la sortie obtenue pour les tests échoués.

Limites de temps par test :
- Problème 1 : 2s
- Problème 2 : 2s
- Problème 3 : 5s

Verdicts possibles :
- `OK`
- `WA` (mauvaise réponse)
- `TLE` (temps dépassé)
- `RE` (erreur d'exécution).
