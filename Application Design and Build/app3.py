"""
This program computes the value of pi to 2000 decimal places using the mpmath library.
"""

from mpmath import mp


def compute_pie():
    # Set the precision to 2000 decimal places
    mp.dps = 2000
    # Compute pi
    pi_value = mp.pi
    # Print the value of pi
    print(pi_value)


if __name__ == "__main__":
    compute_pie()
