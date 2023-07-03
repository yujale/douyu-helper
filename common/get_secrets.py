import os
from common.dirs import *


def get_secrets(item):
    os.environ.setdefault('COOKIES', 'dy_did=7e820adc9c57ced83416adf900021601; acf_did=7e820adc9c57ced83416adf900021601; dy_teen_mode=%7B%22uid%22%3A%22273297400%22%2C%22status%22%3A0%2C%22birthday%22%3A%22%22%2C%22password%22%3A%22%22%7D; dy_did=7e820adc9c57ced83416adf900021601; PHPSESSID=5dghaura6i2rpvbf6ub015scb4; acf_auth=2aa2tQrBinrt5Q1qVrUORPenWFqHBCa4ax2b0QMtR3nMPEqhOA%2FYI98cFEoXVRDR1HiLMNYlaibXNXq4xt9lm7ondslCgtzyq%2BQiejU%2BvxofbBvPtLTPcMc; dy_auth=71b8FTBbN4jhAUrxxU2ejakcYY%2F8Ms7M1AMs5ziTuMyN%2BxoW%2FaLcQHmqLyltgpweuWfrMRz9dxlrCNSE4ibxde5UgWC5AeDYrEbsxTlwyOjhhqZe6zBm1yk; wan_auth37wan=f658691890aemvADXArbEjjwVX7fdOEb%2BPcLLmoubHnZp0QCxhYNUBFCeLlAx5l5D1knUmi6RAY3PCd7p%2BHoWVCiYFSeJqNpyYlVvGZeZ1ZBdeDJvoI; acf_uid=273297400; acf_username=273297400; acf_nickname=%E5%8A%AA%E5%8A%9B%E7%9A%84it%E5%B0%8F%E8%83%96%E5%AD%90; acf_own_room=0; acf_groupid=1; acf_phonestatus=1; acf_avatar=https%3A%2F%2Fapic.douyucdn.cn%2Fupload%2Favatar%2Fdefault%2F11_; acf_ct=0; acf_ltkid=49270830; acf_biz=1; acf_stk=845af64dd92d0619; frm=zb-cjdm2; ext=1%257C1258%257C90%257Czb-cjdm2; fdata=zbj%7C%7C%3Bzb-cjdm2%7C%7C%3B%7C%7C%3B53716%7C%7C%3B5116%7C%7C%3B33382%7C%7C%3B1%7C1258%7C90%7Czb-cjdm2; loginrefer=pt_ik8bleek3in3; acf_ccn=2fccce8bd7f7ff362a29204fa211fbdb')
    return os.environ[item]


if __name__ == '__main__':
    print(get_secrets('COOKIES'))
