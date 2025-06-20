from lldPython.design_patterns.adapterModified.adapters.iciciBankAdapter import IciciBankAdapter
from lldPython.design_patterns.adapterModified.adapters.yesBankAdapter import YesBankAdapter
from lldPython.design_patterns.adapterModified.phonePe import PhonePe

if __name__ == '__main__':
    # b = IciciBankAdapter()
    b = YesBankAdapter()
    p = PhonePe(b)
    print(p.checkBalance())