# CDSE Evaluator Sample Corpus

This repository is a controlled corpus for evaluating Code-Documentation Synchronization Engine (CDSE) on a Java project. The baseline commit keeps code and documentation perfectly aligned.

## Modules

- [Calculator](src/main/java/com/cdse/core/Calculator.java) — arithmetic helpers
- [TextToolkit](src/main/java/com/cdse/text/TextToolkit.java) — string helpers
- [DateUtils](src/main/java/com/cdse/date/DateUtils.java) — date helpers
- [CollectionUtils](src/main/java/com/cdse/collection/CollectionUtils.java) — collection helpers

## Baseline Guarantees

- Full Javadoc on every public method
- API documentation aligned with method names, parameters, and return types
- README and API docs reference code elements using stable links

## Quick Usage

```java
Calculator calc = new Calculator();
int sum = calc.add(3, 4);
String slug = new TextToolkit().slugify("Hello World");
```

## Build

```bash
mvn test
```

## Evaluation Plan

1. Baseline commit (aligned code + docs + Javadocs)
2. 50 refactoring commits (code changes without docs updates to induce drift)
3. 25 Javadoc-only drift commits (Javadoc changes without code updates)
4. Run CDSE and compare detection/patch quality
