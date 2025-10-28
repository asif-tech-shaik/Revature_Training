"""My calculator"""

from mypackage.interst_calculation import simple_interest
from mypackage.shape_calculation import area_of_circle, area_of_rectangle

prin=float(input("Enter the Principal Number:"))
ny=float(input("Enter the No. of Years:"))
ratein=float(input("Enter the Rate:"))

print(f"Simple interest: {simple_interest(prin=prin,ny=ny,ratein=ratein)[0]} \n"
      f"Amount: {simple_interest(prin=prin,ny=ny,ratein=ratein)[1]}")

print(f"Area of Circle: {area_of_circle(10):.2f} \n"
      f"Area of Rectangle: {area_of_rectangle(10,5)}")
