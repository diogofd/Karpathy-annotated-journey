# Building micrograd


These notes are inspired, of course, by Andrej's fantastic course but also by the [notes](https://etale.site/writing/z2h.pdf) of Aaron Mazel-Gee, which offer a mathematically-rich companion to Andrej's more hands-on approach.

In here, you will be reminded of some stuff you learned in multivariable calculus, if you have taken a course on the subject; if that is not the case, then hopefully you get to learn some essential facts about multivariable calculus without which you will never truly understand how Neural Networks are being trained everywhere these days. 

Ideally these notes were meant to capture my thoughts as I am learning this material. The goal was to keep track of how my thinking about the subject evolved and flag certain key insights, which I could potentially refer back to, or offer to anyone interested in reading them. Despite this sounding like a respectable plan, it is not practical; I keep imagining these notes as a more pedagogical tool, and consistently straying off of their original mission, deviating to explanations for a broader audience—while neglecting the self-explanatory tone.


## Some thoughts on Python classes

This is mostly for my own benefit—I have not spent enough time programming in the last couple of years to be comfortable thinking in terms of Python classes--fluently, at least. Perhaps you, the reader, find yourself in a similar situation—if that is the case, I hope this helps :)

I'll try to cover the basics, so that things like "self._backprop" can make a little more sense, even if they sound a somewhat self-explanatory. I am the kind of person who enjoys learning things at a deeper level, so I am usually reluctant to just internalize syntx wihtout proper context. 

There are some fundamental concepts and some syntax involved, but overall I'll keep it as light as possible. 

### Python classes

Classes ara a type of *object* in Python. They are used to define new data structures and specify functionalities for those structures. 

*Attribute references:*

*Data attributes:*

*Method objects:*

## What is a Neural Network

The principal goal of ``micrograd`` is training a neural network. To understand what this means, we must work on defining neural networks; the way micrograd handles this is by breaking down a neural network into components.

A neural network is nothing but a mathematical function. Mathematical functions can be very complicated but they can also be very simple. For example, consider the function $$s(x,y):= x+y$$
which takes as input a pair of real numbers $x,y\in\mathbb{R}$ and outputs another real number $w\in\mathbb{R}$ corresponding to the sum. Let us consider something a hair more complicated, but still very simple, let $$p(x,y):= x\cdot y$$ be the function which takes the product of two real numbers.

To make life more interesting, we can take these two fumctions and *compose* them. This operation is very general for mathemcatical functions: given a pair of functions $f\colon X \rightarrow Y$ and a function $g\colon Y \rightarrow Z$, we can construct a third function $(g\circ f)\colon X \rightarrow Z$.

If this seems abstract, don't worry. We'll unpack it: what does the function $(g\circ f)$ do exactly? Let's say we have a value $x\in X$, then we define $(g\circ f)(x)$ to be the consecutive application of these two functions. So, first we do $f$ which "sends" $x \mapsto f(x)$ (note that $f(x)\in Y$) and then we apply $g$ which will send $f(x) \mapsto g(f(x))$. 

With this, we can ask if $w(x,y)$ and $s(x,y)$ are composble? Well, maybe not. Note that $w\colon \mathbb{R}^2 \rightarrow \mathbb{R}$ and that $p\colon  



## Forward pass



## Backpropagation & Chain Rule




### Manual backpropagation
 





### Automating backpropagation


### topological sorting 

Topological sorting turns a directed acylic graph into a linearly oredered set.

We employ this technique because we need a way of telling ``micrograd`` how to sequence the backpropagation steps. 

To be clear, we can only do backprogation on a node if all of the nodes "after" it have been backpropagated.  

- *Why do we need it:* to "synchronize" the backpropagtion steps.
- *How do we implement it:* using a simple topological sorting algorithm.

**Here it is**:

```python
topo = []
visited = set()

def build_topo(v):
    if v not in visited:
        visited.add(v)
    for child in v._prev:
        build_topo(child)
    topo.append(v)
```

Once we topologically sort our computational graph, we can ensure that, in starting at the last node on the topo list, we have no dependencies. 

## What is a layer?

We have idenitified what a **neuron** is, and we have enshrined its behaviour in a class called ``Neuron``. Neurons come together to form **layers**; 


## Training a small NN

```python
[(yout - ygt)**2 for ygt, yout in zip(ys, ypred)]
```



## The case of the terrible bug

Workin with NN can be tricky. We forgot to zerograd()

We are accumulating gradients, when we should not? It seems like the NN is taking more steps to get to equally good losse

The accumulated gradient gave us a really large step size because the problem was really simple... Does this admit a more mathematically reasonable explanation?

