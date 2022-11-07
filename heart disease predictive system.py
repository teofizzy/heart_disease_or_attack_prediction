import numpy as np
import pickle

#loading the saved model
load_model = pickle.load(open('C:/Users\Teofilo_Ligawa/Documents/Practice/Kaggle/heart_disease_or_attack_prediction/trained_model.sav', 'rb'))

input_data = [1, 1, 1, 40, 1, 0, 0, 0, 0, 1, 0, 1, 0, 5, 18, 15, 1, 0, 9, 4, 3]
test_2 = [1,	1,	1,	30,	1,	0,	2,	0,	1,	1,	0,	1,	0,	5,	30,	30,	1,	0,	9,	5,	1]
# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(test_2)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = load_model.predict(input_data_reshaped)
accuracy = load_model.score(input_data_reshaped, prediction)
print(prediction)

if (prediction[0] == 0):
  print('The person does not have heart disease')
else:
  print('The person has heart disease')
