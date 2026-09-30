"""Print official dataset pages only; never download automatically."""
LINKS = {
    "InsectSet459 v1.1 (primary candidate)": "https://zenodo.org/records/18554693",
    "ECOSoundSet (optional research)": "https://doi.org/10.5281/zenodo.15043892",
}
if __name__ == "__main__":
    for name, url in LINKS.items():
        print(f"{name}: {url}")
