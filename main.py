import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Novelty detection algorithms evaluation')
    parser.add_argument('--data', default="MNIST",
                        help='dataset information, select from ["MNIST", "F-MNIST", "CIFAR-10", "MVTec-AD"] ')
    parser.add_argument('--model', default="RD4AD",
                        help='dataset information, select from ["RD4AD", "patchcore", "patchcore_resnet50"] ')
    parser.add_argument('--mode', default="train",
                        help='train or test')
    parser.add_argument('--weight', default=None,
                        help='weight file')
    args = parser.parse_args()
    
    data = args.data
    model = args.model
    mode = args.mode

    num_of_classes = {
        "MNIST": 10, "F-MNIST": 10, "CIFAR-10": 10, "MVTec-AD": 15
    }


    if mode == 'train':
        if model in ["RD4AD", "patchcore", "patchcore_resnet50"]:
            for normal_cls in range(num_of_classes[data]):
                os.system(f'python anomalib/tools/train.py --config config/{model}/{data}/{model}_{data}_{normal_cls}.yaml')
    
    elif mode == 'test':
        if model in ["RD4AD", "patchcore", "patchcore_resnet50"]:
            for normal_cls in range(num_of_classes[data]):
                os.system(f'python anomalib/tools/test.py --model {model} --config config/{model}/{data}/{model}_{data}_{normal_cls}_test.yaml --weight_file {results/{model}_{data}_{normal_cls}/{model}/{data}/run/weights/lightning/model.ckpt}')s
