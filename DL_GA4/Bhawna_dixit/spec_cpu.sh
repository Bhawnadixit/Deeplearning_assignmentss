#!/bin/bash
#PBS -N Spec_cpu_run2
#PBS -l nodes=1:ppn=20
#PBS -l walltime=00:05:00
#PBS -o out_spec_cpu2.log
#PBS -e err_spec_cpu2.log
#PBS -M bhawna.dixit@vub.be
#PBS -m abe

#module load Python/3.7.4-GCCcore-8.3.0
source activate /user/brussel/102/vsc10271/miniconda3/envs/bhawna

cd $PBS_O_WORKDIR

python spec_cpu2.py

echo "I am done"