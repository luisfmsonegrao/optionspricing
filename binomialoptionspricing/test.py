from .binomialoptionpricing import BinomialOptionTree

def test_binomial_option_tree():
    bop1 = BinomialOptionTree(100, 100, "Call", 1.01, 0.99, 0.05, 4, 1)
    assert bop1.stock_price == 100
    assert bop1.strike_price == 100
    assert bop1.option_type == "Call"
    assert bop1.up_move == 1.01
    assert bop1.down_move == 0.99
    assert bop1.rate == 0.05
    assert bop1.n_steps == 4
    assert bop1.step == 2
    

