> [!IMPORTANT]
> 🌟 Stay up to date at [opendrivelab.com](https://opendrivelab.com/#news)!

# TCP—— 面向端到端自动驾驶的轨迹引导控制预测：一种简洁且性能强劲的基线模型

![teaser](assets/teaser_.png)

> Trajectory-guided Control Prediction for End-to-end Autonomous Driving: A Simple yet Strong Baseline  
> [Penghao Wu*](https://scholar.google.com/citations?user=9mssd5EAAAAJ&hl=en), [Xiaosong Jia*](https://jiaxiaosong1002.github.io/), [Li Chen*](https://scholar.google.com/citations?user=ulZxvY0AAAAJ&hl=en), [Junchi Yan](https://thinklab.sjtu.edu.cn/), [Hongyang Li](https://lihongyang.info/), [Yu Qiao](http://mmlab.siat.ac.cn/yuqiao/)    
>  - [arXiv Paper](https://arxiv.org/abs/2206.08129), NeurIPS 2022
>  - [Blog in Chinese](https://zhuanlan.zhihu.com/p/532665469)

	
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/trajectory-guided-control-prediction-for-end/autonomous-driving-on-carla-leaderboard)](https://paperswithcode.com/sota/autonomous-driving-on-carla-leaderboard?p=trajectory-guided-control-prediction-for-end)

本仓库为论文《面向端到端自动驾驶的轨迹引导控制预测：一种简洁且性能强劲的基线模型》的开源代码。(https://arxiv.org/abs/2206.08129).


TCP 是一套简洁的统一框架，将轨迹预测与控制预测相结合，应用于端到端自动驾驶任务。  本方法于 2022 年 6 月 17 日开源发布时，已在 CARLA 自动驾驶排行榜 上取得当前最优性能；仅以单目相机作为输入，在驾驶得分与违规惩罚两项指标上均位列全球第一。 


## Setup
在carla官网下载 CARLA 0.9.16.1 (https://carla.readthedocs.io/en/latest/start_quickstart/)
```
mkdir carla
cd carla
tar -xf CARLA_0.9.10.1.tar.gz
tar -xf AdditionalMaps_0.9.10.1.tar.gz
rm CARLA_0.9.10.1.tar.gz
rm AdditionalMaps_0.9.10.1.tar.gz
cd ..
```

克隆本仓库并搭建运行环境

```
git clone https://github.com/OpenPerceptionX/TCP.git
cd TCP
conda create -n TCP0916 --file conda_explicit_carla0916.txt
conda activate TCP0916
pip install -r requirements_carla0916_clean.txt
```

这个方式比 yml 更接近“照着原环境装”，因为 conda_explicit_carla0916.txt 里面是精确 URL，不是让 conda 重新求解。

激活虚拟环境后，需先配置PYTHNONPATH
```
export PYTHONPATH=$PYTHONPATH:PATH_TO_TCP
```

## 数据集

下载数据集 [Huggingface](https://huggingface.co/datasets/craigwu/tcp_carla_data) (将部分与命令合并 `cat tcp_carla_data_part_* > tcp_carla_data.zip`) or [GoogleDrive](https://drive.google.com/file/d/1HZxlSZ_wUVWkNTWMXXcSQxtYdT7GogSm/view?usp=sharing) or [BaiduYun](https://pan.baidu.com/s/11xBZwAWQ3WxQXecuuPoexQ) (提取码 8174). 数据集总大小大约是115G，确保你有足够的空间。

## 模型训练
First, set the dataset path in ``TCP/config.py``.
Training:
```
python TCP/train.py --gpus NUM_OF_GPUS
```

## 数据采集
首先启动carla,
```
cd CARLA_ROOT
./CarlaUE4.sh --world-port=2000 -opengl
```
设置 carla 路径、路由文件、场景文件和数据路径以生成数据。 ``leaderboard/scripts/data_collection.sh``.

开始收集数据

```
sh leaderboard/scripts/data_collection.sh
```
数据收集过程结束后，运行并过滤无效数据并打包数据 `tools/filter_data.py` and `tools/gen_data.py` 进行训练。

## 评估
首先，启动Carla服务器，
```
cd CARLA_ROOT
./CarlaUE4.sh --world-port=2000 -opengl
```
在``leaderboard/scripts/run_evaluation.sh``设置 carla 路径、路由文件、场景文件、模型 ckpt 和数据路径进行评估。 

开始评估

```
sh leaderboard/scripts/run_evaluation.sh
```

## Citation

If you find our repo or our paper useful, please use the following citation:

```
@inproceedings{wu2022trajectoryguided,
 title={Trajectory-guided Control Prediction for End-to-end Autonomous Driving: A Simple yet Strong Baseline}, 
 author={Penghao Wu and Xiaosong Jia and Li Chen and Junchi Yan and Hongyang Li and Yu Qiao},
 booktitle={NeurIPS},
 year={2022},
}
```

## License
All code within this repository is under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

## Acknowledgements

Our code is based on several repositories:
- [Transfuser](https://github.com/autonomousvision/transfuser)
- [Roach](https://github.com/zhejz/carla-roach)
- [CARLA Leaderboard](https://github.com/carla-simulator/leaderboard)
- [Scenario Runner](https://github.com/carla-simulator/scenario_runner)

