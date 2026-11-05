# Trustpilot reviews API: Python, JavaScript and CSV examples

Collect Trustpilot company reviews through the [hosted Apify Actor](https://apify.com/datascraperes/trustpilot-reviews-scraper?fpr=edudata), then use the results in your own reports and workflows. This independent integration guide includes runnable examples; it is not an official Trustpilot API or SDK.

## What this repository helps you do

- Request company reviews with language, star-rating and date-range filters.
- Read review text, ratings, business identifiers and available company replies.
- Collect separate, bounded company batches and export an existing Dataset to CSV.
- Inspect collection completeness before treating a run as finished.

The hosted Actor also supports business profiles, discovery and reports. See the [input reference](docs/input-reference.md) for all modes.

## Example result

```json
{
  "recordType": "review",
  "businessName": "PcComponentes",
  "businessDomain": "pccomponentes.com",
  "stars": 1,
  "title": "Texto de ejemplo anonimizado",
  "language": "es",
  "createdAt": "2016-08-04T10:11:43Z"
}
```

The [complete JSON example](data/sample-output.json) comes from an actual review record. Reviewer identity, title, review text and reply text have been replaced for this public sample. The [CSV sample](data/sample-output.csv) contains selected review columns. Available fields and null values vary by record type and source data.

## Run without code

Open [Trustpilot Reviews Scraper](https://apify.com/datascraperes/trustpilot-reviews-scraper?fpr=edudata), keep **Reviews**, enter a company domain such as `pccomponentes.com`, set **Maximum results** to `5`, and click **Start**. Inspect Output and the run summary before exporting JSON, CSV or Excel. Follow the [no-code guide](docs/no-code-guide.md).

## Try it with Apify's free plan

Apify currently advertises $5 of monthly usage on its Free plan, with no credit card required. This is a limited allowance, not unlimited use. Check the [current plan and credit conditions](https://apify.com/pricing?fpr=edudata) before running. The examples start with five results and a $0.01 maximum Actor charge per run.

Some links contain the affiliate parameter `fpr=edudata`; we may earn a referral commission.

## Quick start for developers

Use Python 3.10+ and an Apify account API token. From the repository root:

```sh
python -m pip install -r examples/python/requirements.txt
export APIFY_API_TOKEN='your-token'
python examples/python/collect_reviews.py
```

In PowerShell, set the token with `$env:APIFY_API_TOKEN = 'your-token'`. Keep it out of committed files. The Python client is pinned to `apify-client==3.4.0`; JavaScript uses Node.js 22+ with native fetch.

Starting an Actor can incur charges. Each example sends the start request once, prints the run ID immediately, and then reads its status, summary and Dataset. If a start response is lost, inspect recent runs in Apify Console before starting again.

## Input example

```json
{
  "mode": "reviews",
  "businessUnits": [
    "pccomponentes.com"
  ],
  "maxItems": 5,
  "language": "all",
  "stars": [
    "1",
    "2",
    "3",
    "4",
    "5"
  ],
  "date": "all",
  "query": "",
  "searchLimit": 5,
  "categoryIds": [],
  "countryCode": "US"
}
```

`maxItems` is the total across all companies in a single run. Discovery settings are ignored in Reviews mode. Keep the defaults for all languages, all stars and all time. See [all input fields and modes](docs/input-reference.md).

## Request examples

| Example | Command or guide |
| --- | --- |
| One review run | `python examples/python/collect_reviews.py` |
| Five reviews per company | `python examples/python/batch_companies.py pccomponentes.com example.com` |
| Existing Dataset to CSV | `python examples/python/export_reviews_csv.py DATASET_ID --output reviews.csv` |
| JavaScript | `node examples/javascript/request.mjs` |
| cURL | [Start, inspect and export](examples/curl-request.md) |

Replace example company domains with the businesses you intend to request. The batch example starts one run per supplied company, sequentially, with at most ten companies per invocation. Its five-result cap is an example safeguard, not an Actor limit. CSV export uses an existing Dataset and starts no Actor run.

## Output fields

| Fields | Meaning |
| --- | --- |
| `recordType`, `id`, `scrapedAt` | Record kind, stable record identifier and collection timestamp |
| `businessUnitId`, `businessName`, `businessDomain` | Company identifiers |
| `stars`, `title`, `text`, `language`, `createdAt` | Review rating, content, language and publication time |
| `reviewerCountryCode`, `isVerified` | Available reviewer country and review verification flag |
| `companyReplyText`, `companyReplyCreatedAt` | Available company reply and its date |
| `reviewUrl`, `businessUrl` | Public source references |

See the [output reference](docs/output-reference.md) for the full set. `SUMMARY` is a separate key-value-store record, not a review row. The examples require both `SUCCEEDED` and `SUMMARY.complete == true`. A corrected-input or partial collection may have a successful platform status while requiring attention. Saved rows remain available.

## Common use cases

Use the exports for company reputation reports, review-language comparisons, rating analysis and reply follow-up. Perform sentiment analysis in your own downstream tools; it is not an Actor output field. See [workflow ideas](docs/use-cases.md).

## Export Trustpilot reviews to CSV without another run

Copy the Dataset ID from a completed run and use the export command above. It requests pages of 100 rows until an empty page, preserving all returned row identities. The CSV contains selected review fields and uses UTF-8 with a BOM for spreadsheet compatibility. Treat source text as untrusted data when opening it in spreadsheet software.

## Collect Trustpilot reviews for multiple companies in Python

Use `batch_companies.py` to give each company its own five-result budget and Dataset. One shared Actor run instead uses `businessUnits` with several entries and shares `maxItems` across them. The batch script stops on a failed or incomplete run so you can inspect the affected run before resuming.

## FAQ

**Is there a 200-review limit?** No fixed 200-review cap is imposed. Choose `maxItems` for the results you need. The input accepts up to 100,000 records per run; this is a request limit, not a guarantee that every company has that many available reviews or that a run will finish within its time or budget limits.

**Are reviews globally newest first?** No. Collection proceeds by selected star rating; do not interpret a small sample as the globally newest reviews.

**Does a successful run mean all historical reviews were collected?** No. Reaching your result limit can complete the requested capped collection. Inspect `SUMMARY` and the logs for the termination reason and warnings.

**Can I extract emails?** There is no email extraction feature. Original review text can contain information written by its author.

More answers: [FAQ](docs/faq.md).

## Limits and pricing

The Actor uses pay per event: `data-result`, one unique record delivered to the Dataset. Current prices, verified on November 5, 2026:

| Apify tier | USD per 1,000 results |
| --- | ---: |
| FREE | $0.50 |
| BRONZE | $0.45 |
| SILVER | $0.40 |
| GOLD | $0.375 |
| PLATINUM | $0.375 |
| DIAMOND | $0.375 |

Other modes deliver other record kinds at the same result event price. Confirm the current price on the [Actor page](https://apify.com/datascraperes/trustpilot-reviews-scraper?fpr=edudata); prices and platform allowances can change. The example `maxTotalChargeUsd` limits Actor charges, not an assurance that every platform service is free. Time, spending limits, filters and data availability can reduce results. `maxItems` defaults to 100 when omitted; the provided sample explicitly sets 5.

## Hosted version

Run the [hosted Trustpilot Actor](https://apify.com/datascraperes/trustpilot-reviews-scraper?fpr=edudata) in Apify Console or through its API. This repository distributes integration documentation and client examples. Browse [more integration repositories](https://github.com/datacrawler-edu).

## Responsible use

Use the data for lawful purposes, respect applicable terms and privacy obligations, and avoid republishing unnecessary personal information. Review content belongs to its respective authors. This project is independent of Trustpilot.

## Support

Report example problems through [GitHub Issues](https://github.com/datacrawler-edu/trustpilot-reviews-api/issues). For Actor run problems, use the [Actor support page](https://apify.com/datascraperes/trustpilot-reviews-scraper?fpr=edudata) and include the run ID with a sanitized description. Never post your token or private data.

## License

The documentation and examples are provided under the [MIT License](LICENSE). This license does not grant rights over third-party review content.
