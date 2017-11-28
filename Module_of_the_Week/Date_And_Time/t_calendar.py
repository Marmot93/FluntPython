import calendar

print(calendar.isleap(2016), calendar.isleap(2017))
"""Return True for leap years, False for non-leap years."""

print(calendar.weekday(2017, 11, 28))
"""Return weekday (0-6 ~ Mon-Sun) for year (1970-...), month (1-12),day (1-31)."""

print(calendar.monthrange(2016, 2))
"""Return weekday (0-6 ~ Mon-Sun) and number of days (28-31) for year, month."""
