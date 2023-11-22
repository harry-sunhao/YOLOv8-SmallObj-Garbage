@echo off
REM 初始化Anaconda环境
CALL D:\Programming\Anaconda3\Scripts\activate.bat
REM 激活conda环境
CALL activate pytorch
REM 启动Jupyter Notebook
CALL jupyter notebook --NotebookApp.token='f425885e3f44deefa51613af98fea11694b2806e9628b070'
REM 保持窗口打开
pause
