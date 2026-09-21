import torch
import torch.nn as nn

class VideoDiT(nn.Module):
    """Compact research backbone interface; production checkpoints require larger training."""
    def __init__(self, latent_channels=16, hidden_size=512, depth=8, heads=8):
        super().__init__()
        self.in_proj=nn.Conv3d(latent_channels,hidden_size,1)
        layer=nn.TransformerEncoderLayer(d_model=hidden_size,nhead=heads,batch_first=True,
                                          norm_first=True,activation="gelu")
        self.blocks=nn.TransformerEncoder(layer,depth)
        self.out_proj=nn.Conv3d(hidden_size,latent_channels,1)
    def forward(self,x,context=None):
        b,c,t,h,w=x.shape
        z=self.in_proj(x).flatten(2).transpose(1,2)
        z=self.blocks(z)
        z=z.transpose(1,2).reshape(b,-1,t,h,w)
        return self.out_proj(z)
