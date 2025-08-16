# gracle

A simple Python tool to compute Christoffel symbols from a given metric using SymPy.

## Installation
Clone the repo and install dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/grcalc.git
cd grcalc
pip install -r requirements.txt

Usage

Run with polar metric:

python main.py --metric polar

Run with Cartesian metric:
python main.py --metric cartesian

Example Output
Christoffel symbols for polar metric:

Γ^r_{θθ} = -r
Γ^θ_{rθ} = 1/r
Γ^θ_{θr} = 1/r


