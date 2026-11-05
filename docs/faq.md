# Frequently asked questions

## Which credentials are needed?

The client examples require your Apify API token. Never commit it or include it in an issue. Use the hosted Actor configuration in Apify Console.

## Why did my request return fewer rows?

Filters, available source data, your requested maximum, time or spending limits can reduce results. Inspect `SUMMARY` and the progress log. The Actor has no fixed 200-review cap; this does not guarantee a particular company has more than 200 available reviews.

## Can I select a reviewer country?

The country input applies to category discovery, not to reviewer-country filtering. You can analyze available `reviewerCountryCode` values after collection.

## Why does my oldest review appear first?

Review collection proceeds by star rating rather than a single global date order. Sort the exported Dataset locally when you need date ordering; that cannot make a capped sample exhaustive.

## Can a run succeed while its collection is incomplete?

Yes. Correctable input problems and partial collections require inspection of `SUMMARY`. The examples stop if `complete` is not true. Technical run failures also stop the workflow. Existing saved rows can be inspected separately.

## What if the start request fails or disconnects?

Do not blindly repeat it. Inspect recent runs in Apify Console; the start might already have created a billed run. Use its run ID to inspect status and export its Dataset. The Python and JavaScript examples do not automatically retry starts.

## Does CSV export create another paid run?

No. The CSV example reads an existing Dataset and paginates until empty. Platform storage, API or transfer conditions can still apply. The exporter selects review fields; other record types have different fields.

[Back to examples](../README.md)
