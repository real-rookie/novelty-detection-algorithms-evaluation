import os
import sys
import yaml

import torch
from torch.utils.data import DataLoader
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from data import TrainDataset, ValidDataset, get_train_transforms, get_valid_transforms

from fanogan.train_encoder_izif import train_encoder_izif


def main(opt):
    if type(opt.seed) is int:
        torch.manual_seed(opt.seed)
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    pipeline = [transforms.Resize([opt.img_size]*2),
                transforms.RandomHorizontalFlip()]
    if opt.channels == 1:
        pipeline.append(transforms.Grayscale())
    pipeline.extend([transforms.ToTensor(),
                     transforms.Normalize([0.5]*opt.channels, [0.5]*opt.channels)])

    transform = transforms.Compose(pipeline)
    dataset = TrainDataset(data=opt.data, transform=transform)
    train_dataloader = DataLoader(dataset, batch_size=opt.batch_size,
                                  shuffle=True, num_workers=8)

    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    from mvtec_ad.model import Generator, Discriminator, Encoder

    generator = Generator(opt)
    discriminator = Discriminator(opt)
    encoder = Encoder(opt)

    train_encoder_izif(opt, generator, discriminator, encoder,
                       train_dataloader, device)


"""
The code below is:
Copyright (c) 2018 Erik Linder-Norén
Licensed under MIT
(https://github.com/eriklindernoren/PyTorch-GAN/blob/master/LICENSE)
"""


if __name__ == "__main__":
    import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--force_download", "-f", action="store_true",
    #                     help="flag of force download")
    # parser.add_argument("--n_epochs", type=int, default=200, #!!! 200
    #                     help="number of epochs of training")
    # parser.add_argument("--batch_size", type=int, default=32,
    #                     help="size of the batches")
    # parser.add_argument("--lr", type=float, default=0.0002,
    #                     help="adam: learning rate")
    # parser.add_argument("--b1", type=float, default=0.5,
    #                     help="adam: decay of first order momentum of gradient")
    # parser.add_argument("--b2", type=float, default=0.999,
    #                     help="adam: decay of first order momentum of gradient")
    # parser.add_argument("--latent_dim", type=int, default=100,
    #                     help="dimensionality of the latent space")
    # parser.add_argument("--img_size", type=int, default=224,
    #                     help="size of each image dimension")
    # parser.add_argument("--channels", type=int, default=3,
    #                     help="number of image channels (If set to 1, convert image to grayscale)")
    # parser.add_argument("--n_critic", type=int, default=5,
    #                     help="number of training steps for "
    #                          "discriminator per iter")
    # parser.add_argument("--sample_interval", type=int, default=400,
    #                     help="interval betwen image samples")
    # parser.add_argument("--seed", type=int, default=None,
    #                     help="value of a random seed")
    # opt = parser.parse_args()

    parser = argparse.ArgumentParser(description='Training defect detection as described in the CutPaste Paper.')
    parser.add_argument('--data', default="camelyon",
                        help='MVTec defection dataset type to train seperated by , (default: "all": train all defect types)')
    args = parser.parse_args()

    config_path = f"config/{args.data}_fanogan.yaml"
    print(f"reading config {config_path}...")
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    print(config)
    for key, value in config.items():
        parser.add_argument(f'--{key}', default=value)
    opt = parser.parse_args()
    print(opt)

    main(opt)
