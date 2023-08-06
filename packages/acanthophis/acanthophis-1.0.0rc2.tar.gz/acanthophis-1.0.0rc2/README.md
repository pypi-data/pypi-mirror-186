# Acanthophis

A reusable, comprehensive, opinionated plant hologenomics and variant calling pipeline in Snakemake

<img src=".github/logo.jpg" width="320">

## Installation & Use

```bash
# create conda env, activate it
conda create -n someproject python snakemake pip
conda activate someproject

# install acanthophis itself
pip install acanthophis

# generate a workspace. This copies all files the workflow will need to your workspace directory.
acanthophis-init /path/to/someproject/

# edit config.yml to suit your project. Hopefully this config file documents
# all options available in an understandable fashion. If not, please raise an
# issue on github.

vim config.yml

# run snakemake
snakemake -j 16 -p --use-conda --conda-frontend mamba --ri
# or on a cluster, see acanthophis-init --list-available-profiles
snakemake --profile ./ebio-cluster/
```

Until I write the documentation, please see [the example workflow](acanthophis/template/).
It should contain a fully working example workflow.


## About & Authors

This is an amalgamation of several pipelines developed between the [Weigel Group, MPI DB, Tübingen, DE](https://weigelworld.org), the [Warthmann Group, IAEA/FAO PBGL, Seibersdorf, AT](http://warthmann.com) and the [Borevitz Group, ANU, Canberra, AU](https://borevitzlab.anu.edu.au). This amalgamation authored by Dr. K. D. Murray, original code primary by K. D. Murray, Norman Warthmann, and Ilja Bezrukov, with contributions from others at the aforementioned institutes.
