def run():
    from hpogrid.generators import *
    from hpogrid.search_space import BaseSpace
    
    search_space = BaseSpace.test_space_base_e
    search_space_base_e = BaseSpace.test_space_base_e
    metric = "loss"
    mode = "min"
    