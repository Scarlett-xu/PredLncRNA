#!bin/bash
current_date=$(date +%Y-%m-%d --date="$1 day")
echo "----------------"
echo $current_date
rm /home/xxr/lncRNAwebtool/inputfiles/*
echo "已清空inputfiles"
mv /home/xxr/lncRNAwebtool/predict_results/notexist ~
rm -rf /home/xxr/lncRNAwebtool/predict_results/*
mv ~/notexist /home/xxr/lncRNAwebtool/predict_results/
