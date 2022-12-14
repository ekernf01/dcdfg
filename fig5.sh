conda activate dcdfg
for data in small # control cocult ifn
do
for model in mlplr # linearlr linear 
do
    python -u run_perturbseq_linear.py \
        --data-path ${data} \
        --reg-coeff 0.001 \
        --constraint-mode spectral_radius \
        --lr 0.01 \
        --model ${model} \
        --save-to prediction/${data}/${model} \
        --num-train-epochs 3000 \

done
done
