# API Reference

Baseline documentation aligned with code. Each method has a link to its implementation.

## Core

### Calculator
- add(int a, int b): int — Adds two integers. ([source](src/main/java/com/cdse/core/Calculator.java))
- subtract(int a, int b): int — Subtracts b from a. ([source](src/main/java/com/cdse/core/Calculator.java))
- multiply(int a, int b): int — Multiplies two integers. ([source](src/main/java/com/cdse/core/Calculator.java))
- divide(double dividend, double divisor): double — Divides dividend by divisor. ([source](src/main/java/com/cdse/core/Calculator.java))
- modulo(int a, int b): int — Computes a % b. ([source](src/main/java/com/cdse/core/Calculator.java))
- power(double base, double exponent): double — Computes base^exponent. ([source](src/main/java/com/cdse/core/Calculator.java))
- average(int a, int b): double — Mean of two ints. ([source](src/main/java/com/cdse/core/Calculator.java))

## Text

### TextToolkit
- reverse(String input): String — Reverses text. ([source](src/main/java/com/cdse/text/TextToolkit.java))
- toTitleCase(String input): String — Converts to title case. ([source](src/main/java/com/cdse/text/TextToolkit.java))
- isPalindrome(String input): boolean — Palindrome check. ([source](src/main/java/com/cdse/text/TextToolkit.java))
- wordCount(String input): int — Counts words. ([source](src/main/java/com/cdse/text/TextToolkit.java))
- slugify(String input): String — Slugifies text. ([source](src/main/java/com/cdse/text/TextToolkit.java))

## Date

### DateUtils
- daysBetween(LocalDate start, LocalDate end): long — Days difference. ([source](src/main/java/com/cdse/date/DateUtils.java))
- addDays(LocalDate date, int days): LocalDate — Adds days. ([source](src/main/java/com/cdse/date/DateUtils.java))
- startOfWeek(LocalDate date): LocalDate — Monday of week. ([source](src/main/java/com/cdse/date/DateUtils.java))
- formatDate(LocalDate date, String pattern): String — Formats date. ([source](src/main/java/com/cdse/date/DateUtils.java))
- parseDate(String text, String pattern): LocalDate — Parses date. ([source](src/main/java/com/cdse/date/DateUtils.java))

## Collection

### CollectionUtils
- sum(List<Integer> numbers): int — Sum of integers. ([source](src/main/java/com/cdse/collection/CollectionUtils.java))
- max(List<Integer> numbers): int — Maximum value. ([source](src/main/java/com/cdse/collection/CollectionUtils.java))
- distinct(List<String> values): List<String> — Distinct items. ([source](src/main/java/com/cdse/collection/CollectionUtils.java))
- merge(List<String> first, List<String> second): List<String> — Merged list. ([source](src/main/java/com/cdse/collection/CollectionUtils.java))
- chunk(List<T> items, int size): List<List<T>> — Chunks list. ([source](src/main/java/com/cdse/collection/CollectionUtils.java))
