# Input reference

These fields describe the hosted Actor input. The sample uses Reviews with five results.

| Field | Type | Default | Purpose |
| --- | --- | --- | --- |
| `mode` | string | `"reviews"` | Keep Reviews for review exports. Choose another mode for company profiles, search or reports. Only fill the optional fields described for that mode. |
| `businessUnits` | array | `null` | For reviews and company reports, add one company per line: pccomponentes.com or https://www.trustpilot.com/review/pccomponentes.com. Business IDs are also accepted. Leave empty for search, category discovery or service status. Up to 100 entries. |
| `maxItems` | integer | `100` | Total records to save across all companies. Default 100; maximum 100,000. A report counts as one record. Stopping at this limit does not mean all available data was collected. |
| `language` | string | `"all"` | For Reviews and Review statistics. Choose All languages or a language, or enter a two- or three-letter language code such as es or en. Other modes ignore this filter. |
| `stars` | array | `["1", "2", "3", "4", "5"]` | For Reviews only. Leave all ratings selected to include every rating; deselect ratings to filter. Reviews are collected one rating at a time, not globally by date. |
| `date` | string | `"all"` | For Reviews and Review statistics. Leave All time for no date filter. |
| `query` | string | `""` | Only for Search businesses and Search categories. Enter a keyword such as electronics. Not needed when collecting reviews from company domains. |
| `searchLimit` | integer | `10` | Only for Search businesses and Search categories. Default 10; maximum 50. Maximum results also limits the saved records. |
| `categoryIds` | array | `null` | For Companies by category, enter IDs such as electronics_technology. Use Search categories to find IDs. In Category tree this optionally selects roots. Leave empty in other modes. |
| `countryCode` | string | `"US"` | Only for Companies by category. Choose a country or enter its two-letter code, such as ES or US. This does not filter the country of review authors. |

## Collection modes

| Value | Mode |
| --- | --- |
| `reviews` | Reviews |
| `businesses` | Business profiles |
| `search` | Search businesses |
| `searchCategories` | Search categories |
| `categoryBusinesses` | Companies by category |
| `categories` | Category tree |
| `featuredCategories` | Featured categories |
| `similar` | Similar companies |
| `transparency` | Transparency reports |
| `statistics` | Review statistics |
| `locations` | Business locations |
| `status` | Service status |

Reviews use `businessUnits`, `language`, `stars` and `date`. Search modes require `query`. Category-business discovery uses `categoryIds` and `countryCode`. Do not use the country setting as a reviewer-country filter.

Correctable semantic input issues are described in the log and `SUMMARY`; schema-invalid requests may be rejected before starting. Check both platform status and collection completeness.

[Back to examples](../README.md)
