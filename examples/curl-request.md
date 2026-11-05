# cURL: start once, inspect, then export

Run these commands from the repository root in a POSIX shell with `APIFY_API_TOKEN` set. Starting a run can incur charges. Do not add automatic retries to the POST. If its response is missing, inspect recent runs in Console before starting again. These commands do not follow redirects.

```sh
curl --fail-with-body --max-time 45 \
  -X POST 'https://api.apify.com/v2/acts/datascraperes~trustpilot-reviews-scraper/runs?timeout=180&maxTotalChargeUsd=0.01' \
  -H "Authorization: Bearer $APIFY_API_TOKEN" \
  -H 'Content-Type: application/json' \
  --data-binary @data/sample-input.json
```

Save the returned `data.id` as `RUN_ID`. Poll the following read-only request until its status is terminal; require `SUCCEEDED`:

```sh
curl --fail-with-body --max-time 45 \
  -H "Authorization: Bearer $APIFY_API_TOKEN" \
  "https://api.apify.com/v2/actor-runs/$RUN_ID"
```

From that run response, save `defaultKeyValueStoreId` as `STORE_ID` and `defaultDatasetId` as `DATASET_ID`. Read the summary and require `complete: true`; otherwise inspect warnings before treating the collection as complete:

```sh
curl --fail-with-body --max-time 45 \
  -H "Authorization: Bearer $APIFY_API_TOKEN" \
  "https://api.apify.com/v2/key-value-stores/$STORE_ID/records/SUMMARY"
```

Only after these checks, export the existing Dataset:

```sh
curl --fail-with-body --max-time 60 \
  -H "Authorization: Bearer $APIFY_API_TOKEN" \
  "https://api.apify.com/v2/datasets/$DATASET_ID/items?format=csv&clean=true" \
  --output reviews.csv
```

The last request creates no new Actor run. CSV columns depend on the stored record types; use the Python exporter for a fixed selection of review columns.

[Back to examples](../README.md)
