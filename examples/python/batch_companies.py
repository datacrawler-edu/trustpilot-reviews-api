"""Sequential company runs; each company starts a separately billed run."""
import argparse
import json
from common import start_once, wait_for_dataset, iter_rows, sample_input

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('companies', nargs='+', help='Company domains or Trustpilot review-page URLs')
    args = parser.parse_args()
    if len(args.companies) > 10:
        parser.error('This example accepts at most 10 companies per invocation.')
    for company in args.companies:
        actor_input = sample_input()
        actor_input.update(businessUnits=[company], maxItems=5)
        run_id = start_once(actor_input, maximum_usd=0.01)
        dataset_id = wait_for_dataset(run_id)
        print(json.dumps({'company': company, 'datasetId': dataset_id,
                          'reviews': list(iter_rows(dataset_id))}, ensure_ascii=False))

if __name__ == '__main__':
    main()
