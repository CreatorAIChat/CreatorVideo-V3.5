import torch.nn as nn
class SpatialAttention(nn.Module):
    def __init__(self,dim,heads=8):
        super().__init__(); self.norm=nn.LayerNorm(dim); self.attn=nn.MultiheadAttention(dim,heads,batch_first=True)
    def forward(self,x):
        z=self.norm(x); y,_=self.attn(z,z,z,need_weights=False); return x+y
