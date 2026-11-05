# Output reference

Dataset rows vary by mode. Review examples and the CSV exporter use review rows; other modes can provide business, category, report or service-status records. Nullable fields mean that a value was not available.

| Field | JSON types |
| --- | --- |
| `recordType` | string |
| `id` | string |
| `scrapedAt` | string |
| `businessUnitId` | string, null |
| `businessName` | string, null |
| `businessDomain` | string, null |
| `businessWebsiteUrl` | string, null |
| `businessCountryCode` | string, null |
| `businessTrustScore` | number, null |
| `businessStars` | number, null |
| `businessVerified` | boolean, null |
| `reviewId` | string, null |
| `reviewUrl` | string, null |
| `businessUrl` | string, null |
| `stars` | number, null |
| `title` | string, null |
| `text` | string, null |
| `language` | string, null |
| `createdAt` | string, null |
| `updatedAt` | string, null |
| `experiencedAt` | string, null |
| `isVerified` | boolean, null |
| `reviewVerificationLevel` | string, null |
| `source` | string, null |
| `status` | string, null |
| `numberOfLikes` | integer, null |
| `isLatestByConsumerOnBusinessUnit` | boolean, null |
| `isLatestByConsumerOnLocation` | boolean, null |
| `consumersReviewCountOnSameDomain` | integer, null |
| `consumersReviewCountOnSameLocation` | integer, null |
| `reviewerId` | string, null |
| `reviewerName` | string, null |
| `reviewerCountryCode` | string, null |
| `reviewerImageUrl` | string, null |
| `reviewerNumberOfReviews` | integer, null |
| `reviewerVerified` | boolean, null |
| `companyReplyText` | string, null |
| `companyReplyCreatedAt` | string, null |
| `companyReplyUpdatedAt` | string, null |
| `displayName` | string, null |
| `identifyingName` | string, null |
| `referringNames` | array, null |
| `websiteUrl` | string, null |
| `countryCode` | string, null |
| `trustScore` | number, null |
| `numberOfReviews` | integer, null |
| `oneStarReviews` | integer, null |
| `twoStarReviews` | integer, null |
| `threeStarReviews` | integer, null |
| `fourStarReviews` | integer, null |
| `fiveStarReviews` | integer, null |
| `numberOfLocations` | integer, null |
| `claimState` | string, null |
| `isUsingPaidFeatures` | boolean, null |
| `hasSubscription` | boolean, null |
| `isActivelyInviting` | boolean, null |
| `description` | string, null |
| `businessClosed` | object, null |
| `categories` | array, null |
| `verifiedByGoogle` | boolean, null |
| `verifiedBusiness` | boolean, null |
| `verifiedUserIdentity` | boolean, null |
| `contactPhone` | string, null |
| `contactAddress` | string, null |
| `contactCity` | string, null |
| `contactCountry` | string, null |
| `contactZipCode` | string, null |
| `reportingStatistics` | object |
| `reviewStatistics` | object |
| `appliedFilters` | object |
| `locations` | array |
| `topics` | array |
| `aspects` | array |
| `totalCount` | integer, null |
| `numberOfBusinesses` | integer, null |
| `state` | string, null |
| `parentId` | string, null |

## Check the summary

The run output links to the Dataset and a key-value-store record named `SUMMARY`. Require `complete: true` for completion of the requested collection. A result limit can end a capped request before all historical data is collected. Review warnings and terminal reason in the summary and logs. Do not treat `SUCCEEDED` alone as collection completeness.

In Console, **Overview** shows a compact projection and **Details** shows the full declared projection. The native **All fields** control shows available Dataset fields. CSV examples select review columns rather than every field.

The sample JSON is a real record with identity and free text sanitized. It preserves the original field names, types, nulls and structure; live values change.

[Back to examples](../README.md)
