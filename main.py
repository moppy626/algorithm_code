from typing import List, Tuple
from local_driver import Alg3D, Board  # ローカル検証用
# from framework import Alg3D, Board   # 提出時はこちら

class MyAI(Alg3D):
	def get_best_move(self, score_board: List[List[int]]) -> Tuple[int, int]:
		# 4x4 の二次元配列から最大の点数を持つ (x, y) を返す
		best_score = 0
		best_move = (0, 0)
		for y in range(4):
			for x in range(4):
				score = score_board[y][x]
				if score > best_score:
					best_score = score
					best_move = (x, y)
		return best_move

	def get_move(
		self,
		board: Board,
		player: int,
		last_move: Tuple[int, int, int],
	) -> Tuple[int, int]:

		score_board = [[0]*4 for _ in range(4)]

		#すでに埋まっている箇所に-100を設定
		print("=== 盤面探索開始 ===")
		for y in range(4):
			for x in range(4):
				for z in range(4):
					# 各 (x, y) の最下段セルを出力して確認
					print(f"checking (x={x}, y={y}, z={z}): value={board[z][y][x]}")
					if board[z][y][x] == 0:
						print(f"--> 選択: (x={x}, y={y})")
						score_board[x][y] = -100

		# 端っこが空いていたら重めに配点
		if board[0][0][0] == 0:
			score_board[0][0]+=10
		if board[0][3][0] == 0:
			score_board[0][3]+=10
		if board[0][3][3] == 0:
			score_board[3][3]+=10
		if board[0][0][3] == 0:
			score_board[3][0]+=10

		x, y = self.get_best_move(score_board)
		return (x, y)

		raise ValueError("置ける場所がありません。")

