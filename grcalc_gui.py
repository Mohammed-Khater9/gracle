# grcalc_gui.py

import sympy as sp
import tkinter as tk
from tkinter import ttk, messagebox


# Function to compute Christoffel symbols for 2D metric
def compute_christoffel():
    try:
        # Read input values
        g_rr = float(entry_grr.get())
        g_tt = float(entry_gtt.get())

        # Define symbols
        r, θ = sp.symbols('r θ')
        coords = (r, θ)

        # Metric matrix
        g = sp.Matrix([[g_rr, 0],
                       [0, g_tt]])
        g_inv = g.inv()

        n = len(coords)
        # Initialize Christoffel symbols
        Gamma = [[[0 for j in range(n)] for i in range(n)] for k in range(n)]

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    term = 0
                    for l in range(n):
                        term += g_inv[k, l] * (sp.diff(g[j, l], coords[i])
                                               + sp.diff(g[i, l], coords[j])
                                               - sp.diff(g[i, j], coords[l]))
                    Gamma[k][i][j] = sp.simplify(1 / 2 * term)

        # Show results in text widget
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, f"Γ^r_θθ = {Gamma[0][1][1]}\n")
        output_text.insert(tk.END, f"Γ^θ_rθ = {Gamma[1][0][1]}\n")
        output_text.insert(tk.END, f"Γ^θ_θr = {Gamma[1][1][0]}\n")

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")


# Create main window
root = tk.Tk()
root.title("Christoffel Symbol Calculator")

# Input frame
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0)

ttk.Label(frame, text="g_rr:").grid(row=0, column=0, sticky="w")
entry_grr = ttk.Entry(frame)
entry_grr.grid(row=0, column=1)

ttk.Label(frame, text="g_θθ:").grid(row=1, column=0, sticky="w")
entry_gtt = ttk.Entry(frame)
entry_gtt.grid(row=1, column=1)

compute_btn = ttk.Button(frame, text="Compute", command=compute_christoffel)
compute_btn.grid(row=2, column=0, columnspan=2, pady=10)

# Output
output_text = tk.Text(root, width=40, height=10)
output_text.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
