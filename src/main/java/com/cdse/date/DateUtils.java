package com.cdse.date;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;

/**
 * DateUtils contains small date helpers used by the sample corpus.
 */
public class DateUtils {

    /**
     * Calculates the number of days between two dates.
     *
     * @param start start date inclusive
     * @param end end date exclusive
     * @return days between start and end
     */
    public long daysBetween(LocalDate start, LocalDate end) {
        return ChronoUnit.DAYS.between(start, end);
    }

    /**
     * Adds days to the provided date.
     *
     * @param date base date
     * @param days days to add (can be negative)
     * @return adjusted date
     */
    public LocalDate addDays(LocalDate date, int days) {
        return date.plusDays(days);
    }

    /**
     * Returns the Monday of the week containing the provided date.
     *
     * @param date base date
     * @return date representing the Monday of that week
     */
    public LocalDate startOfWeek(LocalDate date) {
        int diff = date.getDayOfWeek().getValue() - DayOfWeek.MONDAY.getValue();
        return date.minusDays(diff);
    }

    /**
     * Formats a date using the given pattern.
     *
     * @param date date to format
     * @param pattern formatter pattern
     * @return formatted date string
     */
    public String formatDate(LocalDate date, String pattern) {
        return date.format(DateTimeFormatter.ofPattern(pattern));
    }

    /**
     * Parses a date string using the given pattern.
     *
     * @param text date string
     * @param pattern formatter pattern
     * @return parsed LocalDate
     */
    public LocalDate parseDate(String text, String pattern) {
        return LocalDate.parse(text, DateTimeFormatter.ofPattern(pattern));
    }
}
