# INF442P5_python
Viola &amp; Jones in Python

Data_set can be found here :
https://drive.google.com/open?id=10M-HTRWXquvK0fW_OpxB-bWpZbHW1dKA

Exercise followed can be found here :
https://drive.google.com/open?id=1FjeG0eyOq2G87-cs7RUSwSXPYthUmOFP

Warning :
train_images_integral.txt is too large for GitHub
In order to avoid computing it at each training session
it can be found here :
https://drive.google.com/open?id=16zNjH6vrY-bd4zR8xfk3B1J8WjCIF4fr

How to :
(paste in iPython console)

1. Set a training_session :

#will load train_data_set from data/train
execfile("load_train_data.py")

#will load classifiers from classifiers.txt
execfile("load_classifiers.py")

2. Have a training_session :

K = 200
epsilon = 0.01
#will train classifiers with parameters (K,epsilon)
execfile("train_classifiers.py")

3. Set a test_session :

#will load test_data_set from data/test
execfile("load_test_data.py")

#will load classifiers from classifiers.txt
execfile("load_classifiers.py")

4. Have a test_session :

#will test and print accuracy over data/test
execfile("test_data_set.py")

5. Set a boosting_session over data/test :

execfile("load_test_data.py")

execfile("load_classifiers.py")

execfile("set_adaboost_testdataset.py")

6. Have a boosting_session over data/test :

execfile("boosting_with_ada_boost_testdata.py")

7. Have a test_session on boosted_classifiers over data/test :

execfile("test_boosted_classifiers_test_dataset.py")

8. Set a boosting_session over data/train :

execfile("load_train_data.py")

execfile("load_classifiers.py")

execfile("set_adaboost_traindataset.py")

6. Have a boosting_session over data/train :

execfile("boosting_with_ada_boost_traindata.py")

7. Have a test_session on boosted_classifiers over data/train :

execfile("test_boosted_classifiers_train_dataset.py")
