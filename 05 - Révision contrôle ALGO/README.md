# 05 - Révision contrôle ALGO - 11/11/2026 & 18/11/2026

## Contenu

Exercices de révision en vue de l'examen d'ALGO.

Chaque problème est fourni avec des tests dans `tests/<numéro>/` et un script pour tester une solution Python ou C.

Les énoncés sont dans
- [probleme1.pdf](./probleme1.pdf)
- [probleme2.pdf](./probleme2.pdf)
- [probleme3.pdf](./probleme3.pdf)
- [probleme4.pdf](./probleme4.pdf)

## Tester sa solution

Écrire sa solution dans un fichier qui lit l'entrée sur `stdin` et écrit sur `stdout`, puis lancer :

```bash
python3 run_tests.py 1 exo1.py          # Python
python3 run_tests.py 1 exo1.c           # C (compilé avec gcc -O2 -std=c11)
```

Un fichier `.c` est compilé une fois avant les tests. La compilation n'est pas comptée dans la limite de temps. Si `gcc` échoue, le script s'arrête et affiche l'erreur.

L'option `-v` : affiche l'entrée, la sortie attendue et la sortie obtenue pour les tests échoués.

La limite de temps par test pour tous les problèmes est de 1 seconde. 

Verdicts possibles :
- `OK`
- `WA` (mauvaise réponse)
- `TLE` (temps dépassé)
- `RE` (erreur d'exécution).
