#!/usr/bin/env python

import time
import os
from cnn_training_functions import *
import argparse

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def main(batch_size, learning_rate, epochs, optimizer, save_frequency, print_frequency):

    # define path for training dataset
    file_path_train = os.path.join(os.getcwd(), 'data', 'train', 'train_set.h5')
    file_path_test = os.path.join(os.getcwd(), 'data', 'test', 'test_set.h5')

    # print(file_path_train)

    # define batch_size (e.g 50, 100)
    # batch_size = 50

    # define which optimizer you want to use (e.g "Adam", "GDS"). For "Adam" and "GDS" this script will take care the rest.
    # ATTENTION !! If you want to choose a different optimizer from these two, you will have to add it in the training functions.
    # optimizer = "GDS"

    # define learning rate (e.g 1E-3, 1E-4, 1E-5):
    # learning_rate = 1E-5

    # define total epochs (e.g 1000, 5000, 10000)
    # epochs = 100

    # read train data
    print('Reading train dataset')
    train_velocities, train_images = load_data(file_path_train)

    # read test data
    print('Reading test dataset')
    test_velocities, test_images = load_data(file_path_test)

    # construct model name based on the hyper parameters
    # model_name = form_model_name(batch_size, learning_rate, optimizer, epochs)
    model_name = 'learned_models'

    print('Starting training for {} model.'.format(model_name))

    # keep track of training time
    start_time = time.time()

    # train model
    cnn_train = CNN_training(batch_size, epochs, learning_rate, optimizer)
    cnn_train.training(model_name, train_velocities, train_images, test_velocities, test_images, save_frequency, print_frequency)

    # calculate total training time in minutes
    training_time = (time.time() - start_time) / 60

    print('Finished training of {} in {} minutes.'.format(model_name, training_time))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CNN training')
    parser.add_argument('--batch-size', type=int, default=50)
    parser.add_argument('--learning-rate', type=float, default=1E-5)
    parser.add_argument('--epochs', type=int, default=100)
    parser.add_argument('--optimizer', type=str, default="Adam", choices=["GDS", "Adam"])
    parser.add_argument('--save-frequency', type=int, default=10)
    parser.add_argument('--print-frequency', type=int, default=5)

    args = parser.parse_args()
    main(args.batch_size, args.learning_rate, args.epochs, args.optimizer, args.save_frequency, args.print_frequency)
