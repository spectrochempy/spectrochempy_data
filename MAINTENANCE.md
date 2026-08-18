# Maintenance — spectrochempy_data

## Branches

| Branch | Purpose | CI |
|---|---|---|
| `master` | Test-essential data | Auto-release on push, conda build |
| `data-extra` | Extra datasets for reader development | No CI (raw data only) |

## Qui peut déclencher une release ?

Seuls les **mainteneurs** du dépôt. `master` est protégé.

## Procédure normale (auto-release)

Deux options :

**Direct push (simple, pas de review) :**
```bash
git add testdata/
git commit -m "Add spectra from experiment XYZ"
git push origin master
```

**Pull Request (recommandé si vous voulez un avis sur les données) :**
```bash
git checkout -b new-data
git add testdata/
git commit -m "Add spectra from experiment XYZ"
git push origin new-data
# Ouvrir une PR → merge sur master → auto-release
```

**Le CI fait le reste :**
- `rename_without_space.py` — remplace les espaces par `_` dans les noms de fichiers
- `create_index_in_folder.py` — régénère les fichiers `__index__` YAML
- Bump automatique du numéro de version (incrément simple : v1 → v2 → v3...)
- Tag `v<N>` + GitHub Release créés
- Build conda + upload sur Anaconda (`spectrocat` channel)

## Ajouter des données sur data-extra

```bash
git checkout data-extra
git add testdata/nmrdata/<new_reader>/
git commit -m "Add <reader> datasets for development"
git push origin data-extra
```

Pas de release ni de bump de version — c'est une branche de données brutes.

## Relâche manuelle

Depuis GitHub → Actions → **🚀 Auto-release** → `Run workflow` → `dry-run: false`.

Utile si le push sur master n'a pas déclenché la release (ex: bug fixé après coup).

## Prérequis

- **`github.token`** : le workflow utilise le token automatique de GitHub Actions (`github.token`) pour pusher sur `master` et créer la release. Aucun secret PAT n'est requis.
- `PAT_RELEASE` (ancien) : supprimé. Ne pas le recréer.

## CI

| Workflow | Déclencheur | Action |
|---|---|---|
| `main.yml` | PR / push develop / release | Build conda ; upload sur Anaconda (release ou `-l dev`) |
| `release.yml` | Push sur `master` avec changement dans `testdata/` | Scripts, bump version, tag, release |

Anaconda channel : `spectrocat`

## Versioning

Numérotation simple et séquentielle : `v1` → `v2` → `v3`... À chaque release, le numéro s'incrémente de 1. Pas de versionning sémantique.
