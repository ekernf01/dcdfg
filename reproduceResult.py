import os
import torch

command = 'python run_perturbseq_linear.py --data-path ifn --num-train-epochs 600 --num-fine-epochs 100 --num-gpus {1 if torch.cuda.is_available() else 0} --num-modules 20 --train-batch-size 64'
savedir = 'prediction'

if not os.path.exists(savedir):
    os.makedirs(savedir)

    
# Hyperparameter sweep for DCDFG (search space described in Table 2)
for constraint_mode in ["spectral_radius", "exp"]:
    for lasso_coef in [-3, -2, -1, 0, 1, 2]:
        savepath = os.path.join(savedir, f"mlplr.{lasso_coef}.{constraint_mode}")
        full_command = command + f'--constraint-mode {constraint_mode} --reg-coeff {10**(lasso_coef)} --model mlplr --save-to {savepath}'
        print(full_command)
        if os.path.exists(savepath):
            continue
        os.system(full_command)


# DCDFG vs causal model baselines
for models in ["mlplr", "linearlr", "linear"]:
    savepath = os.path.join(savedir, f"{models}.-1.spectral_radius")
    full_command = command + f'--constraint-mode spectral_radius --reg-coeff 0.1 --model {models} --save-to {savepath}'
    print(full_command)
    if os.path.exists(savepath):
        continue
    os.system(full_command)
