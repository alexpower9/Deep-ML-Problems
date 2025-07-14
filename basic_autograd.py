class Value:
    def __init__(self, data, _children=(), _op=''):
        self.data = data
        self.grad = 0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op
    def __repr__(self):
        return f"Value(data={self.data}, grad={self.grad})"

    #we should add checks to __add__ and __mul__ to ensure they are value
    def __add__(self, other):
        if not isinstance(other, Value):
            other = Value(other)
        
        out = Value(self.data + other.data, _children=(self, other), _op='+') 
        
        def _backward():
            self.grad = int(1.0 * out.grad)
            other.grad = int(1.0 * out.grad)
        
        out._backward = _backward
        return out
    
    def __mul__(self, other):
        if not isinstance(other, Value):
            other = Value(other)
        
        out = Value(self.data * other.data, _children=(self, other), _op='*')
        
        def _backward():
            self.grad = int(other.data * out.grad)
            other.grad = int(self.data * out.grad)
        
        out._backward = _backward
            
        return out
             
    # defined as max(0, x)
    def relu(self):
        x = self.data
        out_data = max(0, x)
        out = Value(out_data, _children=(self,), _op='relu')
        
        def _backward():
            dvalue = 1 if out.data > 0 else 0
            self.grad = int(dvalue * out.grad)
            
        out._backward = _backward
        return out

    def backward(self):
        # Implement backward pass here
        # we will traverse the graph and call the backward methods
        # depth-first search
        self.grad = 1.0 # start with a grad of 1
        topo = []
        visited = set()
        
        def build_topo(v):
            if v not in visited:
                visited.add(v)
            
                for child in v._prev:
                    build_topo(child)
                topo.append(v)
        
        build_topo(self)
        
        # now we can call the backward functions on the sorted values
        for node in reversed(topo):
            node._backward()

    
a = Value(2);b = Value(3);c = Value(10);d = a + b * c ;e = Value(7) * Value(2);f = e + d;g = f.relu(); g.backward(); print(a,b,c,d,e,f,g)