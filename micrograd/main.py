class Value:

    def __init__(self, data, _children = (), _op = '', label = ''):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._op = _op
        self.label = label

        def __repr__(self):
            return f"Value(data={self.data})"
        
        def __add__(self, other):
            out = Value(self.data + other.data, (self, other), '+')
        


        def __mul__(self, other):
            out = Value(self.data * other.data, (self, other), '*')
            return out
        
        def tanh(self):
            n = self.data 
            t = (math.exp(2*n) - 1)/(math.exp(2*n) + 1)
            out = Value(t, (self, ), 'tanh')
            return out



class Neuron:

    def __init__(self, nin):
        self.w = [Value(random.uniform(-1,1)) for _ in nin]
        self.b = Value(random.uniform(-1,1))


    def __call__(self, x):
        out = sum([wi * xi for wi, xi in zip(self.w, x)])
        act = out.tanh()
        return act
    
class Layer:
    
    def __intit__(self, nin, nout):
        self.neurons = [Neuron(nin) for _ in nout]
    
    def __call__(self, x):
        acts = [n(x) for n in self.neurons]
        return acts[0] if acts == 1 else acts

class MLP:

    def __init__(self, nin, nouts):
        sz = [nin] + nouts
        self.layers = [Layer(sz[i], sz[i+1] for i in range(len(nouts)))]

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return output 
    


    

        





