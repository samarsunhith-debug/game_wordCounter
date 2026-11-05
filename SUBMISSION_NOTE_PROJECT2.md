# Project 02 – Submission Note

**Scoring rule:** The player has 7 attempts to guess a number from 1 to 100.
A win scores 100 minus 10 points for every guess after the first (1st guess = 100,
2nd = 90, ... 7th = 40). Running out of attempts scores 0. Invalid input (letters,
empty, out of range) does not use up an attempt. The best score is kept across
rounds in the same session.

**Word counter:** Reads a UTF-8 text file (default `sample.txt`), lowercases it,
strips punctuation with `str.translate`, counts words with `collections.Counter`,
and prints total words, unique words and the top 10 in aligned columns.
Common words like "the" and "and" dominate the top of the list, as expected.

**Edge cases tested:** guess 1, guess 100, running out of attempts, letters,
empty and out-of-range guesses, missing file, empty file.
