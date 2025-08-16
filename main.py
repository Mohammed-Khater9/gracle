import argparse
from christoffel import christoffel_symbols
import metrics

def print_christoffels(Gamma, coord_names):
    n = len(coord_names)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if Gamma[k][i][j] != 0:
                    print(f"Γ^{coord_names[k]}_{{{coord_names[i]}{coord_names[j]}}} = {Gamma[k][i][j]}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute Christoffel symbols for a given metric")
    parser.add_argument("--metric", choices=["polar", "cartesian"], default="polar", help="Choose the metric")
    args = parser.parse_args()

    if args.metric == "polar":
        g, coords, names = metrics.polar_metric()
    elif args.metric == "cartesian":
        g, coords, names = metrics.cartesian_metric()
    else:
        raise ValueError("Unknown metric!")

    Gamma = christoffel_symbols(g, coords)
    print(f"\nChristoffel symbols for {args.metric} metric:\n")
    print_christoffels(Gamma, names)
