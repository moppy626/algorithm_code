from typing import List, Tuple
from local_driver import Alg3D, Board  # ローカル検証用
# from framework import Alg3D, Board   # 提出時はこちら

class MyAI(Alg3D):
	def get_best_move(self, score_board: List[List[int]]) -> Tuple[int, int]:
		# 4x4 の二次元配列から最大の点数を持つ (x, y) を返す
		best_score = -10**9
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

		# 端っこが空いていたら重めに配点
		if board[0][0][0] == 0:
			score_board[0][0]+=100
		if board[0][3][0] == 0:
			score_board[3][0]+=100
		if board[0][3][3] == 0:
			score_board[3][3]+=100
		if board[0][0][3] == 0:
			score_board[0][3]+=100
		
		#すべての直線をループ
		for z in range(4):
			for y in range(4):
				for x in range(4):
					#横方向
					if x+3 < 4:
						line = [board[z][y][x+i] for i in range(4)]
						if line.count(1) == 3 and line.count(0) == 1:
							score_board[y][x+line.index(0)] += 100
						if line.count(2) == 3 and line.count(0) == 1:
							score_board[y][x+line.index(0)] += 50
					#縦方向
					if y+3 < 4:
						line = [board[z][y+i][x] for i in range(4)]
						if line.count(1) == 3 and line.count(0) == 1:
							score_board[y+line.index(0)][x] += 100
						if line.count(2) == 3 and line.count(0) == 1:
							score_board[y+line.index(0)][x] += 50
					#奥行き方向
					if z+3 < 4:
						line = [board[z+i][y][x] for i in range(4)]
						if line.count(1) == 3 and line.count(0) == 1:
							score_board[y][x] += 100
						if line.count(2) == 3 and line.count(0) == 1:
							score_board[y][x] += 50
					#斜め方向 xy平面
					if x+3 < 4 and y+3 < 4:
						line = [board[z][y+i][x+i] for i in range(4)]
						if line.count(1) == 3 and line.count(0) == 1:
							score_board[y+line.index(0)][x+line.index(0)] += 100
						if line.count(2) == 3 and line.count(0) == 1:
							score_board[y+line.index(0)][x+line.index(0)] += 50
					if x-3 >= 0 and y+3 < 4:
						line = [board[z][y+i][x-i] for i in range(4)]
						if line.count(1) == 3 and line.count(0) == 1:
							score_board[y+line.index(0)][x-line.index(0)] += 100
						if line.count(2) == 3 and line.count(0) == 1:
							score_board[y+line.index(0)][x-line.index(0)] += 50
					#斜め方向 xz平面
					if x+3 < 4 and z+3 < 4:
						line = [board[z+i][y][x+i] for i in range(4)]
						if line.count(1) == 3 and line.count(0) == 1:
							score_board[y][x+line.index(0)] += 100
						if line.count(2) == 3 and line.count(0) == 1:
							score_board[y][x+line.index(0)] += 50
					if x-3 >= 0 and z+3 < 4:
						line = [board[z+i][y][x-i] for i in range(4)]
						if line.count(1) == 3 and line.count(0) == 1:
							score_board[y][x-line.index(0)] += 100
						if line.count(2) == 3 and line.count(0) == 1:
							score_board[y][x-line.index(0)] += 50
					#斜め方向 yz平面
					if y+3 < 4 and z+3 < 4:
						line = [board[z+i][y+i][x] for i in range(4)]
						if line.count(1) == 3 and line.count(0) == 1:
							score_board[y+line.index(0)][x] += 100
						if line.count(2) == 3 and line.count(0) == 1:
							score_board[y+line.index(0)][x] += 50
					if y-3 >= 0 and z+3 < 4:
						line = [board[z+i][y-i][x] for i in range(4)]
						if line.count(1) == 3 and line.count(0) == 1:
							score_board[y-line.index(0)][x] += 100
						if line.count(2) == 3 and line.count(0) == 1:
							score_board[y-line.index(0)][x] += 50
					#斜め方向 xyz空間
					if x+3 < 4 and y+3 < 4 and z+3 < 4:
						line = [board[z+i][y+i][x+i] for i in range(4)]
						if line.count(1) == 3 and line.count(0) == 1:
							score_board[y+line.index(0)][x+line.index(0)] += 100
						if line.count(2) == 3 and line.count(0) == 1:
							score_board[y+line.index(0)][x+line.index(0)] += 50
					if x-3 >= 0 and y+3 < 4 and z+3 < 4:
						line = [board[z+i][y+i][x-i] for i in range(4)]
						if line.count(1) == 3 and line.count(0) == 1:
							score_board[y+line.index(0)][x-line.index(0)] += 100
						if line.count(2) == 3 and line.count(0) == 1:
							score_board[y+line.index(0)][x-line.index(0)] += 50
					if x+3 < 4 and y-3 >= 0 and z+3 < 4:
						line = [board[z+i][y-i][x+i] for i in range(4)]
						if line.count(1) == 3 and line.count(0) == 1:
							score_board[y-line.index(0)][x+line.index(0)] += 100
						if line.count(2) == 3 and line.count(0) == 1:
							score_board[y-line.index(0)][x+line.index(0)] += 50
					if x-3 >= 0 and y-3 >= 0 and z+3 < 4:
						line = [board[z+i][y-i][x-i] for i in range(4)]
						if line.count(1) == 3 and line.count(0) == 1:
							score_board[y-line.index(0)][x-line.index(0)] += 100
						if line.count(2) == 3 and line.count(0) == 1:
							score_board[y-line.index(0)][x-line.index(0)] += 50			
				


		#すでに埋まっている箇所に-10**9を設定
		print("=== 盤面探索開始 ===")
		for y in range(4):
			for x in range(4):
					if board[3][y][x] > 0:
						score_board[y][x] = -10**9
					# 各 (x, y) の最下段セルを出力して確認
					#print(f"checking (x={x}, y={y}, z={z}): value={board[z][y][x]}")
		x, y = self.get_best_move(score_board)
		return (x, y)

		raise ValueError("置ける場所がありません。")

