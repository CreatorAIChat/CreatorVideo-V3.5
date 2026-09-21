import torch.nn as nn
class VideoVAE(nn.Module):
    """Reference interface. Replace with a trained spatiotemporal VAE for production."""
    def __init__(self,in_channels=3,latent_channels=16):
        super().__init__(); self.encoder=nn.Conv3d(in_channels,latent_channels,3,2,1); self.decoder=nn.ConvTranspose3d(latent_channels,in_channels,4,2,1)
    def encode(self,x): return self.encoder(x)
    def decode(self,z): return self.decoder(z).clamp(-1,1)
