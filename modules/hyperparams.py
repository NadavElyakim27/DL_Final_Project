r"""
This module is used to determine the parameters of the model.
"""


def part1_rnn_hyperparams():
    hypers = dict(
        batch_size=0,
        seq_len=0,
        h_dim=0,
        n_layers=0,
        dropout=0,
        learn_rate=0.0,
        lr_sched_factor=0.0,
        lr_sched_patience=0,
    )

    hypers['batch_size'] = 1000 
    hypers['seq_len'] = 60
    hypers['h_dim'] = 512
    hypers['n_layers'] = 3
    hypers['dropout'] = 0.2
    hypers['learn_rate'] = 0.001
    hypers['lr_sched_factor'] = 0.01
    hypers['lr_sched_patience'] = 4
    return hypers


def part1_generation_params():

    start_seq = "once upon a time"
    temperature = 0.0001

    return start_seq, temperature

