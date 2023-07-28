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
            os.system(f'python anomalib/tools/train.py --config config/{model}/{data}/{model}_{data}_textures_to_objects.yaml')
            os.system(f'python anomalib/tools/train.py --config config/{model}/{data}/{model}_{data}_objects_to_textures.yaml')
    elif mode == 'test':
        if model in ["RD4AD", "patchcore", "patchcore_resnet50"]:
            if model == "RD4AD":
                os.system(f'python anomalib/tools/test.py --model {model} --config config/{model}/{data}/{model}_{data}_textures_to_objects.yaml --weight_file results/{model}_{data}_textures_to_objects/reverse_distillation/{data}_textures_to_objects/run/weights/lightning/model.ckpt')
                os.system(f'python anomalib/tools/test.py --model {model} --config config/{model}/{data}/{model}_{data}_objects_to_textures.yaml --weight_file results/{model}_{data}_objects_to_textures/reverse_distillation/{data}_objects_to_textures/run/weights/lightning/model.ckpt')
            else:
                os.system(f'python anomalib/tools/test.py --model {model} --config config/{model}/{data}/{model}_{data}_textures_to_objects.yaml --weight_file results/{model}_{data}_textures_to_objects/{model}/{data}_textures_to_objects/run/weights/lightning/model.ckpt')
                os.system(f'python anomalib/tools/test.py --model {model} --config config/{model}/{data}/{model}_{data}_objects_to_textures.yaml --weight_file results/{model}_{data}_objects_to_textures/{model}/{data}_objects_to_textures/run/weights/lightning/model.ckpt')
