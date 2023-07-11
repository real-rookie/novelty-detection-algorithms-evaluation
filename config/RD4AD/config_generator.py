import copy

num_of_classes = {
    "MNIST": 10,
    "FashionMNIST": 10,
    "CIFAR10": 10,
    "MVTec-AD": 15
}

for data in ["MNIST", "FashionMNIST", "CIFAR10", "MVTec-AD"]:
    filename_old = f"{data}/RD4AD_{data}_0.yaml"
    with open(filename_old, "r") as original:
        o_text = original.read()
        for i in range(1, num_of_classes[data]):
            filename_new = f"{data}/RD4AD_{data}_{i}.yaml"
            with open (filename_new, "w") as new:
                original_text = copy.deepcopy(o_text)
                original_text = original_text.replace(f"name: {data}_0", f"name: {data}_{i}")
                original_text = original_text.replace("normal_dir: train/0", f"normal_dir: train/{i}")
                original_text = original_text.replace("abnormal_dir: cv/0/novel", f"abnormal_dir: cv/{i}/novel")
                original_text = original_text.replace("normal_test_dir: cv/0/normal", f"normal_test_dir: cv/{i}/normal")
                original_text = original_text.replace("seed: 0", f"seed: {i}")
                original_text = original_text.replace(f"path: ./results/RD4AD_{data}_0", f"path: ./results/RD4AD_{data}_{i}")
                new.write(original_text)

    filename_old = f"{data}/RD4AD_{data}_0_test.yaml"
    with open(filename_old, "r") as original:
        o_text = original.read()
        for i in range(1, num_of_classes[data]):
            filename_new = f"{data}/RD4AD_{data}_{i}_test.yaml"
            with open (filename_new, "w") as new:
                original_text = copy.deepcopy(o_text)
                original_text = original_text.replace(f"name: {data}_0", f"name: {data}_{i}")
                original_text = original_text.replace("normal_dir: train/0", f"normal_dir: train/{i}")
                original_text = original_text.replace("abnormal_dir: test/0/novel", f"abnormal_dir: test/{i}/novel")
                original_text = original_text.replace("normal_test_dir: test/0/normal", f"normal_test_dir: test/{i}/normal")
                original_text = original_text.replace("seed: 0", f"seed: {i}")
                original_text = original_text.replace(f"path: ./results/RD4AD_{data}_0", f"path: ./results/RD4AD_{data}_{i}")
                new.write(original_text)