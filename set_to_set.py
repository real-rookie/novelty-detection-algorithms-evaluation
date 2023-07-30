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
    weight = args.weight

    if mode == 'train':
        if model in ["RD4AD", "patchcore", "patchcore_resnet50"]:
            for dataset in ["MNIST", "FashionMNIST", "CIFAR10"]:
                os.system(f'python anomalib/tools/train.py --config config/{model}/{dataset}/{model}_{dataset}_MVTec-AD.yaml')
            os.system(f'python anomalib/tools/train.py --config config/{model}/MVTec-AD/{model}_MVTec-AD_MNIST.yaml')
    elif mode == 'test':
        if model in ["RD4AD", "patchcore", "patchcore_resnet50"]:
            if model == "RD4AD":
                for dataset_train in ["MNIST", "FashionMNIST", "CIFAR10", "MVTec-AD"]:
                    for dataset_test in ["MNIST", "FashionMNIST", "CIFAR10", "MVTec-AD"]:
                        if dataset_train != dataset_test:
                            if dataset_train == "MVTec-AD":
                                os.system(f'python anomalib/tools/test.py --model {model} --config config/{model}/{dataset_train}/{model}_{dataset_train}_{dataset_test}.yaml --weight_file results/{model}_{dataset_train}_MNIST/reverse_distillation/{dataset_train}_MNIST/run/weights/lightning/model.ckpt')
                            else:
                                os.system(f'python anomalib/tools/test.py --model {model} --config config/{model}/{dataset_train}/{model}_{dataset_train}_{dataset_test}.yaml --weight_file results/{model}_{dataset_train}_MVTec-AD/reverse_distillation/{dataset_train}_MVTec-AD/run/weights/lightning/model.ckpt')

            else:
                os.system(f'python anomalib/tools/test.py --model {model} --config config/{model}/{data}/{model}_{data}_inter_set.yaml --weight_file results/{model}_{data}_inter_set/{model}/{data}_inter_set/run/weights/lightning/model.ckpt')
