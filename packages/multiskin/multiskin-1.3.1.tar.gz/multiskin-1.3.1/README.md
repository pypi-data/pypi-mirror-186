### Things to remember
1. Make sure under arm64 (check with `arch`).
2. If not under arm64, run: `env /usr/bin/arch -arm64 /bin/zsh`
3. Remove all (presumably wrong) reqs with: `pip freeze | xargs pip uninstall -y`
5. Latest pip: `pip install --ugprade pip`
4. Install requirements: `pip install -r requirements.txt`
5. Make sure you're logged in with `huggingface-cli login`
