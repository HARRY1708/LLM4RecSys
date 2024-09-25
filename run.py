import recbole
from recbole.quick_start import run_recbole

if __name__ == '__main__':
    parameter_dict = {
    'train_neg_sample_args': None,
    'data_path': "/Users/harkanwarsingh/Desktop/LLM4RecSys/",
    'dataset': 'Amazon_All_Beauty',
    'config_file_list': ['Amazon_All_Beauty.yaml'],
    'load_col': {'inter': ['user_id','item_id','rating','timestamp'] }
    }
    run_recbole(model='SASRec',dataset='Amazon_All_Beauty',config_dict=parameter_dict)