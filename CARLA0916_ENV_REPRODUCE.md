# CARLA 0.9.16 / TCP0916 environment reproduction

Generated files:

1. `environment_carla0916_full_lock.yml`
   - Single-file, old-yml-style export.
   - Conda packages are pinned as `name=version=build`.
   - Pip packages are pinned as `package==version`.
   - Does not include `prefix`, because that path is machine-specific.

2. `requirements_carla0916_clean.txt`
   - Clean pip-only requirements extracted from `environment_carla0916_locked.yml`.
   - Prefer this over raw `pip freeze` if the raw file contains local `file:///...` paths or ROS/system packages.

Recommended install method, if you want a single yml:

```bash
conda env create -f environment_carla0916_full_lock.yml --name TCP0916
conda activate TCP0916
```

Most exact install method, if you want minimal conda solving:

```bash
conda create -n TCP0916 --file conda_explicit_carla0916.txt
conda activate TCP0916
pip install -r requirements_carla0916_clean.txt
```

Note:
- `conda_explicit_carla0916.txt` is platform-specific: linux-64.
- It is usually the fastest and most reproducible conda install format.
- The yml format is easier to read and edit, but it still may require conda solving.
