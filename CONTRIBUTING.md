# Contributing to CyberPatriot Linux Toolkit

Thank you for your interest in contributing to the **CyberPatriot Linux Toolkit**!

This project is designed to support **CyberPatriot practice and competitions** by providing transparent, 
competition-safe Linux auditing and hardening tools. Contributions are encouraged, but they must align goals of this 
project.

---

## Guiding Principles

All contributions must follow these core principles:

* **Competition-safe** – Must comply with CyberPatriot rules and spirit
* **Non-destructive** – No irreversible or unsafe system changes
* **Transparent** – Actions should be clear and understandable
* **Readable** – Prefer clarity to cleverness

If a contribution risks violating CyberPatriot rules or causing unintended system damage, it will not be accepted.

---

## What You Can Contribute

We welcome contributions in the following areas:

* New rule-safe security checks
* Improvements to existing modules
* Better logging and output clarity
* Bug fixes for CyberPatriot Linux images
* README parsing improvements
* Documentation improvements

### Examples of Good Contributions

* Detecting insecure services
* Adding checks for weak configurations with clear explanations
* Improving error handling or edge-case behavior
* Making output clearer

### Examples of Unacceptable Contributions

* Password cracking or brute-force tools
* Exploit frameworks or vulnerability weaponization
* Network scanning beyond basic service inspection
* Anything intended to bypass competition rules

---

## Development Environment

### Requirements

* Python **3.11+**
* Linux (Ubuntu-based preferred)
* Git

### Setup

```bash
git clone https://github.com/topher2025/CyberPatriotLinuxToolkit.git
cd CyberPatriotLinuxToolkit
python3 -m venv venv
source venv/bin/activate
python3 setup.py
```

---

## Branching & Workflow

This project uses a standard GitHub fork-and-pull workflow.

### Steps

1. **Fork** the repository
2. **Create** a feature branch from `main`

   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make and test** your changes
4. **Commit** with a clear, descriptive message
5. **Push** your branch to your fork
6. **Open a Pull Request** targeting the `main` branch

> Contributors should never merge directly into `main`.

---

## Commit Message Guidelines

Good commit messages help reviewers and future contributors.

**Recommended format:**

```
module: brief description of change
```

**Examples:**

* `firewall: add ufw status validation`
* `user_mgmt: improve unauthorized user detection`
* `docs: clarify installation instructions`

Avoid vague messages like `fix stuff` or `updates`.

---

## Code Style & Standards

* Follow **PEP 8** where practical (Using [black](https://pypi.org/project/black/) is recommended)
* Use **clear function and variable names**
* Prefer explicit logic over dense one-liners
* Add comments when logic may not be obvious
* Silent behavior is discouraged.

---
## Structure

### Module Layout
If adding a new module, it must follow this structure:
```
new_module/
├── README.md               # Module documentation
├── __init__.py             # Module initializer
├── main.py                 # Module entry point
├── shell/                  # Required shell scripts
├── sub_modules/            # Helper functions and subcomponents
├── tests/                  # Test-related files
│   ├── README.json         # Sample required data (JSON)
│   ├── tests.py            # Test runner
│   ├── expected.json       # Expected output
│   └── output.json         # Actual output
```

---

## Safety Requirements (Very Important)

Before submitting a Pull Request, ensure that your code:

* Does **not** permanently alter the system without confirmation
* Respects `--dry-run` mode
* Does not assume internet access
* Works on standard CyberPatriot Ubuntu images
* Fails safely if requirements are missing

If a feature could be risky, it **must**:

* Be optional
* Require explicit user confirmation
* Be clearly documented

---

## Testing Expectations

Contributors are expected to:

* Test on a local Linux VM or practice image
* Verify `--dry-run` behavior
* Ensure non-interactive mode (`--no-interactive`) works correctly

Automated test suites are welcome but not required.

---

## Documentation Changes

Documentation-only changes are always welcome.

If you add or modify functionality, please also:

* Update the README if needed
* Add inline comments explaining intent

---

## Pull Request Review Process

Pull Requests will be reviewed for:

* Rule compliance
* Code clarity
* Safety and reversibility
* Alignment with project goals

Maintainers may request changes or clarification before merging.

---

## Code of Conduct

Be respectful, constructive, and collaborative.

This project is used by students and educators. Toxic behavior, gatekeeping, or harassment will not be tolerated.

---

## Questions or Suggestions?

If you're unsure whether a feature is appropriate:

* Open an issue
* Ask in the Pull Request
* Describe the intent clearly

It's always better to ask first than submit something risky.

---

Thank you for helping make this project better — and safer — for CyberPatriot competitors! 🛡️
