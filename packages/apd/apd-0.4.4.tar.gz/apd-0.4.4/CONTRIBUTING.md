# Contributing guidelines

## Creating a development environment

```bash
git clone ssh://git@gitlab.cern.ch:7999/lhcb-dpa/analysis-productions/apd.git
cd apd
mamba create --name apd-dev requests requests-kerberos beautifulsoup4 click click-log ipython black pre-commit pytest
conda activate apd-dev
pip install -e .[testing]
pre-commit install
curl -o lb-check-copyright "https://gitlab.cern.ch/lhcb-core/LbDevTools/raw/master/LbDevTools/SourceTools.py?inline=false"
chmod +x lb-check-copyright
```

## Running the tests

```bash
pre-commit run --all-files
pytest
```
