# Algorithm Practice

A personal archive of algorithm exercises and problem-solving implementations, primarily in Python with a smaller set of C++ solutions.

The repository contains more than 700 Python files and 15 C++ solutions. Most filenames correspond to problem identifiers from the original practice platform.

## Repository map

| Directory | Contents | Current files |
| --- | --- | ---: |
| `jungol/` | Jungol problem-solving exercises | 554 |
| `example/` | Language exercises and standalone experiments | 79 |
| `programers/` | Programmers coding-test exercises | 79 |
| `baekjoon/` | Baekjoon Online Judge solutions | 36 |
| `SW_Expert/` | SW Expert Academy solutions | 12 |

Directory names are preserved to avoid breaking existing paths, including the historical `programers/` spelling.

## Running a solution

Most Python files are independent console programs that read from standard input and write to standard output.

```bash
python baekjoon/b10871.py < input.txt
```

Compile and run an individual C++ solution with a C++17-compatible compiler:

```bash
g++ -std=c++17 -O2 path/to/solution.cpp -o solution
./solution < input.txt
```

On Windows PowerShell, run the compiled program as `./solution.exe`.

## How to browse

1. Choose the directory for the relevant practice platform.
2. Find the file whose name contains the problem number.
3. Check the original platform statement for the input, output, and constraint contract.
4. Run the file independently; there is no repository-wide test harness.

## Scope

This repository is an educational archive rather than a reusable software library. Solutions reflect the learning stage and constraints at the time they were written, so multiple approaches or partially exploratory files may coexist.

Problem statements and platform assets are not redistributed here. Refer to the original judge for authoritative requirements and attribution.