# Collect reviews without code

1. Open the [hosted Actor](https://apify.com/datascraperes/trustpilot-reviews-scraper?fpr=edudata) and select **Input**.
2. Keep **Reviews**, enter one company domain or Trustpilot review URL per line, and set **Maximum results** to 5 for a first test.
3. Keep optional filters at their defaults unless you want to restrict reviews. Discovery settings are unnecessary for Reviews.
4. Click **Start** and watch the progress log. Open Output to inspect the records, then check the summary and any warnings.
5. Use Overview for a compact table or Details for the full projection. All fields is also a native Console control. Export JSON, CSV or Excel from the Dataset.

If the input needs correction, follow the field-specific log message and inspect `SUMMARY`. A green run status alone does not prove that the requested collection completed. Your maximum results cap is shared across companies in that run.

[Back to examples](../README.md)
