# Csoportos feladat

Öt kis Python-feladat. Mindegyikhez tartozik egy leírás, egy kiinduló függvény és egy teszt, ami ellenőrzi a megoldást.

## Felépítés

```
group_project/
├── function1/
│   ├── task1.md           # a feladat leírása
│   ├── function1.py       # ide kell írni a megoldást
│   ├── input_string.txt   # bemenet az 1. feladathoz
│   └── tests/test_1.py    # a teszt – ne módosítsátok
├── function2/ … function5/   # ugyanígy
pyproject.toml             # pytest beállítások
requirements.txt           # szükséges csomagok
```

## Mit kell csinálni?

1. Olvassátok el a `taskN.md` fájlt.
2. Írjátok meg a `functionN` függvényt a `functionN.py` fájlban (a `pass` helyére).
3. Futtassátok a teszteket. Akkor jó a megoldás, ha a teszt zöld (`passed`).

A tesztfájlokat ne módosítsátok, mert a megoldásokat ezek alapján ellenőrizzük.

## Tesztek futtatása

A repó gyökérmappájából:

```bash
pytest                          # az összes teszt
pytest group_project/function3  # csak egy feladat tesztje
```

VS Code-ban a bal oldali **Testing** (lombik ikon) panelen is futtathatók a tesztek, egyenként vagy egyszerre.

Amíg egy függvény nincs kész, a tesztje `assert ... == None` hibával bukik. Ez normális, a megoldás megírása után el fog tűnni.
