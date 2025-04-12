

- We now attempt to present the information in a different way. We want to visualize this bigram data as a square matrix whose rows and columns are in correspondence with the character alphabet.
    - The rows will encode the first character and the columns will encode the second character.
    - With this setup, the entry of the matrix which corresponds to the pair "de" is the number of times this bigram shows up in our database.`
- We do sampling from a distribution using torch.multinomial
- One of the most confusing points about this video was working out what Andrej was in fact calling "the model". Especially in the section which discusses the quality of the model: here, I felt especially lost for 1 or 2 minutes, when we were just looking at bigram probs for the bigrams in the dataset. 
    - I then realized that what he meant by model was just the choice of bigrams + next character prediction. 
- Model smoothing: solving the problem of training loss dumbness when the dataset is "limited".f


Passage from bigram character-level LM --> Neural Network.

Gradient based optimization.

Aha, we're going to use one-hot encodings to translate integer-representation into vector representations. I wonder how bengign the effect of using one-hot encodings is? The answer is: none, at least in this case. 


We can think of the NN computation here as a demonstration of what we might be able to do with gradient-based approaches to learning propbability distributions from a training set.

## Pytorch 

Here we talked a little bit about the 

- torch.tensor vs. torch.Tensor
- about how torch does broadcasting, and the pitfalls of not understanding this well
- torch.nn and torch.backward



## Matplotlib

- 