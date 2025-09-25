from typing import List, Tuple
#from local_driver import Alg3D, Board # ローカル検証用
from framework import Alg3D, Board # 本番用

class MyAI(Alg3D):
    def get_move(
        self,
        board: List[List[List[int]]], # 盤面情報
        player: int, # 先手(黒):1 後手(白):2
        last_move: Tuple[int, int, int] # 直前に置かれた場所(x, y, z)
    ) -> Tuple[int, int]:
        # 空いている座標を取得
        moves = self.get_available_moves(board)
        # とりあえず最初の候補を返す
        if moves:
            return moves[0][:2]  # (x, y) だけ返す
        else:
            raise ValueError("置ける場所がありません。")

    def get_available_moves(
        self,
        board: List[List[List[int]]]
    ) -> List[Tuple[int, int, int]]:
        """ 置ける場所(最下段の空き)を返す """
        size_x = len(board)
        size_y = len(board[0])
        size_z = len(board[0][0])

        available = []
        for x in range(size_x):
            for y in range(size_y):
                for z in range(size_z):
                    if board[x][y][z] == 0:  # 空き
                        available.append((x, y, z))
                        break  # 一番下の空きだけで良いのでbreak
        return available