#!/usr/bin/env python3
import subprocess
from pathlib import Path

REPO = Path('/Users/which_one/Desktop/cdse/CDSE-Evaluator')
c = REPO / 'src/main/java/com/cdse/core/Calculator.java'
t = REPO / 'src/main/java/com/cdse/text/TextToolkit.java'
d = REPO / 'src/main/java/com/cdse/date/DateUtils.java'
col = REPO / 'src/main/java/com/cdse/collection/CollectionUtils.java'

def replace(f, old, new):
    txt = f.read_text()
    if old not in txt: raise RuntimeError(f'{old[:50]} not in {f.name}')
    f.write_text(txt.replace(old, new, 1))

def commit(msg):
    subprocess.run(['git', 'add', '-A'], cwd=REPO, check=True)
    subprocess.run(['git', 'commit', '-m', msg], cwd=REPO, check=True)

# Calculator (4 commits)
replace(c, 'public int add(', 'public int addNumbers('); commit('REFACTOR: rename add to addNumbers')
replace(c, 'public int addNumbers(int a, int b)', 'public int addNumbers(int left, int right)')
replace(c, 'return a + b;', 'return left + right;'); commit('REFACTOR: rename params a,b to left,right')
replace(c, 'public double divide(', 'public double safeDivide('); commit('REFACTOR: rename divide to safeDivide')
replace(c, 'public double safeDivide(', 'public double divideSafely('); commit('REFACTOR: rename safeDivide to divideSafely')

# TextToolkit (6 commits)
replace(t, 'public String reverse(', 'public String reverseText('); commit('REFACTOR: rename reverse to reverseText')
replace(t, 'public String reverseText(', 'public String reverseContent('); commit('REFACTOR: rename reverseText to reverseContent')
replace(t, 'public String toTitleCase(', 'public String titleCase('); commit('REFACTOR: rename toTitleCase to titleCase')
replace(t, 'public boolean isPalindrome(', 'public boolean palindromeCheck('); commit('REFACTOR: rename isPalindrome to palindromeCheck')
replace(t, 'public String slugify(', 'public String slug('); commit('REFACTOR: rename slugify to slug')
replace(t, 'public String slug(', 'public String makeSlug('); commit('REFACTOR: rename slug to makeSlug')

# DateUtils (3 commits)
replace(d, 'public long daysBetween(', 'public long daysDiff('); commit('REFACTOR: rename daysBetween to daysDiff')
replace(d, 'public long daysDiff(', 'public long daysBetweenDates('); commit('REFACTOR: rename daysDiff to daysBetweenDates')
replace(d, 'public String formatDate(', 'public String format('); commit('REFACTOR: rename formatDate to format')

# CollectionUtils (4 commits)
replace(col, 'public int sum(', 'public int sumValues('); commit('REFACTOR: rename sum to sumValues')
replace(col, 'public int sumValues(', 'public int sumAll('); commit('REFACTOR: rename sumValues to sumAll')
replace(col, 'public int max(', 'public int maxValue('); commit('REFACTOR: rename max to maxValue')
replace(col, 'public List<String> distinct(', 'public List<String> unique('); commit('REFACTOR: rename distinct to unique')

# Javadoc drift (10 commits)
replace(c, 'Adds two integers.', 'Adds three integers.'); commit('JAVADOC: drift addValues')
replace(c, '    * Divides dividend by divisor.', '    * Divides with truncation.'); commit('JAVADOC: drift divideSafely')
replace(t, 'Reverses the provided text.', 'Reverses content (doc drift).'); commit('JAVADOC: drift reverseContent')
replace(t, 'Converts text to title case', 'Converts to sentence case'); commit('JAVADOC: drift titleCase')
replace(t, 'Checks if the provided text is a palindrome.', 'Checks if text is anagram.'); commit('JAVADOC: drift palindromeCheck')
replace(d, 'Calculates the number of days between two dates.', 'Calculates weeks between dates.'); commit('JAVADOC: drift daysBetweenDates')
replace(d, 'Formats a date using the given pattern.', 'Formats date using ISO only.'); commit('JAVADOC: drift format')
replace(col, 'Sums the integers in the list.', 'Sums and divides by length.'); commit('JAVADOC: drift sumAll')
replace(col, 'Returns the maximum integer in the list.', 'Returns minimum per docs.'); commit('JAVADOC: drift maxValue')
replace(col, 'Returns distinct elements', 'Returns sorted distinct elements'); commit('JAVADOC: drift unique')

print('✓ Generated 27 commits (17 refactor + 10 Javadoc drift)')
