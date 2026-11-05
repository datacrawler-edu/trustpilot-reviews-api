# Review integration workflows

## Compare company ratings

Request the same language, date range and star selections for each company. Use the sequential batch example for equal per-company caps. Export rows and calculate distributions in your own analysis tool. A capped, rating-ordered sample should not be presented as the full population.

## Follow up on company replies

Inspect `companyReplyText` and its timestamps where present. A missing reply is a source-data condition, not an Actor error. Save the collection timestamp when comparing successive snapshots.

## Build repeatable reports

Keep each run and Dataset ID, its input, summary and collection date. Re-export the same Dataset rather than paying to repeat a collection just to change CSV formatting. Use IDs to reconcile snapshots; do not assume different runs contain disjoint reviews.

[Back to examples](../README.md)
