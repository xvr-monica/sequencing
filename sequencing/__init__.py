#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   Author: Sword York
#   GitHub: https://github.com/SwordYork/sequencing
#   No rights reserved.
#
from collections import namedtuple

import tensorflow

MODE = namedtuple('MODE', 'TRAIN EVAL INFER RL')(0, 1, 2, 3)
TIME_MAJOR = True
DTYPE = tensorflow.float32

from .encoders.rnn_encoder import StackBidirectionalRNNEncoder
from .attention.attention import Attention
from .decoders.feedback import TrainingFeedBack, BeamFeedBack, \
    RLTrainingFeedBack
from .decoders.attention_decoder import AttentionRNNDecoder
from .decoders.decoder import dynamic_decode
from .utils.algebra_ops import LookUpOp, LinearOp
from .utils.misc import disable_dropout
from .data.vocab import Vocab

__all__ = ('StackBidirectionalRNNEncoder', 'Attention', 'TrainingFeedBack',
           'RLTrainingFeedBack', 'BeamFeedBack', 'AttentionRNNDecoder',
           'dynamic_decode', 'LookUpOp', 'LinearOp', 'disable_dropout', 'Vocab')

__version__ = 0.1
