# API Documentation
## User login
 - POST **/api/auth/register**
   - Register a new user
   - Form data
     - username
     - password
   - Response
     - success
     - (when success) uuid
     - (when not success) reason
 - POST **/api/auth/login**
   - Login the user
   - Form data
     - username
     - password
   - Response
     - (when valid) uuid
     - (when valid) expires
     - (when valid) token
     - (when not valid) 400
## Model
  - GET **/api/model/params**
  
    Gets the hyper parameters
    - Response
    
      JSON: \[int, int]
      - (int) inputSize
      - (int) learningRate
  - POST **/api/model/params**
  
    Adjusts the hyper parameters
    - Form data
    
      int
      - (optional) (int) learningRate
    - Response
    
      bool
      - (bool) success
  - POST **/api/model/forward**
    - Forward the model
    - Form data
    
      JSON: int[]
      - (int[]) X: input data
    - Response
    
      int
      - (int) A: output data
  - GET **/api/model/backward**
    - Backward the model
    - Response
    
      int
      - (int) A: output data
  - GET **/api/model/output**
    - Gets the output
    - Response
    
      int
      - (int) A: output
  - GET **/api/model/optimize**
    - Optimizes the model
    - Response
    
      JSON: [int[][], int[][]]
      - (int[][]) dW: gradient of W
      - (int[][]) dB: gradient of B
  - GET **/api/model/model**
    - Gets the model
    - Response
    
      JSON: [int[][], int[][]]
      - (int[][]) W: weights matrix
      - (int[][]) B: biases matrix
