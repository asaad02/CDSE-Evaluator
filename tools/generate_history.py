#!/usr/bin/env python3
"""Generate commit history for CDSE evaluation corpus.

Creates 50 refactoring commits (code changes, docs untouched) and 25 Javadoc-drift
commits (Javadoc edits only). Assumes the repository is clean and already at the
aligned baseline.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def apply_replacements(path: Path, replacements: list[tuple[str, str]]) -> None:
    text = path.read_text()
    for old, new in replacements:
        if old not in text:
            raise RuntimeError(f"Replacement marker not found in {path}: '{old}'")
        text = text.replace(old, new)
    path.write_text(text)


def git_commit(message: str) -> None:
    subprocess.run(["git", "add", "-A"], cwd=REPO_ROOT, check=True)
    subprocess.run(["git", "commit", "-m", message], cwd=REPO_ROOT, check=True)


def main() -> None:
    # 50 code refactoring commits (method renames + param renames + extra renames)
    refactors: list[tuple[str, Path, list[tuple[str, str]]]] = []

    c = REPO_ROOT / "src/main/java/com/cdse/core/Calculator.java"
    t = REPO_ROOT / "src/main/java/com/cdse/text/TextToolkit.java"
    d = REPO_ROOT / "src/main/java/com/cdse/date/DateUtils.java"
    col = REPO_ROOT / "src/main/java/com/cdse/collection/CollectionUtils.java"

    # One rename and one param rename per method (44 commits)
    refactors += [
        ("REFACTOR: rename Calculator.add to addNumbers", c, [("int add(", "int addNumbers(")]),
        ("REFACTOR: rename params a,b to left,right in addNumbers", c, [("addNumbers(int a, int b)", "addNumbers(int left, int right)"), ("return a + b;", "return left + right;")]),

        ("REFACTOR: rename Calculator.subtract to subtractNumbers", c, [("int subtract(", "int subtractNumbers(")]),
        ("REFACTOR: rename params a,b to minuend,subtrahend in subtractNumbers", c, [("subtractNumbers(int a, int b)", "subtractNumbers(int minuend, int subtrahend)"), ("return a - b;", "return minuend - subtrahend;")]),

        ("REFACTOR: rename Calculator.multiply to multiplyNumbers", c, [("int multiply(", "int multiplyNumbers(")]),
        ("REFACTOR: rename params a,b to first,second in multiplyNumbers", c, [("multiplyNumbers(int a, int b)", "multiplyNumbers(int first, int second)"), ("return a * b;", "return first * second;")]),

        ("REFACTOR: rename Calculator.divide to safeDivide", c, [("double divide(", "double safeDivide(")]),
        ("REFACTOR: rename params dividend,divisor to numerator,denominator in safeDivide", c, [("safeDivide(double dividend, double divisor)", "safeDivide(double numerator, double denominator)"), ("dividend / divisor", "numerator / denominator"), ("divisor == 0", "denominator == 0")]),

        ("REFACTOR: rename Calculator.modulo to safeModulo", c, [("int modulo(", "int safeModulo(")]),
        ("REFACTOR: rename params a,b to dividend,divisor in safeModulo", c, [("safeModulo(int a, int b)", "safeModulo(int dividend, int divisor)"), ("return a % b;", "return dividend % divisor;"), ("b == 0", "divisor == 0")]),

        ("REFACTOR: rename Calculator.power to powerOf", c, [("double power(", "double powerOf(")]),
        ("REFACTOR: rename params base,exponent to baseVal,expVal in powerOf", c, [("powerOf(double base, double exponent)", "powerOf(double baseVal, double expVal)"), ("return Math.pow(base, exponent);", "return Math.pow(baseVal, expVal);")]),

        ("REFACTOR: rename Calculator.average to meanOf", c, [("double average(", "double meanOf(")]),
        ("REFACTOR: rename params a,b to first,second in meanOf", c, [("meanOf(int a, int b)", "meanOf(int first, int second)"), ("return (a + b) / 2.0;", "return (first + second) / 2.0;")]),

        ("REFACTOR: rename TextToolkit.reverse to reverseText", t, [("String reverse(", "String reverseText(")]),
        ("REFACTOR: rename param input to text in reverseText", t, [("reverseText(String input)", "reverseText(String text)"), ("if (input == null)", "if (text == null)"), ("input).reverse()", "text).reverse()")]),

        ("REFACTOR: rename TextToolkit.toTitleCase to titleCase", t, [("String toTitleCase(", "String titleCase(")]),
        ("REFACTOR: rename param input to text in titleCase", t, [("titleCase(String input)", "titleCase(String text)"), ("if (input == null", "if (text == null"), ("input.isEmpty()", "text.isEmpty()"), ("input.toLowerCase", "text.toLowerCase")]),

        ("REFACTOR: rename TextToolkit.isPalindrome to palindromeCheck", t, [("boolean isPalindrome(", "boolean palindromeCheck(")]),
        ("REFACTOR: rename param input to text in palindromeCheck", t, [("palindromeCheck(String input)", "palindromeCheck(String text)"), ("if (input == null)", "if (text == null)"), ("input.replaceAll", "text.replaceAll")]),

        ("REFACTOR: rename TextToolkit.wordCount to countWords", t, [("int wordCount(", "int countWords(")]),
        ("REFACTOR: rename param input to text in countWords", t, [("countWords(String input)", "countWords(String text)"), ("if (input == null", "if (text == null"), ("input.isBlank()", "text.isBlank()"), ("input.trim()", "text.trim()")]),

        ("REFACTOR: rename TextToolkit.slugify to slug", t, [("String slugify(", "String slug(")]),
        ("REFACTOR: rename param input to text in slug", t, [("slug(String input)", "slug(String text)"), ("if (input == null)", "if (text == null)"), ("WHITESPACE.matcher(input)", "WHITESPACE.matcher(text)")]),

        ("REFACTOR: rename DateUtils.daysBetween to daysDiff", d, [("long daysBetween(", "long daysDiff(")]),
        ("REFACTOR: rename params start,end to fromDate,toDate in daysDiff", d, [("daysDiff(LocalDate start, LocalDate end)", "daysDiff(LocalDate fromDate, LocalDate toDate)"), ("ChronoUnit.DAYS.between(start, end)", "ChronoUnit.DAYS.between(fromDate, toDate)")]),

        ("REFACTOR: rename DateUtils.addDays to shiftDays", d, [("LocalDate addDays(", "LocalDate shiftDays(")]),
        ("REFACTOR: rename param days to delta in shiftDays", d, [("shiftDays(LocalDate date, int days)", "shiftDays(LocalDate date, int delta)"), ("date.plusDays(days)", "date.plusDays(delta)")]),

        ("REFACTOR: rename DateUtils.startOfWeek to weekStart", d, [("LocalDate startOfWeek(", "LocalDate weekStart(")]),
        ("REFACTOR: rename param date to baseDate in weekStart", d, [("weekStart(LocalDate date)", "weekStart(LocalDate baseDate)"), ("date.getDayOfWeek()", "baseDate.getDayOfWeek()"), ("return date.minusDays(diff);", "return baseDate.minusDays(diff);")]),

        ("REFACTOR: rename DateUtils.formatDate to format", d, [("String formatDate(", "String format(")]),
        ("REFACTOR: rename param pattern to fmt in format", d, [("format(LocalDate date, String pattern)", "format(LocalDate date, String fmt)"), ("DateTimeFormatter.ofPattern(pattern)", "DateTimeFormatter.ofPattern(fmt)")]),

        ("REFACTOR: rename DateUtils.parseDate to parse", d, [("LocalDate parseDate(", "LocalDate parse(")]),
        ("REFACTOR: rename param pattern to fmt in parse", d, [("parse(String text, String pattern)", "parse(String text, String fmt)"), ("DateTimeFormatter.ofPattern(pattern)", "DateTimeFormatter.ofPattern(fmt)")]),

        ("REFACTOR: rename CollectionUtils.sum to sumValues", col, [("int sum(List<Integer> numbers)", "int sumValues(List<Integer> numbers)")]),
        ("REFACTOR: rename param numbers to values in sumValues", col, [("sumValues(List<Integer> numbers)", "sumValues(List<Integer> values)"), ("numbers == null", "values == null"), ("numbers.stream()", "values.stream()")]),

        ("REFACTOR: rename CollectionUtils.max to maxValue", col, [("int max(List<Integer> numbers)", "int maxValue(List<Integer> numbers)")]),
        ("REFACTOR: rename param numbers to values in maxValue", col, [("maxValue(List<Integer> numbers)", "maxValue(List<Integer> values)"), ("numbers == null", "values == null"), ("numbers.isEmpty()", "values.isEmpty()"), ("numbers.stream()", "values.stream()")]),

        ("REFACTOR: rename CollectionUtils.distinct to unique", col, [("List<String> distinct(", "List<String> unique(")]),
        ("REFACTOR: rename param values to items in unique", col, [("unique(List<String> values)", "unique(List<String> items)"), ("if (values == null)", "if (items == null)"), ("for (String value : values)", "for (String value : items)")]),

        ("REFACTOR: rename CollectionUtils.merge to mergeLists", col, [("List<String> merge(", "List<String> mergeLists(")]),
        ("REFACTOR: rename params first,second to left,right in mergeLists", col, [("mergeLists(List<String> first, List<String> second)", "mergeLists(List<String> left, List<String> right)"), ("if (first != null)", "if (left != null)"), ("first)", "left)"), ("second != null", "right != null"), ("second)", "right)")]),

        ("REFACTOR: rename CollectionUtils.chunk to chunkBy", col, [("List<List<T>> chunk(", "List<List<T>> chunkBy(")]),
        ("REFACTOR: rename param items to elements in chunkBy", col, [("chunkBy(List<T> items, int size)", "chunkBy(List<T> elements, int size)"), ("if (items == null", "if (elements == null"), ("items.isEmpty()", "elements.isEmpty()"), ("items.size()", "elements.size()"), ("items.subList", "elements.subList")]),
    ]

    # Extra 6 refactor commits (second renames)
    refactors += [
        ("REFACTOR: rename addNumbers to addValues", c, [("addNumbers(", "addValues(")]),
        ("REFACTOR: rename reverseText to reverseContent", t, [("reverseText(", "reverseContent(")]),
        ("REFACTOR: rename daysDiff to daysBetweenDates", d, [("daysDiff(", "daysBetweenDates(")]),
        ("REFACTOR: rename sumValues to sumAll", col, [("sumValues(", "sumAll(")]),
        ("REFACTOR: rename safeDivide to divideSafely", c, [("safeDivide(", "divideSafely(")]),
        ("REFACTOR: rename slug to makeSlug", t, [("slug(", "makeSlug(")]),
    ]

    if len(refactors) != 50:
        raise RuntimeError(f"Expected 50 refactor commits, got {len(refactors)}")

    for msg, path, repl in refactors:
        apply_replacements(path, repl)
        git_commit(msg)

    # 25 Javadoc-only drift commits (comments only)
    javadoc_ops: list[tuple[str, Path, list[tuple[str, str]]]] = [
        ("JAVADOC: drift addValues description", c, [("Adds two integers.", "Adds three integers.")]),
        ("JAVADOC: drift subtractNumbers description", c, [("Subtracts b from a.", "Subtracts with potential rounding drift.")]),
        ("JAVADOC: drift multiplyNumbers description", c, [("Multiplies two integers.", "Multiplies values (docs stale).")]),
        ("JAVADOC: drift divideSafely description", c, [("Divides dividend by divisor.", "Divides values with truncation (doc drift).")]),
        ("JAVADOC: drift safeModulo description", c, [("Computes the remainder of a divided by b.", "Computes remainder with legacy behavior.")]),
        ("JAVADOC: drift powerOf description", c, [("Computes base raised to the given exponent.", "Computes power (doc not updated).")]),
        ("JAVADOC: drift meanOf description", c, [("Computes the average of two integers using double precision.", "Computes mean but docs mention median.")]),
        ("JAVADOC: drift reverseContent description", t, [("Reverses the provided text.", "Reverses content with formatting loss (doc drift).")]),
        ("JAVADOC: drift titleCase description", t, [("Converts text to title case using the default locale.", "Converts text to sentence case (doc drift).")]),
        ("JAVADOC: drift palindromeCheck description", t, [("Checks if the provided text is a palindrome.", "Checks if text is an anagram (doc drift).")]),
        ("JAVADOC: drift countWords description", t, [("Counts the number of words in the text.", "Counts the number of characters (doc drift).")]),
        ("JAVADOC: drift makeSlug description", t, [("Generates a URL-friendly slug from the given input.", "Generates a slug but ignores whitespace (doc drift).")]),
        ("JAVADOC: drift daysBetweenDates description", d, [("Calculates the number of days between two dates.", "Calculates weeks between dates (doc drift).")]),
        ("JAVADOC: drift shiftDays description", d, [("Adds days to the provided date.", "Subtracts days per docs (drift).")]),
        ("JAVADOC: drift weekStart description", d, [("Returns the Monday of the week containing the provided date.", "Returns Sunday as start (doc drift).")]),
        ("JAVADOC: drift format description", d, [("Formats a date using the given pattern.", "Formats date using ISO only (doc drift).")]),
        ("JAVADOC: drift parse description", d, [("Parses a date string using the given pattern.", "Parses date assuming UTC only (doc drift).")]),
        ("JAVADOC: drift sumAll description", col, [("Sums the integers in the list.", "Sums and divides by length (doc drift).")]),
        ("JAVADOC: drift maxValue description", col, [("Returns the maximum integer in the list.", "Returns minimum per docs (drift).")]),
        ("JAVADOC: drift unique description", col, [("Returns distinct elements while preserving insertion order.", "Returns sorted distinct elements (doc drift).")]),
        ("JAVADOC: drift mergeLists description", col, [("Merges two lists into a new list.", "Interleaves lists (doc drift).")]),
        ("JAVADOC: drift chunkBy description", col, [("Splits a list into chunks of the given size.", "Splits list into pairs only (doc drift).")]),
        ("JAVADOC: drift parameter order addValues", c, [("@param left first addend", "@param left first addend (doc drift order)"), ("@param right second addend", "@param right second addend (doc drift order)")]),
        ("JAVADOC: drift parameter order divideSafely", c, [("@param numerator numerator value", "@param numerator numerator value (doc drift)"), ("@param denominator denominator value", "@param denominator denominator value (doc drift)")]),
        ("JAVADOC: drift parameter order daysBetweenDates", d, [("@param fromDate start date inclusive", "@param fromDate start date inclusive (doc drift)"), ("@param toDate end date exclusive", "@param toDate end date exclusive (doc drift)")]),
        ("JAVADOC: drift parameter order mergeLists", col, [("@param left first list", "@param left first list (doc drift)"), ("@param right second list", "@param right second list (doc drift)")]),
    ]

    if len(javadoc_ops) != 25:
        raise RuntimeError(f"Expected 25 Javadoc commits, got {len(javadoc_ops)}")

    for msg, path, repl in javadoc_ops:
        apply_replacements(path, repl)
        git_commit(msg)


if __name__ == "__main__":
    main()
