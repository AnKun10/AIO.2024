from Module2.Week3.model.create_train_dataset import create_train_dataset
from Module2.Week3.model.get_index_from_value import get_index_from_value
from Module2.Week3.model.compute_probability import *

# Ex 13
train_data = create_train_dataset()
print(train_data)

# Ex 14
prior_probability = compute_prior_probability(train_data)
print("P(play tennis = No) =", prior_probability[0])
print("P(play tennis = Yes) =", prior_probability[1])

# Ex 15
_, list_x_name = compute_conditional_probability(train_data)
print("x1 = ", list_x_name[0])
print("x2 = ", list_x_name[1])
print("x3 = ", list_x_name[2])
print("x4 = ", list_x_name[3])

# Ex 16
outlook = list_x_name[0]
i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)
print(i1, i2, i3)

# Ex 17
conditional_probability, list_x_name = compute_conditional_probability(train_data)
x1 = get_index_from_value("Sunny", list_x_name[0])
print("P('Outlook'='Sunny'| 'Play Tennis'='Yes') = ", np.round(conditional_probability
                                                               [0][1, x1], 2))

# Ex 18
x1 = get_index_from_value("Sunny", list_x_name[0])
print("P('Outlook'='Sunny'| 'Play Tennis'='No') = ", np.round(conditional_probability
                                                              [0][0, x1], 2))

# Ex 19
X = ['Sunny', 'Cool', 'High', 'Strong']
prior_probability, conditional_probability, list_x_name = train_naive_bayes(train_data)
pred = prediction_play_tennis(X, list_x_name, prior_probability, conditional_probability)
if pred:
    print("Ad should go!")
else:
    print("Ad should not go!")
