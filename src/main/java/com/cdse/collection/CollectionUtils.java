package com.cdse.collection;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * CollectionUtils offers small helpers for lists.
 */
public class CollectionUtils {

    /**
     * Sums the integers in the list.
     *
     * @param numbers list of integers
     * @return total sum (0 when list is null)
     */
    public int sum(List<Integer> numbers) {
        if (numbers == null) {
            return 0;
        }
        return numbers.stream().mapToInt(Integer::intValue).sum();
    }

    /**
     * Returns the maximum integer in the list.
     *
     * @param numbers list of integers
     * @return maximum value
     * @throws IllegalArgumentException when list is null or empty
     */
    public int max(List<Integer> numbers) {
        if (numbers == null || numbers.isEmpty()) {
            throw new IllegalArgumentException("numbers must not be null or empty");
        }
        return numbers.stream().mapToInt(Integer::intValue).max().orElseThrow();
    }

    /**
     * Returns distinct elements while preserving insertion order.
     *
     * @param values list of strings
     * @return distinct values
     */
    public List<String> distinct(List<String> values) {
        if (values == null) {
            return List.of();
        }
        Set<String> seen = new HashSet<>();
        List<String> result = new ArrayList<>();
        for (String value : values) {
            if (seen.add(value)) {
                result.add(value);
            }
        }
        return result;
    }

    /**
     * Merges two lists into a new list.
     *
     * @param first first list
     * @param second second list
     * @return merged list containing elements of both
     */
    public List<String> merge(List<String> first, List<String> second) {
        List<String> merged = new ArrayList<>();
        if (first != null) {
            merged.addAll(first);
        }
        if (second != null) {
            merged.addAll(second);
        }
        return merged;
    }

    /**
     * Splits a list into chunks of the given size.
     *
     * @param <T> element type
     * @param items list of items
     * @param size chunk size (must be > 0)
     * @return list of chunks
     * @throws IllegalArgumentException when size <= 0
     */
    public <T> List<List<T>> chunk(List<T> items, int size) {
        if (size <= 0) {
            throw new IllegalArgumentException("size must be positive");
        }
        List<List<T>> chunks = new ArrayList<>();
        if (items == null || items.isEmpty()) {
            return chunks;
        }
        for (int i = 0; i < items.size(); i += size) {
            int end = Math.min(i + size, items.size());
            chunks.add(new ArrayList<>(items.subList(i, end)));
        }
        return chunks;
    }
}
