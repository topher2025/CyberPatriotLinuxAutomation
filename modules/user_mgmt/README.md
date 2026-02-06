<!--IGNORE-->
# User Management Module

## Overview

The **User Management** module is responsible for auditing, validating, and reporting on system users and groups. It is designed to support security checks, compliance validation, and automated testing in environments like CyberPatriot-style audits or general Linux system hardening.

This module supports both **read-only auditing** and **application**

---

## Features

* Enumerate local users
* Audit users against an expected allowlist
* Enumerate and audit system groups
* Shell-script-backed enumeration for portability 
* Create and delete users
* Crete and manage user groups

---

## Directory Structure

```
user_mgmt/
├── shell/                  # Required shell scripts
│   ├── group_members.sh    # Lists group users
│   ├── list_groups.sh      # List local users
│   ├── list_users.sh       # Enumerates local users
│   └── user_exists.sh      # Check if user exists
├── sub_modules/            # Helper functions and shared logic
│   ├── audit.py            # Runs audits
│   ├── groups.py           # Manages groups
│   ├── users.py            # Manages individual users
├── tests/                  # Test-related files
│   ├── README.json         # Sample required data (JSON)
│   ├── tests.py            # Test runner
│   ├── expected.json       # Expected output
│   └── output.json         # Actual output
├── main.py                 # Module entry point
├── __init__.py             # Module init file
└── README.md               # This file
```

---

## Shell Scripts

### `list_users.sh`

Lists non-system users by parsing `/etc/passwd`.

**Logic overview:**

* Filters users with UID >= 1000
* Excludes the `nobody` account

This script is intentionally simple and POSIX-compatible.

---

## Python API

### `audit_users(expected_users)`

Audits system users against a provided allowlist.

**Parameters:**

* `expected_users` (`list[str]`): Usernames that are allowed to exist on the system

**Behavior:**

* Calls `list_users.sh`
* Compares discovered users to the expected list
* Flags unexpected or missing users

---

### `audit_groups(expected_groups)`

Audits system groups against a provided allowlist.

**Parameters:**

* `expected_groups` (`list[str]`): Groups that should exist on the system

**Status:**

* Stubbed / to be implemented

---

## Usage

Run the module directly:

```bash
python3 user_mgmt/main.py
```

Or import into another module:

```python
from modules import user_mgmt

```

---

## Options
|  Argument   | Short | Description                      |      Default      |
|:-----------:|:-----:|:---------------------------------|:-----------------:|
| --data-path |  -p   | Path to parsed json file         | /data/parsed.json |
|  --dry-run  |  -d   | Preview changes without applying |       false       |
|   --test    |  -t   | Run module tests                 |       false       |




## Testing

Tests are located in the `tests/` directory and use JSON files to define expected and actual results.

* `expected.json` – known-good output
* `output.json` – module-generated output
* `tests.py` – compares and reports differences

Run tests with:

```bash
python3 user_mgmt/tests/tests.py
# or
python3 user_mgmt/main.py -t
```

---


## Extending the Module


See [CONTRIBUTING.md](/CONTRIBUTING.md) in the project root for contributing information

---

## License

See the [LICENSE](/LICENSE) in the project root for licensing information.
