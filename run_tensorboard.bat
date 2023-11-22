@echo off
REM 初始化Anaconda环境
CALL D:\Programming\Anaconda3\Scripts\activate.bat
REM 激活conda环境
CALL activate pytorch
REM 启动Jupyter Notebook
CALL python -m tensorboard.main --logdir='small_grabage/'
REM 保持窗口打开
pause