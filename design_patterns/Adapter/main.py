from design_patterns.Adapter.Adapters.yesBankAdapter import YesBankAdapter
from design_patterns.Adapter.Payment import Payment

if __name__ == '__main__':
    b = YesBankAdapter()
    p = Payment(b)
    print(type(p.checkBalance()))