import copy

num_of_classes = {
    "MNIST": 10,
    "FashionMNIST": 10,
    "CIFAR10": 10,
    "MVTec-AD": 15
}
model = "RD4AD"
sample_data = "MNIST"
filename_old = f"{sample_data}/{model}_{sample_data}_0.yaml"
for data in ["MNIST", "FashionMNIST", "CIFAR10", "MVTec-AD"]:
    with open(filename_old, "r") as original:
        o_text = original.read()
        for i in range(0, num_of_classes[data]):
            filename_new = f"{data}/{model}_{data}_{i}.yaml"
            with open (filename_new, "w") as new:
                original_text = copy.deepcopy(o_text)
                original_text = original_text.replace(f"name: {sample_data}_0", f"name: {data}_{i}")
                original_text = original_text.replace(f"path: ../datasets/{sample_data}/images/", f"path: ../datasets/{data}/images/")
                original_text = original_text.replace("normal_dir: train/0", f"normal_dir: train/{i}")
                original_text = original_text.replace("abnormal_dir: test/0/novel", f"abnormal_dir: test/{i}/novel")
                original_text = original_text.replace("normal_test_dir: test/0/normal", f"normal_test_dir: test/{i}/normal")
                original_text = original_text.replace("seed: 0", f"seed: {i}")
                original_text = original_text.replace(f"path: ./results/{model}_{sample_data}_0", f"path: ./results/{model}_{data}_{i}")
                new.write(original_text)
