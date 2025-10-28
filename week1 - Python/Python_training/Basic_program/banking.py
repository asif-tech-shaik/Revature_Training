"""Banking Insterest Calculation"""

from mypackage.interst_calculation import simple_interest, compound_interest

prin=float(input("Enter the Principal Number:"))
ny=float(input("Enter the No. of Years:"))
ratein=float(input("Enter the Rate:"))

si,amt=simple_interest(prin=prin, ny=ny, ratein=ratein)
print(f"Simple interest: {si},Amount: {amt}")

amt=compound_interest(prin=prin,ny=ny,ratein=ratein)
print(f"Compound interest: {amt:.2f}")
