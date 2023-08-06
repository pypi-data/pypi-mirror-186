from typing import Optional, Callable, Union, List

import torch
import torch.nn.functional as F
from torch import Tensor, Size
from torch.nn import Module, Parameter, ModuleList
from torch_geometric.nn import MessagePassing
from torch_geometric.typing import Adj, OptTensor
from torch_sparse import matmul, SparseTensor

__all__ = ['SparseReservoirConvLayer', 'SparseStaticGraphReservoir']


class SparseReservoirConvLayer(MessagePassing):
    """
    A Sparse Graph ESN convolution layer

    :param input_features: Input dimension
    :param hidden_features: Reservoir dimension
    :param bias: If bias term is present
    :param activation: Activation function (default tanh)
    """
    input_weight: Parameter
    recurrent_weight: Parameter
    bias: Optional[Parameter]
    activation: Callable[[Tensor], Tensor]

    def __init__(self, input_features: int, hidden_features: int, bias: bool = False,
                 activation: Union[str, Callable[[Tensor], Tensor]] = 'tanh', **kwargs):
        super().__init__(**kwargs)
        self.input_weight = Parameter(torch.empty(hidden_features, input_features), requires_grad=False)
        self.recurrent_weight = Parameter(torch.empty(hidden_features, hidden_features), requires_grad=False)
        self.bias = Parameter(torch.empty(hidden_features), requires_grad=False) if bias else None
        self.activation = activation if callable(activation) else getattr(torch, activation)

    def project_input(self, input: Tensor):
        return F.linear(input, self.input_weight, self.bias)

    def forward(self, edge_index: Adj, input: Tensor, state: Tensor, edge_weight: OptTensor = None):
        neighbour_aggr = self.propagate(edge_index=edge_index, x=state, edge_weight=edge_weight)
        return self.activation(input + (self.recurrent_weight.t() @ neighbour_aggr.t()).t())

    def message(self, x_j: Tensor, edge_weight: OptTensor = None) -> Tensor:
        return x_j if edge_weight is None else edge_weight.view(-1, 1) * x_j

    def message_and_aggregate(self, adj_t: SparseTensor, x: Tensor) -> Tensor:
        return matmul(adj_t, x, self.aggr)

    def initialize_parameters(self, recurrent: Callable[[Size], Tensor], input: Callable[[Size], Tensor],
                              bias: Optional[Callable[[Size], Tensor]] = None):
        """
        Initialize reservoir weights

        :param recurrent: Random matrix generator for recurrent weight
        :param input: Random matrix generator for input weight
        :param bias: Random matrix generator for bias, if present
        """
        self.recurrent_weight = Parameter(recurrent(self.recurrent_weight.shape), requires_grad=False)
        self.input_weight = Parameter(input(self.input_weight.shape), requires_grad=False)
        if self.bias is not None:
            self.bias = Parameter(bias(self.bias.shape), requires_grad=False)

    @property
    def in_features(self) -> int:
        """Input dimension"""
        return self.input_weight.shape[1]

    @property
    def out_features(self) -> int:
        """Reservoir state dimension"""
        return self.recurrent_weight.shape[0]

    def extra_repr(self) -> str:
        return f'in={self.in_features}, out={self.out_features}, bias={self.bias is not None}'


class SparseReservoirEmbConvLayer(SparseReservoirConvLayer):
    """
    A Sparse Graph ESN convolution layer for categorical input features

    :param input_features: Input categories
    :param hidden_features: Reservoir dimension
    :param bias: If bias term is present
    :param activation: Activation function (default tanh)
    """

    def __init__(self, input_features: int, hidden_features: int, bias: bool = False,
                 activation: Union[str, Callable[[Tensor], Tensor]] = 'tanh', **kwargs):
        super().__init__(input_features, hidden_features, bias, activation, **kwargs)
        self.input_weight = Parameter(torch.empty(input_features, hidden_features), requires_grad=False)

    def project_input(self, input: Tensor):
        return F.embedding(input, self.input_weight) + self.bias

    @property
    def in_features(self) -> int:
        """Input categories"""
        return self.input_weight.shape[0]


