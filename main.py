from typing import List, Tuple
from local_driver import Alg3D, Board  # ローカル検証用
# from framework import Alg3D, Board   # 提出時はこちら

class MyAI(Alg3D):
	DIRECTIONS = [
		(1,0,0), (0,1,0), (0,0,1),
		(1,1,0), (1,-1,0),
		(1,0,1), (1,0,-1),
		(0,1,1), (0,1,-1),
		(1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1),
	]

	def in_bounds(self, x:int,y:int,z:int)->bool:
		return 0 <= x < 4 and 0 <= y < 4 and 0 <= z < 4

	def iter_lines(self):
		lines = []
		for dx,dy,dz in self.DIRECTIONS:
			for x0 in range(4):
				for y0 in range(4):
					for z0 in range(4):
						# 逆方向に1マス進めるなら始点じゃない
						px,py,pz = x0 - dx, y0 - dy, z0 - dz
						if self.in_bounds(px,py,pz):
							continue
						# 4マス目の終点が盤外なら直線にならない
						x3,y3,z3 = x0 + 3*dx, y0 + 3*dy, z0 + 3*dz
						if self.in_bounds(x3,y3,z3):
							line = [(x0 + i*dx, y0 + i*dy, z0 + i*dz) for i in range(4)]
							lines.append(line)
		return lines

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
		
		for line in self.iter_lines():
			# 相手の石の数をカウント
			enemy_count = 0
			empty_count = 0
			for idx, (x,y,z) in enumerate(line):
				if (board[z][y][x] == 0):
					empty_count += 1
				elif (board[z][y][x] != player):
					enemy_count += 1
			print("enemy_count:", enemy_count)
			if (enemy_count >= 2):
				for idx, (x,y,z) in enumerate(line):
					# 石が置ける高さの場合
					if (board[z][y][x] == 0) and (z == 0 or board[z - 1][y][x] > 0):
						# 相手の石が3つあるときは重めに配点
						if (enemy_count == 3):
							score_board[y][x]+= 1000
						# 相手の石が2つあり残り2つが空の場合も重めに配点
						elif (empty_count == 2):
							score_board[y][x]+= 50
					# 石が置けない高さでも、置くと相手が上がってしまう場合は置かない
					elif (enemy_count == 3):
						if (board[z - 1][y][x] == 0):
							score_board[y][x] = -10**9

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

