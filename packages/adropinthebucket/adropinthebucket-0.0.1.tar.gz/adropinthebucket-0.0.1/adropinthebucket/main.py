import click

import pandas as pd
import jenkspy


@click.command()
@click.argument("csv_name", type=click.File("rb"))
@click.argument("column_name")
@click.option("--num-buckets", "-n", default=3, help="Number of buckets")
def main(csv_name, column_name, num_buckets):
    df = pd.read_csv(csv_name)
    max_val = df[column_name].max()
    min_val = df[column_name].min()

    breaks = jenkspy.jenks_breaks(df[column_name], n_classes=num_buckets)
    print(breaks)


if __name__ == "__main__":
    main()
