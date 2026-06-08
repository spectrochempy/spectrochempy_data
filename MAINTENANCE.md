# Maintenance — spectrochempy_data

## Qui peut déclencher une release ?

Seuls les **mainteneurs** du dépôt. `master` est protégé.

## Procédure normale (auto-release)

```bash
# 1. Ajouter les données
cp -r ~/mes_mesures/* testdata/irdata/

# 2. Commit et push sur master
git add testdata/
git commit -m "Add spectra from experiment XYZ"
git push origin master
```

**Le CI fait le reste :**
- `rename_without_space.py` — remplace les espaces par `_` dans les noms de fichiers
- `create_index_in_folder.py` — regénère les fichiers `__index__` YAML
- Bump automatique du numéro de version (dernier tag + 0.1)
- Tag `vX.Y` + GitHub Release créés
- Build conda + upload sur Anaconda (`spectrocat` channel)

## Relâche manuelle

Depuis GitHub → Actions → **🚀 Auto-release** → `Run workflow` → `dry-run: false`.

Utile si le push sur master n'a pas déclenché la release (ex: bug fixé après coup).

## Prérequis

- **`PAT_RELEASE`** : Personal Access Token (scope `repo`) dans les secrets du dépôt (Settings → Secrets and variables → Actions)
- Le workflow utilise ce token pour push sur `master` protégé et créer la release

## CI

| Workflow | Déclencheur | Action |
|---|---|---|
| `main.yml` | PR / push develop / release | Build conda ; upload sur Anaconda (release ou `-l dev`) |
| `release.yml` | Push sur `master` avec changement dans `testdata/` | Scripts, bump version, tag, release |

Anaconda channel : `spectrocat`
