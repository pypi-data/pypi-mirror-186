# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['trill', 'trill.utils']

package_data = \
{'': ['*'], 'trill': ['data/*']}

install_requires = \
['GitPython>=3.1.29,<4.0.0',
 'biotite>=0.35.0,<0.36.0',
 'datasets>=2.7.1,<3.0.0',
 'deepspeed>=0.7.6,<0.8.0',
 'fair-esm>=2.0.0,<3.0.0',
 'fairscale>=0.4.13,<0.5.0',
 'pandas>=1.5.2,<2.0.0',
 'pyfiglet>=0.8.post1,<0.9',
 'pytest>=7.2.0,<8.0.0',
 'transformers>=4.25.1,<5.0.0']

entry_points = \
{'console_scripts': ['trill = trill.trill_main:cli']}

setup_kwargs = {
    'name': 'trill-proteins',
    'version': '0.2.4',
    'description': 'Sandbox (in progress) for Computational Protein Design',
    'long_description': '                              _____________________.___.____    .____     \n                              \\__    ___/\\______   \\   |    |   |    |    \n                                |    |    |       _/   |    |   |    |    \n                                |    |    |    |   \\   |    |___|    |___ \n                                |____|    |____|_  /___|_______ \\_______ \\\n                                                 \\/            \\/       \\/\n\n[![pypi version](https://img.shields.io/pypi/v/trill-proteins)](https://pypi.org/project/trill-proteins)\n![status](https://github.com/martinez-zacharya/TRILL/workflows/CI/badge.svg)\n# TRILL\n**TR**aining and **I**nference using the **L**anguage of **L**ife\n\n## Set-Up\n1. I recommend using a virtual environment with conda, venv etc.\n2. Run ```$ pip install trill-proteins torch pytorch-lightning```\n3. ```$ pip install pyg-lib torch-scatter torch-sparse torch-cluster torch-spline-conv torch-geometric -f https://data.pyg.org/whl/torch-1.13.0+cu117.html```\n\n## Examples\n\n### Default (Fine-tuning ESM2)\n  1. The default mode for TRILL is to just fine-tune the base esm2_t12_35M_UR50D model from FAIR with the query input.\n  ```\n  $ trill fine_tuning_ex 1 --query data/query.fasta\n  ```\n### Embed with base esm2_t12_35M_UR50D model\n  2. You can also embed proteins with just the base model from FAIR and completely skip fine-tuning. The output will be a CSV file where each row corresponds to a single protein with the last column being the fasta header.\n  ```\n  $ trill base_embed 1 --query data/query.fasta --noTrain\n  ```\n### Embedding with a custom pre-trained model\n  3. If you have a pre-trained model, you can use it to embed sequences by passing the path to --preTrained_model. \n  ```\n  $ trill pre_trained 1 --query data/query.fasta --preTrained_model /path/to/models/pre_trained_model.pt\n  ```\n### Distributed Training/Inference\n  4. In order to scale/speed up your analyses, you can distribute your training/inference across many GPUs with a few extra flags to your command. You can even fit models that do not normally fit on your GPUs with sharding, CPU-offloading etc. Below is an example slurm batch submission file. The list of strategies can be found here (https://pytorch-lightning.readthedocs.io/en/stable/extensions/strategy.html). The example below utilizes 16 GPUs in total (4(GPUs) * 4(--nodes)) with Fully Sharded Data Parallel and the 650M parameter ESM2 model.\n  ```shell\n  #!/bin/bash\n  #SBATCH --time=8:00:00   # walltime\n  #SBATCH --ntasks-per-node=4\n  #SBATCH --nodes=4 # number of nodes\n  #SBATCH --gres=gpu:4 # number of GPUs\n  #SBATCH --mem-per-cpu=60G   # memory per CPU core\n  #SBATCH -J "tutorial"   # job name\n  #SBATCH --mail-user="" # change to your email\n  #SBATCH --mail-type=BEGIN\n  #SBATCH --mail-type=END\n  #SBATCH --mail-type=FAIL\n  #SBATCH --output=%x-%j.out\n  master_addr=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1)\n  export MASTER_ADDR=$master_addr\n  export MASTER_PORT=13579\n  \n  srun trill distributed_example 4 --query data/query.fasta --nodes 4 --strategy fsdp --model esm2_t33_650M_UR50D\n  ```\n  You can then submit this job with:\n  ```\n  $ sbatch distributed_example.slurm\n  ```\n  More examples for distributed training/inference without slurm coming soon!\n  \n### Generating protein sequences using inverse folding with ESM-IF1\n  5. When provided a protein backbone structure (.pdb, .cif), the IF1 model is able to predict a sequence that might be able to fold into the input structure. The example input are the backbone coordinates from DWARF14, a rice hydrolase. For every chain in the structure, 2 in 4ih9.pdb, the following command will generate 3 sequences. In total, 6 sequences will be generated.\n  ```\n  $ trill IF_Test 1 --query data/4ih9.pdb --if1 --genIters 3\n  ```\n  \n### Generating Proteins using ProtGPT2\n  6. You can also generate synthetic proteins using ProtGPT2. The command below generates 5 proteins with a max length of 100. The default seed sequence is "M", but you can also change this. Check out the command-line arguments for more details.\n  ```\n  $ trill Gen_ProtGPT2 1 --protgpt2 --gen --max_length 100 --num_return_sequences 5\n  ```\n  \n### Fine-Tuning ProtGPT2\n  7. In case you wanted to generate certain "types" of proteins, below is an example of fine-tuning ProtGPT2 and then generating proteins with the fine-tuned model. \n  ```\n  $ trill FineTune 2 --protgpt2 --epochs 100\n  ```\n  ```\n  $ trill Gen_With_FineTuned 1 --protgpt2 --gen --preTrained_model FineTune_ProtGPT2_100.pt\n  ```\n\n## Arguments\n\n### Positional Arguments:\n1. name (Name of run)\n2. GPUs (Total # of GPUs requested for each node)\n\n### Optional Arguments:\n- -h, --help (Show help message)\n- --query (Input file. Needs to be either protein fasta (.fa, .faa, .fasta) or structural coordinates (.pdb, .cif))\n- --nodes (Total number of computational nodes. Default is 1)\n- --lr (Learning rate for adam optimizer. Default is 0.0001)\n- --epochs (Number of epochs for fine-tuning transformer. Default is 20)\n- --noTrain (Skips the fine-tuning and embeds the query sequences with the base model)\n- --preTrained_model (Input path to your own pre-trained ESM model)\n- --batch_size (Change batch-size number for fine-tuning. Default is 1)\n- --model (Change ESM model. Default is esm2_t12_35M_UR50D. List of models can be found at https://github.com/facebookresearch/esm)\n- --strategy (Change training strategy. Default is None. List of strategies can be found at https://pytorch-lightning.readthedocs.io/en/stable/extensions/strategy.html)\n- --logger (Enable Tensorboard logger. Default is None)\n- --if1 (Utilize Inverse Folding model \'esm_if1_gvp4_t16_142M_UR50\' to facilitate fixed backbone sequence design. Basically converts protein structure to possible sequences)\n- --temp (Choose sampling temperature. Higher temps will have more sequence diversity, but less recovery of the original sequence for ESM_IF1)\n- --genIters (Adjust number of sequences generated for each chain of the input structure for ESM_IF1)\n- --LEGGO (Use deepspeed_stage_3_offload with ESM. Will be removed soon...)\n- --profiler (Utilize PyTorchProfiler)\n- --protgpt2 (Utilize ProtGPT2. Can either fine-tune or generate sequences)\n- --gen (Generate protein sequences using ProtGPT2. Can either use base model or user-submitted fine-tuned model)\n- --seed_seq (Sequence to seed ProtGPT2 Generation)\n- --max_length (Max length of proteins generated from ProtGPT)\n- --do_sample (Whether or not to use sampling ; use greedy decoding otherwise)\n- --top_k (The number of highest probability vocabulary tokens to keep for top-k-filtering)\n- --repetition_penalty (The parameter for repetition penalty. 1.0 means no penalty)\n- --num_return_sequences (Number of sequences for ProtGPT2 to generate)\n\n## Misc. Tips\n\n- Make sure there are no "\\*" in the protein sequences\n- Don\'t run jobs on the login node, only submit jobs with sbatch or srun on the HPC\n- Caltech HPC Docs https://www.hpc.caltech.edu/documentation\n',
    'author': 'Zachary Martinez',
    'author_email': 'martinez.zacharya@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/martinez-zacharya/TRILL',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
