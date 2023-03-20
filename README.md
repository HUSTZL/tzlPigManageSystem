# PigManageSystem

Ubuntu 20.04

注意修改各个文件中的数据库地址修改为对应地址

设计测试用例时要注意数据库的上下文环境

`
    
    sudo apt-get install sqlite3

    git clone git@github.com:HUSTZL/PigManageSystem.git

    cd PigManageSystem

    conda create -n PigManageSystem python=3.8

    conda activate PigManageSystem

    pip install -r requirement.yaml

    cd src
    
    python rebuild_database.py

    python main.py
`