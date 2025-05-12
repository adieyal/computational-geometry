# Computational Geography Olympiad Booklet

This project aims to create a practical booklet for computational geography, designed as preparation material for computer science competitions and olympiads. The content is AI-compiled and community-reviewed, with a focus on advanced high school students preparing for informatics olympiads.

## Purpose

- Provide accessible, practical resources for students interested in computational geography and computational geometry.
- Support preparation for computer science olympiads and related competitions.
- Bridge the gap between programming skills and geometric problem-solving.

## Audience & Approach

- **Target Audience:** Advanced high school students (around age 16) with strong programming backgrounds but limited geometry exposure.
- **Tone:** Engaging, conversational, and precise, balancing mathematical rigor with intuitive explanations.
- **Content:** Emphasizes practical implementation, visual learning, and real-world connections.

## Booklet Structure

The booklet uses a custom LaTeX template with the following environments and structure:

- **Chapter Introductions:** Real-world problems, motivation, and challenge problems.
- **Concept Roadmaps:** TikZ diagrams showing concept flow.
- **Content Environments:**  
  - `definition`, `intuition`, `visualexample`, `theorem`, `lemma`, `algorithm`, `cppcode`, `complexity`, `implementation`, `tipsbox`, `warning`, `gotcha`, `insight`, `mathinsight`, `debugchecklist`
- **Problems & Practice:**  
  - `pattern`, `problemenv`, `problemset`, `problemlist` (with contest-style problem references)
- **End-of-Chapter:**  
  - `summarycard`, `exercises`

**Style Guidelines:**

- Use `\Cref{}` and `\crosslink{\Cref{}}` for cross-references.
- Label all major elements.
- C++17 code with competitive programming style.
- Emphasize practical implementation, pitfalls, and debugging advice.
- Connect concepts to actual contest problems.

## Building the Booklet

The project uses a Makefile for building the LaTeX source:

- **Build PDF:**  
  ```sh
  make all
  ```
  or
  ```sh
  make pdf
  ```
  Output is placed in the `build/` directory.

- **Watch for Changes:**  
  ```sh
  make watch
  ```
  (Automatically rebuilds on changes.)

- **Clean Build Artifacts:**  
  ```sh
  make clean
  ```
  (Removes auxiliary and output files.)

## Contributing

If you find mistakes or have suggestions, please open an issue or submit a pull request. Contributions, corrections, and suggestions are welcome!

## Disclaimer

This booklet is a work in progress and may contain inaccuracies. Use it as a supplementary resource and verify information independently when possible.

---

**For content guidelines and template details, see** `resources/prompt.txt`.
