from eICU_preprocessing.split_train_test import create_folder
from models.run_lstm import BaselineLSTM
from models.hyperparameter_scripts.eICU.channel_wise_lstm import get_hyperparam_config


if __name__=='__main__':
    c = get_hyperparam_config()
    c['dataset'] = 'MIMIC'
    c['no_diag'] = True
    log_folder_path = create_folder('models/experiments/hyperparameters/MIMIC', c.exp_name)
    channel_wise_lstm = BaselineLSTM(config=c,
                                     n_epochs=c.n_epochs,
                                     name=c.exp_name,
                                     base_dir=log_folder_path,
                                     explogger_kwargs={'folder_format': '%Y-%m-%d_%H%M%S{run_number}'})
    channel_wise_lstm.run()