class SparseStaticGraphReservoir(Module):
    """
    Reservoir for static graphs

    :param num_layers: Reservoir layers
    :param in_features: Size of input
    :param hidden_features: Size of reservoir (i.e. number of hidden units per layer)
    :param bias: Whether bias term is present
    :param pooling: Graph pooling function (optional, default no pooling)
    :param fully: Whether to concatenate all layers' encodings, or use just final layer encoding
    :param max_iterations: Maximum number of iterations (optional, default infinity)
    :param epsilon: Convergence condition (default None)
    :param categorical_input: Whether input features are categorical
    :param kwargs: Other `SparseReservoirConvLayer` arguments (activation, etc.)
    """
    layers: ModuleList
    pooling: Optional[Callable[[Tensor, Tensor], Tensor]]
    fully: bool
    max_iterations: Optional[int]
    epsilon: float

    def __init__(self, num_layers: int, in_features: int, hidden_features: int, bias: bool = False,
                 pooling: Optional[Callable[[Tensor, Tensor], Tensor]] = None, fully: bool = False,
                 max_iterations: Optional[int] = None, epsilon: Optional[float] = None, categorical_input: bool = False, **kwargs):
        super().__init__()
        assert num_layers > 0, 'At least one layer'
        assert any([max_iterations, epsilon]), 'A stop condition must be defined'
        self.layers = ModuleList()
        if categorical_input:
            self.layers.append(SparseReservoirEmbConvLayer(input_features=in_features, hidden_features=hidden_features, bias=bias, **kwargs))
        else:
            self.layers.append(SparseReservoirConvLayer(input_features=in_features, hidden_features=hidden_features, bias=bias, **kwargs))
        for _ in range(1, num_layers):
            self.layers.append(SparseReservoirConvLayer(input_features=hidden_features, hidden_features=hidden_features, bias=bias, **kwargs))
        self.pooling = pooling
        self.fully = fully
        self.max_iterations = max_iterations
        self.epsilon = epsilon

    def initialize_parameters(self, recurrent: Callable[[Size], Tensor], input: Callable[[Size], Tensor],
                              bias: Optional[Callable[[Size], Tensor]] = None):
        """
        Initialize reservoir weights for all layers

        :param recurrent: Random matrix generator for recurrent weight
        :param input: Random matrix generator for input weight
        :param bias: Random matrix generator for bias, if present
        """
        for layer in self.layers:
            layer.initialize_parameters(recurrent=recurrent, input=input, bias=bias)

    def forward(self, edge_index: Adj, input: Tensor, initial_state: Optional[Union[List[Tensor], Tensor]] = None,
                batch: OptTensor = None, edge_weight: OptTensor = None) -> Tensor:
        """
        Encode input

        :param edge_index: Adjacency
        :param edge_weight: Edges weight (optional)
        :param input: Input graph signal (nodes × in_features)
        :param initial_state: Initial state (nodes × hidden_features) for all reservoir layers, default zeros
        :param batch: Batch index (optional)
        :return: Encoding (samples × dim)
        """
        if initial_state is None:
            initial_state = [torch.zeros(input.shape[0], layer.out_features).to(layer.recurrent_weight) for layer in
                             self.layers]
        elif len(initial_state) != self.num_layers and initial_state.dim() == 2:
            initial_state = [initial_state] * self.num_layers
        embeddings = [self._embed(self.layers[0], edge_index, edge_weight, input, initial_state[0])]
        for i in range(1, self.num_layers):
            embeddings.append(self._embed(self.layers[i], edge_index, edge_weight, embeddings[-1], initial_state[i]))
        if self.fully:
            return torch.cat([self.pooling(x, batch) if self.pooling else x for x in embeddings], dim=-1)
        else:
            return self.pooling(embeddings[-1], batch) if self.pooling else embeddings[-1]

    def _embed(self, layer: SparseReservoirConvLayer, edge_index: Adj, edge_weight: OptTensor, input: Tensor,
               initial_state: Tensor) -> Tensor:
        """
        Compute node embeddings for a single layer

        :param layer: Reservoir layer
        :param edge_index: Adjacency
        :param edge_weight: Edges weight (optional)
        :param input: Input graph signal (nodes × in_features)
        :param initial_state: Initial state (nodes × hidden_features) for all reservoir layers, default zeros
        :return: Encoding (nodes × dim)
        """
        iterations = 0
        old_state = initial_state
        input = layer.project_input(input)
        while True:
            state = layer(edge_index, input, old_state, edge_weight)
            if self.max_iterations and iterations >= self.max_iterations:
                break
            if self.epsilon is not None and torch.norm(old_state - state) < self.epsilon:
                break
            old_state = state
            iterations += 1
        return state

    @property
    def num_layers(self) -> int:
        """Number of reservoir layers"""
        return len(self.layers)

    @property
    def in_features(self) -> int:
        """Input dimension"""
        return self.layers[0].input_weight.shape[1]

    @property
    def out_features(self) -> int:
        """Embedding dimension"""
        return sum(layer.out_features for layer in self.layers) if self.fully else self.layers[-1].out_features

