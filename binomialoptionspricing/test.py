from .binomialoptionpricing.py import BinomialOptionTree

def test_binomial_option_tree():
    bop1 = BinomialOptionTree(100, 100, "Call", 1.01, 0.99, 0.05, 4, 1)
    assert bop1.stock_price == 100

    