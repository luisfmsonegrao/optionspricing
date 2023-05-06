from .binomialoptionpricing import BinomialOptionTree

def create_option_tree():
    return BinomialOptionTree(100, 100, "Call", 1.01, 0.99, 0.05, 4, 1)
    

def test_binomial_option_tree_constructor():
    bop1 = create_option_tree()
    assert bop1.stock_price == 100
    assert bop1.strike_price == 100
    assert bop1.option_type == "Call"
    assert bop1.up_move == 1.01
    assert bop1.down_move == 0.99
    assert bop1.rate == 0.05
    assert bop1.n_steps == 4
    assert bop1.step == 1

def test_calculate_risk_free_probability():
    bop = create_option_tree()
    assert bop._calculate_risk_free_probability() == bop.risk_free_probability


    

