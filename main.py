from typing import List, Tuple
from local_driver import Alg3D, Board  # ローカル検証用
# from framework import Alg3D, Board   # 提出時はこちら

class MyAI(Alg3D):
	def get_move(
		self,
		board: Board,
		player: int,
		last_move: Tuple[int, int, int],
	) -> Tuple[int, int]:
		print("=== 盤面探索開始 ===")
		for y in range(4):
			for x in range(4):
				for z in range(4):
					# 各 (x, y) の最下段セルを出力して確認
					print(f"checking (x={x}, y={y}, z={z}): value={board[z][y][x]}")
					if board[z][y][x] == 0:
						print(f"--> 選択: (x={x}, y={y})")
						return (x, y)

		raise ValueError("置ける場所がありません。")