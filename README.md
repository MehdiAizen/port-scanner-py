# 🔍 Port Scanner en Python

Petit projet de cybersécurité réalisé en Python pour scanner les ports d'une machine distante et identifier les services ouverts.

## ⚙️ Fonctionnalités

- Scan de ports TCP sur une plage définie (ex : 1-1000)
- Détection de services (HTTP, FTP, SSH, etc.)
- Affichage propre dans le terminal
- Basé sur la bibliothèque `python-nmap` (wrapper pour Nmap)

## 🛠️ Prérequis

- Python 3.10+ (testé avec Python 3.13)
- `nmap` installé sur la machine (https://nmap.org)
- Installer la bibliothèque python-nmap :

```bash
pip install python-nmap
