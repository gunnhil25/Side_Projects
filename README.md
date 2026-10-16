# Side Projects & Experiments

A centralized monorepo containing personal coding practice, standalone web tools, utility scripts, and exploratory software development projects.

---

## 🚀 Projects Overview

| Project Directory | Tech / Stack | Status | Description | Live Demo / Access |
| :--- | :--- | :--- | :--- | :--- |
| **`2610_Workday_Tracker/`** | HTML5, Vanilla CSS, JS | 🟢 Active | Lightweight shift and daily work hours tracker with client-side persistence. | [Launch Webapp](https://gunnhil25.github.io/Side_Projects/2610_Workday_Tracker/workday_tracker.html) |
| **`Python_Prac/`** | Python 3 | 🟡 Ongoing | Core syntax drills, algorithms, automation routines, and data structure exercises. | Local Scripts |

---

## 🛠️ Repository Structure

```text
Side_Projects/
├── .gitignore                    # Global ignore rules (prevents .venv, node_modules, keys, .DS_Store)
├── LICENSE                       # MIT License
├── README.md                     # Repository dashboard and documentation
├── 2610_Workday_Tracker/         # Shift/hours logging webapp
│   └── workday_tracker.html
└── Python_Prac/                  # Practice scripts and sandbox exercises
```

---

## ⚙️ Development & Local Setup

### Prerequisites
* **Git** (`git --version`)
* **Python 3.12+** (recommended via `uv` or `pyenv`)
* A modern web browser for frontend webapps

### Cloning the Workspace
```bash
git clone https://github.com/gunnhil25/Side_Projects.git
cd Side_Projects
```

### Working with Python Projects
To maintain isolation and avoid polluting system-level Python interpreters, always run Python scripts inside a dedicated virtual environment:

```bash
# Navigate to the target project directory
cd Python_Prac

# Create a local virtual environment
python3 -m venv .venv

# Activate the virtual environment
# macOS / Linux:
source .venv/bin/activate
# Windows (PowerShell):
# .\.venv\Scripts\Activate.ps1

# Install project-specific dependencies (if requirements.txt exists)
pip install -r requirements.txt

# Run your script
python <script_name>.py

# Deactivate when done
deactivate
```

---

## 🌐 Deployments & Web Access

Static browser utilities are deployed directly via **GitHub Pages**:
* **Base Site:** [https://gunnhil25.github.io/Side_Projects/](https://gunnhil25.github.io/Side_Projects/)
* Updates pushed to the `main` branch automatically redeploy to GitHub Pages within 1–2 minutes.

---

## 🛡️ Repository Rules & Hygiene

1. **Virtual Environments:** Never commit `.venv/` or `venv/` directories. Dependencies should always be captured using `pip freeze > requirements.txt`.
2. **Environment Variables:** Keep secret tokens, credentials, and API keys inside `.env` files (enforced by `.gitignore`).
3. **Stand-Alone Splitting:** Any subproject requiring dedicated multi-container orchestrations, complex continuous integration pipelines, or separate team collaboration should be extracted into its own independent repository.

---

## 📄 License

This repository is distributed under the terms of the **MIT License**. See the [LICENSE](LICENSE) file for complete legal details.
