modules = [
    "carla",
    "torch",
    "torchvision",
    "numpy",
    "cv2",
    "PIL",
    "yaml",
    "yacs",
    "tqdm",
    "skimage",
    "pandas",
    "scipy",
    "matplotlib",
    "gym",
    "py_trees",
    "leaderboard",
    "srunner",
]

for m in modules:
    try:
        mod = __import__(m)
        print(f"[OK] {m}")
    except Exception as e:
        print(f"[FAIL] {m}: {e}")
