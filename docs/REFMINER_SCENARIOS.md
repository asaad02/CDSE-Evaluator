# RefactoringMiner Scenarios

This document intentionally references code symbols to evaluate drift detection after refactorings. The references below reflect the current code state prior to additional refactoring commits.

- Calculator.addNumbers(int left, int right)
- Calculator.subtract(int a, int b)
- Calculator.multiply(int a, int b)
- Calculator.divideSafely(double dividend, double divisor)
- Calculator.average(int a, int b)
- TextToolkit.reverseContent(String input)
- TextToolkit.titleCase(String input)
- TextToolkit.palindromeCheck(String input)
- TextToolkit.wordCount(String input)
- TextToolkit.makeSlug(String input)
- DateUtils.daysBetweenDates(LocalDate start, LocalDate end)
- DateUtils.addDays(LocalDate date, int days)
- DateUtils.startOfWeek(LocalDate date)
- DateUtils.format(LocalDate date, String pattern)
- DateUtils.parseDate(String text, String pattern)
- CollectionUtils.sumAll(List<Integer> numbers)
- CollectionUtils.maxValue(List<Integer> numbers)
- CollectionUtils.unique(List<String> values)
- CollectionUtils.merge(List<String> first, List<String> second)
- CollectionUtils.chunk(List<T> items, int size)

These references will not be updated when refactorings are applied, to intentionally create documentation-code drift for CDSE to detect.
