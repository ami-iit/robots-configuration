### SOME PARAMETERS OF THE NN ###

import torch

### SOME PARAMETERS OF THE NN ###

import torch

batch_size = 1000 # 114 #1024 #339  #220 #50     #179     #512
num_epochs = 8 #7 with other datasets
learning_rate = 0.0094023971181947206 # 5e-4  # 0.003946384047393205 # 0.001  
n_neurons = 256 #435 #1445 # 500 #1100 #1200 #1100 #850 #750 #500                       
n_layers = 2 #5                            # number of hidden layers of neurons
normalization = 1                       # 1 = standarization, 2 = euclidean, otherwise no normalization
initialization = 1                      # 1 = initialization of parameters of NN with xavier, 2 = normal distribution, 3 = uniform distribution
mean_stand_initialization = 0           # mean of the normal distribution for initialization of parameters of NN
std_stand_initialization = 0.05         # std of the normal distribution for initialization of parameters of NN
lim_inf_unif_initialization = -0.1      # lower bound of the uniform distribution for initialization of parameters of NN
lim_sup_unif_initialization = 0.1       # upper bound of the uniform distribution for initialization of parameters of NN
weight_centroidal = 0.0                 # weight of centroidal momentum in the loss function
weight_expected = 407.3938302752665                   # weight of expected sum of wrenches in the loss function
Sensor = 8                              # 1 = entire left foot, 2 = only front of left, 3 = only rear of left, 4 = entire right foot, 5 = only front of right, 6 = only rear of right, 7 = entire left leg, 8 = entire right leg, 9 = entire left arm, 10 = entire right arm
AlsoOtherInputs = True                  # True if you wanna include temperature, angular velocity and linear acceleration as inputs
Scheduler = True                        # True if you wanna the scheduler to decrease learning rate during the training
TypeScheduler = 1                       # 1 = exponential, 2 = plateau
PrintParameters = False                 # True if yuo wanna print the parameters of the NNs during each iteration
UseActivation = True                    # True if you wanna use an activation function, False if you don't wanna use it
activation = [torch.nn.LeakyReLU, torch.nn.ReLU, torch.nn.LeakyReLU, torch.nn.ReLU, torch.nn.ReLU, torch.nn.ReLU, torch.nn.ReLU, torch.nn.ReLU, torch.nn.ReLU, torch.nn.ReLU]              # Activation function
UseDropout = True                       # True if you wanna use dropout, False if you don't wanna use iteration
dropout_prob = [0.1,
    0.05,
    0.0,
    0.0,
    0.19413787771313248, 0.19197994726158144, 0.2, 0.2, 0.2, 0.2] #0.3                     # probability of dropout                 
BiasBool = True                         # True if you wanna use bias in the NN, False if you don't wanna use it
SplitDataset = True                    # True if you wanna split the dataset in training and testing, False if you wanna use same dataset for training and testing
CutFirstAndLast = False                  # True if you wanna cut the first and last part of the dataset
Cut = 1000                              # number of samples to cut at the beginning and at the end of the dataset
weight_decay_optimizer = 0.0            # weight decay for Adam optimizer
gamma_Scheduler = 0.99                 # gamma for exponential scheduler
threshold_loss = 0.005                  # threshold for the loss function to decrease the learning rate with the scheduler  
train_fraction = 0.8                    # in (0,1); decide proportions for training and testing
sign_residual_centroidal = 1            # 1 if you wanna use the residual of the centroidal momentum as it is, -1 if you wanna use the opposite
continue_training = False               # True if you wanna continue training from a previous model
optimizer_name = 'Adam'                      # 'Adam' or 'SGD'
SHUFFLE = True                         # True if you wanna shuffle the dataset
SEED = 1000
INCLUDE_WALKING = False                 # True if you wanna include walking in the dataset
USE_NEW_MODELS = False
SAVE_MODELS = True
FILTERED = False
BATCH_NORMALIZATION = False


if AlsoOtherInputs == True:
    n_input = 13
else:
    n_input = 6

config_parameters_PINN = {
    'batch_size' : batch_size,
    'num_epochs' : num_epochs,
    'learning_rate' : learning_rate,
    'n_neurons' : n_neurons,
    'n_layers' : n_layers,
    'normalization' : normalization,
    'initialization' : initialization,
    'mean_stand_initialization' : mean_stand_initialization,
    'std_stand_initialization' : std_stand_initialization,
    'lim_inf_unif_initialization' : lim_inf_unif_initialization,
    'lim_sup_unif_initialization' : lim_sup_unif_initialization,
    'weight_centroidal' : weight_centroidal,
    'weight_expected' : weight_expected,
    'Sensor' : Sensor,
    'AlsoOtherInputs' : AlsoOtherInputs,
    'Scheduler' : Scheduler,
    'TypeScheduler' : TypeScheduler,
    'PrintParameters' : PrintParameters,
    'UseActivation' : UseActivation,
    'activation' : activation,
    'UseDropout' : UseDropout,
    'dropout_prob' : dropout_prob,
    'BiasBool' : BiasBool,
    'SplitDataset' : SplitDataset,
    'CutFirstAndLast' : CutFirstAndLast,
    'Cut' : Cut,
    'weight_decay_optimizer' : weight_decay_optimizer,
    'gamma_Scheduler' : gamma_Scheduler,
    'threshold_loss' : threshold_loss,
    'train_fraction' : train_fraction,
    'sign_residual_centroidal' : sign_residual_centroidal,
    'n_input' : n_input,
    'continue_training' : continue_training,
    'optimizer_name' : optimizer_name,
    'SHUFFLE' : SHUFFLE,
    'SEED' : SEED,
    'INCLUDE_WALKING' : INCLUDE_WALKING,
    'USE_NEW_MODELS' : USE_NEW_MODELS,
    'SAVE_MODELS' : SAVE_MODELS,
    'FILTERED' : FILTERED,
    'BATCH_NORMALIZATION' : BATCH_NORMALIZATION
}