import argparse,torch
from openvideo.models.video_dit import VideoDiT
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--steps",type=int,default=20); a=ap.parse_args()
    device="cuda" if torch.cuda.is_available() else "cpu"
    m=VideoDiT(latent_channels=4,hidden_size=128,depth=2,heads=4).to(device)
    opt=torch.optim.AdamW(m.parameters(),lr=1e-4)
    for i in range(a.steps):
        x=torch.randn(1,4,4,8,8,device=device); y=torch.randn_like(x)
        loss=(m(x)-y).square().mean(); opt.zero_grad(); loss.backward(); opt.step()
        print(i+1,float(loss))
if __name__=="__main__": main()
