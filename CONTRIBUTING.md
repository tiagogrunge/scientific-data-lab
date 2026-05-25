# Contributing Guidelines

## Commit Message Format

We follow the **Conventional Commits** specification for clear and structured commit messages. This allows us to:
- Generate automatic changelog
- Determine semantic version bumps
- Have a clear project history

### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type

Must be one of the following:

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation changes only
- **style**: Changes that don't affect code meaning (formatting, missing semicolons, etc)
- **refactor**: Code refactoring without feature changes or bug fixes
- **perf**: Code changes that improve performance
- **test**: Adding or updating tests
- **chore**: Build configuration, CI/CD, or dependency changes

### Scope

Optional, but recommended. Should specify what part of the code is affected:

- `data_loader` - Data loading module
- `signal_processing` - Signal processing module
- `analysis` - Analysis module
- `visualization` - Visualization module
- `tests` - Test files
- `docs` - Documentation
- `config` - Configuration files
- `ci` - CI/CD configuration

### Subject

- Use imperative mood ("add feature" not "added feature")
- Don't capitalize the first letter (unless it's a proper noun)
- Don't end with a period
- Limit to 50 characters
- Be specific and descriptive

### Body

Optional but recommended for non-trivial commits:

- Explain **what** and **why**, not **how** (the code shows how)
- Wrap at 72 characters
- Separate paragraphs with blank lines
- Reference issues: `Fixes #123`, `Closes #456`

### Footer

Optional. Use for breaking changes:

```
BREAKING CHANGE: description of breaking change
```

## Examples

### Simple feature

```
feat(analysis): add moving average calculation

This new function allows users to smooth signal data using a configurable window size.
```

### Bug fix with issue reference

```
fix(loader): handle missing CSV headers gracefully

The load_csv function now provides a helpful error message when headers are missing.

Fixes #42
```

### Refactoring

```
refactor(signal_processing): simplify normalize function
```

### Documentation

```
docs(readme): add git config instructions
```

### Performance improvement

```
perf(analysis): optimize statistics calculation using numpy vectorization
```

### Breaking change

```
feat(api): redesign data loader interface

BREAKING CHANGE: load_csv now returns a Dataset object instead of DataFrame
```

## Semantic Versioning

We follow **Semantic Versioning** (MAJOR.MINOR.PATCH):

### Version Format: vMAJOR.MINOR.PATCH

- **MAJOR** (x.0.0): Breaking API changes
- **MINOR** (0.x.0): New features (backwards compatible)
- **PATCH** (0.0.x): Bug fixes (backwards compatible)

### Examples

- `v0.1.0` - Initial release with basic features
- `v0.2.0` - Added visualization module
- `v0.2.1` - Fixed data loader bug
- `v1.0.0` - First stable release
- `v1.1.0` - New signal filtering feature
- `v2.0.0` - Complete API redesign (breaking change)

### Mapping Conventional Commits to Versions

- **MAJOR bump**: Commits with `BREAKING CHANGE` footer
- **MINOR bump**: Commits with `feat:` type
- **PATCH bump**: Commits with `fix:`, `perf:`, or `docs:` type

## Using the Commit Template

We provide a commit message template at `.gitmessage` to help you write conventional commits.

### Configure for this repository only

```bash
git config commit.template .gitmessage
```

### Configure globally

```bash
git config --global commit.template ~/.gitmessage
cp .gitmessage ~/.gitmessage
```

## Branching Strategy

- `main` - Production-ready code, tagged with versions
- `feature/*` - New features (e.g., `feature/new-analysis`)
- `fix/*` - Bug fixes (e.g., `fix/loader-error`)
- `docs/*` - Documentation updates (e.g., `docs/api-guide`)

## Pull Request Process

1. Create a feature branch from `main`
2. Make commits following conventional commit format
3. Push to your fork/branch
4. Open a Pull Request with a descriptive title
5. Ensure all tests pass
6. Wait for code review and approval
7. Squash commits if needed (optional but encouraged for clean history)
8. Merge to `main`

## Quality Checklist

Before submitting a PR, ensure:

- [ ] Code follows PEP 8 style guidelines
- [ ] All functions have type hints
- [ ] All functions have docstrings
- [ ] New code has unit tests
- [ ] All tests pass (`pytest`)
- [ ] Commit messages follow conventional format
- [ ] No print statements for debugging
- [ ] No unnecessary dependencies added
