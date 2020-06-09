# Model API Documentation

## Create a model
POST ```/api/model/new```

Response:

Name   | Format | Description
-------|--------|------------
(None) | uuid | The session_id, id of the model (unique per model)

## Iter the model
POST ```/api/model/iter```

Form data:

Name | Format | Description
-----|--------|------------
session_id | uuid | Unique id of the model, created by ```/api/model/new```
epoch_num | int | The number of epochs (2)
learning_rate | float | The rate of learning (0.01)

Json response:

Name | Format | Description
-----|--------|------------
X | float\[\]\[\] | The input data matrix, with size (input_node_num, data_num)
Y | float\[\]\[\] | The output data matrix, with size (output_node_num, data_num)
W | float\[\]\[\]\[\] | The weight matrix, with size (layer_num, node_num_per_layer, previous_layer_node_num)
dW | float\[\]\[\]\[\] | The gradient matrix, size same as W
loss | float\[\] | The loss for each epoch, with size (epoch_num)
avg_loss | float | The average loss
accuracy | float\[\] | The accuracy for each epoch, size same as loss
A | float\[\]\[\] | The predicted value, size same as Y
