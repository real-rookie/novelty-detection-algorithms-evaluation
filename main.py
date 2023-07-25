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
    parser.add_argument('--method', default="one_to_many",
                        help='["one_to_many", "inter_set", "set_to_set"]')
    parser.add_argument('--config', default="",
                        help="specify the config file")
    args = parser.parse_args()
    
    data = args.data
    model = args.model
    mode = args.mode
    method = args.method
    config = args.config

    num_of_classes = {
        "MNIST": 10, "FashionMNIST": 10, "CIFAR10": 10, "MVTec-AD": 15
    }


    if mode == 'train':
        if model in ["RD4AD", "patchcore", "patchcore_resnet50"]:
            if method == "one_to_many":
                for normal_cls in range(num_of_classes[data]):
                    os.system(f'python anomalib/tools/train.py --config config/{model}/{data}/{model}_{data}_{normal_cls}.yaml')
            elif method == "inter_set":
                if data == "MVTec-AD":
                    os.system(f'python anomalib/tools/train.py --config {config}')
                else:
                    os.system(f'python anomalib/tools/train.py --config config/{model}/{data}/{model}_{data}_inter_set.yaml')
    elif mode == 'test':
        if model in ["RD4AD", "patchcore", "patchcore_resnet50"]:
            if method == "one_to_many":
                for normal_cls in range(num_of_classes[data]):
                    if model == "RD4AD":
                        os.system(f'python anomalib/tools/test.py --model {model} --config config/{model}/{data}/{model}_{data}_{normal_cls}_test.yaml --weight_file results/{model}_{data}_{normal_cls}/reverse_distillation/{data}_{normal_cls}/run/weights/lightning/model.ckpt')
                    else:
                        os.system(f'python anomalib/tools/test.py --model {model} --config config/{model}/{data}/{model}_{data}_{normal_cls}_test.yaml --weight_file results/{model}_{data}_{normal_cls}/{model}/{data}_{normal_cls}/run/weights/lightning/model.ckpt')
            elif method == "inter_set":
                if model == "RD4AD":
                    if data == "MVTec-AD":
                        os.system(f'python anomalib/tools/test.py --model {model} --config {config}')
                    else:
                        os.system(f'python anomalib/tools/test.py --model {model} --config config/{model}/{data}/{model}_{data}_inter_set_test.yaml --weight_file results/{model}_{data}_inter_set/reverse_distillation/{data}_inter_set/run/weights/lightning/model.ckpt')
                else:
                    os.system(f'python anomalib/tools/test.py --model {model} --config config/{model}/{data}/{model}_{data}_inter_set_test.yaml --weight_file results/{model}_{data}_inter_set/{model}/{data}_inter_set/run/weights/lightning/model.ckpt')
