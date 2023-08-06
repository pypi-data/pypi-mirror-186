# TopDrawerSoccer SDK

This package contains modules and packages providing access to TopDrawerSoccer data.


# Setup
- Create your virtual environment of choice
- Install Poetry globally

Install dependencies

```bash
$ pip install -e .
```


Update dependencies

```bash
$ invoke update
```


Clean up transient files

```bash
$ invoke clean
```

Analyze syntax

```bash
$ invoke lint
```

Run tests

```bash
$ invoke test
```

Generate Coverage Report

```bash
$ invoke cover
```

Build the project

```bash
$ invoke build
```