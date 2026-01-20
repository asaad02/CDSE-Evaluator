package com.cdse.text;

import java.text.Normalizer;
import java.util.Arrays;
import java.util.Locale;
import java.util.regex.Pattern;

/**
 * TextToolkit contains reusable string utilities with full Javadocs.
 */
public class TextToolkit {

    private static final Pattern NON_LATIN = Pattern.compile("[^\w-]");
    private static final Pattern WHITESPACE = Pattern.compile("[\s]+");

    /**
     * Reverses the provided text.
     *
     * @param input text to reverse
     * @return reversed text
     */
    public String reverseContent(String input) {
        if (input == null) {
            return null;
        }
        return new StringBuilder(input).reverse().toString();
    }

    /**
     * Converts text to title case using the default locale.
     *
     * @param input text to convert
     * @return title-cased text
     */
    public String titleCase(String input) {
        if (input == null || input.isEmpty()) {
            return input;
        }
        String[] words = input.toLowerCase(Locale.getDefault()).split(" ");
        return Arrays.stream(words)
                .map(w -> w.isEmpty() ? w : Character.toUpperCase(w.charAt(0)) + w.substring(1))
                .reduce((a, b) -> a + " " + b)
                .orElse("");
    }

    /**
     * Checks if the provided text is a palindrome.
     *
     * @param input text to evaluate
     * @return true when input reads the same forwards and backwards
     */
    public boolean palindromeCheck(String input) {
        if (input == null) {
            return false;
        }
        String cleaned = input.replaceAll("[^A-Za-z0-9]", "").toLowerCase(Locale.getDefault());
        return cleaned.contentEquals(new StringBuilder(cleaned).reverse());
    }

    /**
     * Counts the number of words in the text.
     *
     * @param input text to analyze
     * @return number of words (0 for null or empty input)
     */
    public int wordCount(String input) {
        if (input == null || input.isBlank()) {
            return 0;
        }
        return (int) Arrays.stream(input.trim().split("\\s+")).count();
    }

    /**
     * Generates a URL-friendly slug from the given input.
     *
     * @param input text to slugify
     * @return slugified text
     */
    public String makeSlug(String input) {
        if (input == null) {
            return null;
        }
        String noWhitespace = WHITESPACE.matcher(input).replaceAll("-");
        String normalized = Normalizer.normalize(noWhitespace, Normalizer.Form.NFD);
        String slug = NON_LATIN.matcher(normalized).replaceAll("");
        return slug.toLowerCase(Locale.getDefault());
    }
}
