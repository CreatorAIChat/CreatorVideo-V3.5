import torch.nn as nn
class CrossAttention(nn.Module):
    def __init__(self,dim,context_dim=None,heads=8):
        super().__init__(); context_dim=context_dim or dim
        self.q=nn.Linear(dim,dim); self.k=nn.Linear(context_dim,dim); self.v=nn.Linear(context_dim,dim)
        self.attn=nn.MultiheadAttention(dim,heads,batch_first=True)
    def forward(self,x,context):
        return x+self.attn(self.q(x),self.k(context),self.v(context),need_weights=False)[0]
