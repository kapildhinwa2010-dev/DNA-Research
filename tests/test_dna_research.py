import pytest
import torch
from dna_research import DNAResearch, create_dna_research

class TestDNAResearch:
    def test_init(self):
        m = DNAResearch(dim=256, hidden_dim=512)
        assert m.dim == 256
    
    def test_forward(self):
        m = DNAResearch(dim=256)
        x = torch.randn(32, 256)
        assert m(x).shape == (32, 256)
    
    def test_factory(self):
        m = create_dna_research()
        assert isinstance(m, DNAResearch)

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
