#!bin/bash

# 执行该脚本的代码: bash predict_cnci.sh ve > predictCNCI.log
# $1 inputfile $2=ve或者pl 
# 预测路径
PREDICT_PATH=/home/xxr/lncRNAwebtool/Predpackage/CNCI-master
# 输出结果路径
RESULT_PATH=/home/xxr/lncRNAwebtool/Predpackage/result
# 获取当天时间
currentdate=$(date "+%Y-%m-%d")
# 建立日期文件夹
if ! [ -d $RESULT_PATH/$currentdate ]
then
    mkdir $RESULT_PATH/$currentdate
    echo "已建立文件夹：$currentdate"
else
    echo "文件夹已存在：$currentdate"
fi
# 建立cnci文件夹
if ! [ -d $RESULT_PATH/$currentdate/cnci ]
then
    mkdir $RESULT_PATH/$currentdate/cnci
    echo "已建立文件夹：$currentdate/cnci"
else
    echo "文件夹已存在：$currentdate/cnci"
fi


# 清空结果文件夹中的文件
rm -rf $RESULT_PATH/$currentdate/cnci/*
echo "已清空当前文件夹中的文件"
# 建立结果文件
# -f:input files -g:gtf files -o:output path -m:物种选择，后面待改
cd $PREDICT_PATH
echo "python2.7 $PREDICT_PATH/CNCI.py -f test.fa -o $RESULT_PATH/$currentdate -m $1 -p 8"
python2.7 $PREDICT_PATH/CNCI.py -f test.fa -o $RESULT_PATH/$currentdate/cnci -m $1 -p 8
# 删除自动生成的log文件
rm -rf $RESULT_PATH/$currentdate/cnci/*.log