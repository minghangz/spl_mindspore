import argparse
from datetime import datetime

parser = argparse.ArgumentParser()
# data parameters
parser.add_argument('--save_dir', type=str, default='datasets', help='path to save processed dataset')
parser.add_argument('--task', type=str, default='charades', help='target task')
parser.add_argument('--fv', type=str, default='new', help='[new | org] for visual features')
parser.add_argument('--fq', type=str, default='word+char', help='query features: word, char, word+char')
parser.add_argument('--max_pos_len', type=int, default=128, help='maximal position sequence length allowed')
# model parameters
parser.add_argument("--word_size", type=int, default=None, help="number of words")
parser.add_argument("--char_size", type=int, default=None, help="number of characters")
parser.add_argument("--word_dim", type=int, default=300, help="word embedding dimension")
parser.add_argument("--video_feature_dim", type=int, default=1024, help="video feature input dimension")
parser.add_argument("--char_dim", type=int, default=50, help="character dimension, set to 100 for activitynet")
parser.add_argument("--dim", type=int, default=128, help="hidden size")
parser.add_argument("--highlight_lambda", type=float, default=5.0, help="lambda for highlight region")
parser.add_argument("--rank_lambda", type=float, default=1.0, help="lambda for ranking branch")
parser.add_argument("--num_heads", type=int, default=8, help="number of heads")
parser.add_argument("--num_layers", type=int, default=1, help="number of convolution layers")
parser.add_argument("--drop_rate", type=float, default=0.2, help="dropout rate")
parser.add_argument("--min_iou", type=float, default=0.3, help="lower bound of iou")
parser.add_argument("--max_iou", type=float, default=0.7, help="upper bound of iou")
parser.add_argument("--threshold", type=float, default=0.5, help="lambda for ranking loss")
# training/evaluation parameters
parser.add_argument("--gpu_idx", type=str, default="0", help="GPU index")
parser.add_argument("--seed", type=int, default=None, help="random seed")
parser.add_argument("--mode", type=str, default="train", help="[train | test]")
parser.add_argument("--elastic", action='store_true', help='if test the model according to elastic boundary')
parser.add_argument("--epochs", type=int, default=100, help="number of epochs")
parser.add_argument("--batch_size", type=int, default=16, help="batch size")
parser.add_argument("--num_train_steps", type=int, default=None, help="number of training steps")
parser.add_argument("--init_lr", type=float, default=0.0005, help="initial learning rate")
parser.add_argument("--clip_norm", type=float, default=1.0, help="gradient clip norm")
parser.add_argument("--warmup_proportion", type=float, default=0.0, help="warmup proportion")
parser.add_argument("--extend", type=float, default=0.1, help="highlight region extension")
parser.add_argument("--period", type=int, default=5, help="training loss print period")
parser.add_argument('--deploy', action='store_true', help='if to save checkpoint and logs')
parser.add_argument('--model_dir', type=str, default='sessions', help='path to save trained model weights')
parser.add_argument('--model_name', type=str, default=datetime.now().strftime('%Y%m%d-%H%M%S'), help='model name')
parser.add_argument('--suffix', type=str, default=None, help='set to the last `_xxx` in ckpt repo to eval results')
parser.add_argument('--noise_alpha', type=float, default=0.75)
parser.add_argument('--noise_beta', type=float, default=0.75)
parser.add_argument('--use_refine', action='store_true')

gconfigs = parser.parse_args()