# Wordle Helper.

This a small program which help solving the popular puzzle called wordle([Link](https://www.powerlanguage.co.uk/wordle/)). Program takes three optional inputs for each one of the colored clues. Here is an example of how it works. 

<div align=center><img src="img/1.PNG" height = "30%" width = "30%"/></div>
<div align=center><img src="img/2.PNG" height = "30%" width = "30%"/></div>

### Model Compression

Following commands can be used to reproduce the results presented in the paper. 

##### 1. Resnet56

| Flops         | Parameters      | Accuracy |
|---------------|-----------------|----------|
|89.80M(64.22%) | 0.32M(62.97%)   | 92.71%   | 

```shell
python run_cifar.py \
--jobid resnet56_test \
--arch resnet56 \
--dataset cifar10 \
--compress_rate :[6,4,4,6,4,4,4,4,4,4,4,4,4,13,4,10,6,4,4,12,18,16,4,15,4,16,4,12,7,13,4,15,4,18,4,12,4,32,26,36,16,32,13,29,23,32,16,36,10,23,13,20,10,13,7] \
--l2_weight 0.001 \
--add_bn True \
--epochs 120 \
--schedule 30 60 90 \
--lr 0.01
```
