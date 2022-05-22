import argparse
import time
import os


def pred_test(input_file, models):
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    output_file = 'result' + now
    print("input_file"+input_file)

    if(models == 'CNCI' or models == 'cnci'):
        os.path.join('data/test.fa')
        com = 'python2.7 CNCI.py -f '+input_file+' -g -o ' + \
            output_file + ' -m ve -p 8 -d hg19.2bit'
        print(com)
        os.system('cd ../../CNCI-master')
        os.system(com)


parser = argparse.ArgumentParser(description='Pred lncRNA')
parser.add_argument('--input', '-i', help='test_input_file', required=True)
parser.add_argument('--models', '-m', help='select_models', required=True)
# 可能会有spieces，后面再加

args = parser.parse_args()


if __name__ == "__main__":
    try:
        pred_test(args.input, args.models)
    except Exception as e:
        print(e)
