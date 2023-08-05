# ftable

下の方に日本語の説明があります

## Overview
- A table that has had its filter/search function optimized for speed.
- A system that can quickly and easily perform complex feature generation for machine learning using simple descriptions

## Example usage
```python
import ftable

raw_data = [
	{"date": "20450105", "name": "taro", "score": 22.5},
	{"date": "20450206", "name": "hanako", "score": 12.6},
	{"date": "20450206", "name": "taro", "score": 3.5},
]

# Fast table type [ftable]
ft = ftable.FTable(
	raw_data,	# The raw table data
	sorted_keys = ["date"]	# Specifying the sorting axis
)

# Cached filter function [ftable]
filtered_ft = ft.cfilter("name", "taro")
# Display filter result
print(filtered_ft)

# The first argument of cfilter is not a specific column name, but a function that returns a value with one record as its argument.
def judge_score(rec): return ("high" if rec["score"] > 15 else "low")
filtered_ft = ft.cfilter(judge_score, "high")
print(filtered_ft)

# Binary search (find the last index that meets the condition; if False from the beginning, return -1) [ftable]
idx = filtered_ft.bfind("date",
	cond = lambda date: (date < "20450110"))

# Direct reference to original data
print(idx)
if idx == -1: idx = None
print(filtered_ft.data[idx])

# The principle of accelerating the aggregation is to automatically cache the aggregation results of 2^n data blocks of the original data, resulting in faster performance.
# If no binary operation is specified, it computes the sum over the specified index range with respect to the specified column.
res = ft.csum(0, 2, "score")	# The first and second arguments are the start and end indices, respectively. The range specified is up to just before the end index.
print(res)

# It is also possible to perform binary operations other than sum (such as max)
res = ft.csum(0, 2, "score", lambda a, b: max(a, b))
print(res)

# If the value to be aggregated is not the record value itself and requires some processing, the fast sum function (aggregating with binary operation) can be used for that as well.
res = ft.csum(
	0, 2,
	lambda rec: len(rec["name"]),
	lambda a, b: max(a, b)
)
print(res)

# Select a random record (with fixed seed) [ftable]
print(ft.rget(2))
```

## Note
- Please do not modify the data once it has been initialized as an FTable. (This may cause search functionality to be unreliable)
- In the current version, only 1 or 0 sorted_keys can be specified
- Note that bfind returns -1 if the result of cond() is False for the first element (be aware of this when implementing previous and next, taking into account that Python's -1 index reference refers to the last element)
- Note that the raw_data accessible via the `ftable_obj.data` interface is reordered in sorted_keys order, so the order is different from the original data.
- csum can be used to perform aggregation on a variety of binary operations; as a restriction on the range of binary operations, it need not be commutative, but the join rule `f(a, f(b, c)) == f(f(a, b), c)` must always hold. (Thus, it can also be used for matrix product-like aggregations.)
- In cfilter and csum, when passing an aggregate function, it is recommended to pass a function defined once in a common place as a function name, instead of writing a lambda expression on the spot, from the viewpoint of calculation volume. (This is because the function match `f == g` is used as a criterion to determine the identity of the aggregate function when utilizing the internal cache.)

## 概要
- フィルタ・検索機能が高速化されたテーブル
- 機械学習の複雑な特徴量生成を簡単な記述で高速に実行できる

## 使用例
```python
import ftable

raw_data = [
	{"date": "20450105", "name": "taro", "score": 22.5},
	{"date": "20450206", "name": "hanako", "score": 12.6},
	{"date": "20450206", "name": "taro", "score": 3.5},
]

# 高速テーブル型 [ftable]
ft = ftable.FTable(
	raw_data,	# 原型となるテーブルデータ
	sorted_keys = ["date"]	# 整序軸の指定
)

# cacheされたフィルタ機能 [ftable]
filtered_ft = ft.cfilter("name", "taro")
# フィルタ結果の表示
print(filtered_ft)

# cfilterの第一引数は具体的な列名ではなく、1レコードを引数として値を返す関数を指定することもできる。
# cacheされたフィルタ機能 [ftable]
def judge_score(rec): return ("high" if rec["score"] > 15 else "low")
filtered_ft = ft.cfilter(judge_score, "high")
# フィルタ結果の表示
print(filtered_ft)

# 二分探索 (条件を満たす最後のインデックスを見つける; 最初からFalseの場合は-1を返す) [ftable]
idx = filtered_ft.bfind("date",
	cond = lambda date: (date < "20450110"))
print(idx)

# 元データの直接参照
if idx == -1: idx = None
print(filtered_ft.data[idx])

# 集計の高速化の原理は、元データの2のn乗個のデータブロックに対する集計結果を自動的にキャッシュすることで高速化しています。
# 高速合計関数 (2項演算で集計) [ftable]
res = ft.csum(0, 2, "score")	# 第1,2引数はそれぞれ開始インデックスと終了インデックス。終了インデックスの直前までが指定される範囲。
print(res)

# 合計ではない2項演算 (max等) も可能
res = ft.csum(0, 2, "score", lambda a, b: max(a, b))	# 高速合計関数 (2項演算で集計)
print(res)

# 集計対象の値がレコード値そのものではなく、少し加工が必要な場合
res = ft.csum(	# 高速合計関数 (2項演算で集計)
	0, 2,
	lambda rec: len(rec["name"]),
	lambda a, b: max(a, b)
)
print(res)

# ランダムなレコードを選定 (seed固定) [ftable]
print(ft.rget(2))
```

## 注意
- 一度FTableとして初期化したデータは改変しないでください。 (検索の動作が保証されなくなります)
- sorted_keysの指定は現行バージョンでは1または0個のみです
- bfindは、先頭要素からcond()の結果がFalseの場合は-1を返すので注意 (pythonの-1インデックス参照は最終要素を指定することに注意して前後の実装を行ってください)
- `ftable_obj.data` インターフェースでアクセスできるraw_dataは、sorted_keysの順序に並べ変わっているので、元データと順序が異なることに注意してください
- csumは様々な2項演算に対する集計ができる。2項演算の範囲の制限としては、可換である必要はないが、結合則 `f(a, f(b, c)) == f(f(a, b), c)` が必ず成立する必要があります。 (したがって、行列積のような集計にも利用できます。)
- cfilterやcsumにおいて、集計関数を渡す際、その場でlambda式を書くのではなく、共通の場所で1度定義した関数を関数名として渡すのが計算量の観点から推奨です。 (内部のキャッシュ活用時に集計関数の同一性を判定するのに関数の一致 `f == g` を判定基準に用いているためです。)
