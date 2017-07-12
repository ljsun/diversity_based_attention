import sys

class Config:
    """ Config class represents the hyperparameters in a single
        object
    """ 
    def __init__(self, filename="../config"):

        """ Initialize the object with the parameters.

        Args:
            learning_rate : Learning rate for the optimizer
            embedding_size: dimensions of word embeddings
            hidden_size   : dimensions of hidden state of rnn cell
            batch_size    : batch size
            max_epochs    : Number of epochs to be run
            early_stop    : early stop

            max_sequence_length_content: Max length to be set for encoder inputs
            max_sequence_length_title  : Max length to be set for decoder inputs
            max_sequence_length_query  : Max length to be set for query inputs
        """

        f = open(filename, "r")
        config_dir = {}
        for line in f:
        	 key, value = line.split("=")

        	 if key == "learning_rate":
        	 	config_dir[key] = float(value)
        	 elif value.isdigit():
        	 	config_dir[key] = int(value)
        	 else:
        	 	config_dir[key] = value

        self.config_dir = config_dir
        self.learning_rate  = learning_rate
        self.embedding_size = embedding_size
        self.max_sequence_length_content = max_sequence_length_content
        self.max_sequence_length_title   = max_sequence_length_title
        self.max_sequence_lenght_query   = max_sequence_length_query
        self.hidden_size = hidden_size
        self.batch_size = batch_size
        self.max_epochs = max_epochs
        self.outdir     = outdir
        self.emb_tr     = emb_tr
        self.early_stop = early_stop
