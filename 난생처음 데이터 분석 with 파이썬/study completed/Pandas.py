#= = = = = = = = = = = = = = = = = = = = = = = = = = 

                   # 연관 : 딕셔너리 #
                # 판다스 라이브러리 사용법 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
# 시리즈(Series)는 판다스(Pandas)에서 제공하는 1차원 데이터 구조입니다.

# 인덱스(Index): 
# - 각 데이터 값에 대한 레이블 또는 키를 나타냅니다. 
# - 이 인덱스를 통해 데이터에 접근할 수 있습니다. 인덱스는 정수, 문자열, 날짜 등 다양한 형태를 가질 수 있습니다.

# 값(Value): 
# - 시리즈가 담고 있는 데이터 값들입니다. 
# - 값은 일반적으로 숫자, 문자열, 불리언 등 다양한 데이터 타입을 가질 수 있습니다.

# 시리즈는 데이터 분석에서 다양한 용도로 활용됩니다. 
# 예를 들어, 데이터의 색인(Indexing), 슬라이싱(Slicing), 필터링(Filtering), 연산(Operation) 등을 수행할 수 있습니다. 
# 또한, 시리즈는 데이터프레임(DataFrame)의 열(Column)로 사용될 수 있습니다.
#= = = = = = = = = = = = = = = = = = = = = = = = = =

              # 타입 : 시리즈 : 1차원  #

#= = = = = = = = = = = = = = = = = = = = = = = = = =

            # 1.리스트를 활용한 시리즈 생성  #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
import pandas as pd

# 인덱스를 지정하지 않고 Series를 생성합니다.
# 인덱스를 지정하지 않으면 기본적으로 0부터 시작하는 정수형 인덱스가 자동으로 할당됩니다. 
# 이때 인덱스는 0, 1, 2, 3과 같은 정수로 자동으로 지정됩니다.
시리즈1 = pd.Series([1, 2, 3, 4])
시리즈2 = pd.Series(['서울', '부산', '대구', '대전', '광주'])

# 인덱스를 지정하여 Series를 생성합니다.
# 인덱스에는 정수뿐만 아니라 문자열, 날짜 등 다양한 타입의 값을 사용할 수 있습니다. 
# Pandas의 Series를 생성할 때에는 인덱스의 개수와 데이터값의 개수가 일치해야 합니다. 인덱스와 데이터값은 1:1 매칭이 되어야 합니다.
# 인덱스 값에는 여러가지 타입으로 사용 해도 오류가 발생하지는 않지만 일반적으로 통일시키는 것이 좋다.
# index=['a', 'b', '가', 'd', 500] 부분은 리스트를 생성하는 부분이다.
시리즈3 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
시리즈4 = pd.Series(['서울', '부산', '대구', '대전', '광주'], index=['a', 'b', '가', 'd', 500])


#= = = = = = = = = = = = = = = = = = = = = = = = = =

            # 2.딕셔너리를 활용해 시리즈 생성  #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
# 딕셔너리를 활용해 시리즈를 생성합니다.
# data2_list = pd.Series(['서울', 2018], index=['city', 'year'])와 동일하다.
딕셔너리1 = {'city': '서울', 'year': 2018}
시리즈5 = pd.Series(딕셔너리1)

# 해당방식은 리스트를 활용해 하나의 키 값에 여러가지 값을 넣어 줄 수 있습니다.
딕셔너리2 = {'city': ['서울','여러가지값'], 'year': 2018}
시리즈6 = pd.Series(딕셔너리2)

딕셔너리3 = {'city': ['서울', '부산', '대전', '대구', '광주'],
         'year': [2017, 2017, 2018, 2018, 2018],
         'temp': [18, 20, 19, 21, 20]}
시리즈7 = pd.Series(딕셔너리3)

#= = = = = = = = = = = = = = = = = = = = = = = = = =

              # 시리즈 값처리 관련코드 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
# 시리즈1 시리즈 정의
시리즈1 = pd.Series(['c', 'a', 'd', 'a', 'a'])

# 시리즈1 시리즈에서 고유한 값들을 반환합니다.
시리즈1.unique()

# 출력결과: array(['c', 'a', 'd'], dtype=object)

# 시리즈1 시리즈에서 각 값의 빈도수를 반환합니다.
시리즈1.value_counts()
# 출력결과:
c    1
a    3
d    1

# 시리즈1 시리즈에서 각 값의 빈도수를 반환하지만 정렬을 하지 않습니다.
시리즈1.value_counts(sort=False)
# 출력결과:
c    1
a    3
d    1


# 시리즈1 시리즈에서 'b'인 값을 가진 요소가 있는지 확인합니다.
시리즈1.isin(['b'])
# 출력결과:
0    False
1    False
2    False
3    False
4    False


# 시리즈1 시리즈에서 'b' 또는 'c'인 값을 가진 요소가 있는지 확인합니다.
시리즈1.isin(['b','c'])
# 출력결과:
0     True
1    False
2    False
3    False
4     True

# 'b' 또는 'c'를 가진 요소들에 해당하는 위치를 마스킹하여 해당 값을 출력합니다.
# 'b' 또는 'c'를 가진 요소들에 해당새로운 시리즈를 생성합니다
mask = 시리즈1.isin(['b','c'])
시리즈1[mask]
# 출력결과:
0    c
4    c

#= = = = = = = = = = = = = = = = = = = = = = = = = =

                # 시리즈의 속성 순위 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
시리즈 = pd.Series([100, 23, 55, 44, 22, 44, 33, 44])

# 기본적으로는 오름차순으로 순위를 부여합니다.
# 'ascending=False' = 순위의 내림차순
시리즈.rank()
시리즈.rank(ascending=True)
 0    1    2    3    4    5    6    7
8.0  2.0  7.0  5.0  1.0  5.0  3.0  5.0

# 동일한 값을 갖는 요소들 중 가장 작은 순위를 사용합니다.
시리즈.rank(method="min")
 0    1    2    3    4    5    6    7
8.0  2.0  7.0  4.0  1.0  4.0  3.0  4.0

# 동일한 값을 갖는 요소들 중 가장 큰 순위를 사용합니다.
시리즈.rank(method="max")
 0    1    2    3    4    5    6    7
8.0  2.0  7.0  6.0  1.0  6.0  3.0  6.0
# 동일한 값을 갖는 요소들의 순서대로 순위를 부여합니다.
시리즈.rank(method="first")
 0    1    2    3    4    5    6    7
8.0  2.0  7.0  4.0  1.0  5.0  3.0  6.0


#= = = = = = = = = = = = = = = = = = = = = = = = = =

            # 타입 : 데이터프레임 : 2차원  #

#= = = = = = = = = = = = = = = = = = = = = = = = = =

        # 1.딕셔너리를 활용해 데이터프레임 생성 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
# 딕셔너리 형태로 데이터프레임 생성
# 단일 값은 리스트로 감싸지 않아도 자동처리 됩니다.
# 'year' 열 값은 리스트 형태로 전달됨
딕셔너리2 = {'city': ['서울'], 'year': [2018]}
데이터프레임2 = pd.DataFrame(딕셔너리2)
# 데이터프레임2 출력 결과
   city  year
0  서울  2018

# 여러 개의 키와 값이 리스트 형태로 전달됨
# 'city', 'year', 'temp' 열을 가진 데이터프레임 생성
딕셔너리3 = {'city': ['서울', '부산', '대전', '대구', '광주'],
            'year': [2017, 2017, 2018, 2018, 2018],
            'temp': [18, 20, 19, 21, 20]}
데이터프레임3 = pd.DataFrame(딕셔너리3)
# 데이터프레임3 출력 결과
  city  year  temp
0  서울  2017   18
1  부산  2017   20
2  대전  2018   19
3  대구  2018   21
4  광주  2018   20

# 여러 개의 키에 동일한 값이 전달됨
# 'city' 열에는 리스트 형태의 값이 전달되고, 'year' 열에는 단일 값이 전달됨
딕셔너리4 = {'city': ['서울', '부산', '대구', '광주'], 
            'year': 2018}
데이터프레임4 = pd.DataFrame(딕셔너리4)
# 데이터프레임4 출력 결과
  city  year
0  서울  2018
1  부산  2018
2  대구  2018
3  광주  2018

# 딕셔너리 형태로 데이터프레임 생성
# 'b', 'a', 'c' 열을 가진 데이터프레임 생성
데이터프레임5 = pd.DataFrame({'b': [4, 7, 3, 2], 'a': [4, 9, 2, 5], 'c': [5, 3, 7, 9]})
# 데이터프레임5 출력 결과
   b  a  c
0  4  4  5
1  7  9  3
2  3  2  7
3  2  5  9

# 리스트 형태로 데이터프레임 생성
데이터프레임6 = pd.DataFrame([[np.nan, 6.5, 3.], [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
# 데이터프레임6 출력 결과
     0    1    2
0  NaN  6.5  3.0
1  NaN  NaN  NaN
2  NaN  6.5  3.0

# 넘파이 배열을 이용하여 데이터프레임 생성
데이터프레임7 = pd.DataFrame(np.arange(12).reshape(4, 3),
                           columns=['A열', 'B열', 'C열'],
                           index=['a', 'b', 'c', 'd'])
# 데이터프레임7 출력 결과
   A열  B열  C열
a   0   1   2
b   3   4   5
c   6   7   8
d   9  10  11

#= = = = = = = = = = = = = = = = = = = = = = = = = =

               # 2.데이터프레임 속성 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
# DataFrame 'data5'에서 단일 열을 추출합니다.
# 'data5' 데이터프레임에서 'city' 열에 해당하는 시리즈(Series)를 추출하여 변수 a에 저장합니다. 
시리즈 = 데이터프레임['city']         # type : Series

# DataFrame 'data5'에서 여러 열을 추출합니다.
# 'data5' 데이터프레임에서 'year', 'temp' 열에 해당하는 데이터프레임(DataFrame)를 추출하여 변수 a에 저장합니다. 
데이터프레임 = 데이터프레임[['year', 'temp']]    # type : DataFrame

# 데이터프레임에서 열을 추출할 때, 추출된 열이 하나인 경우에는 시리즈로 반환되고, 
# 추출된 열이 여러 개인 경우에는 데이터프레임으로 반환됩니다.

#= = = = = = = = = = = = = = = = = = = = = = = = = =

                  # 2-1.인덱스 값 변경 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
# DataFrame 'data5'의 인덱스를 변경합니다.
# 인덱스의 개수보다 더 많은 값을 넣게된다면 오류가 발생한다.
데이터프레임.index = ['가', 'a', 5.2, '라', '기린']

#= = = = = = = = = = = = = = = = = = = = = = = = = =

                  # 2-2.열 이름 변경 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
# DataFrame 'data5'의 열 이름을 변경합니다.
# 열 이름의 개수가 데이터프레임의 열의 개수보다 많은 경우에는 오류가 발생하게 됩니다. 
# 이는 열 이름의 개수가 일치하지 않기 때문입니다.
# 단 열 이름의 개수보다 적을 경우에는 오류가 발생하지 않습니다.
데이터프레임.columns = ['도시', '연도', '날씨']

#= = = = = = = = = = = = = = = = = = = = = = = = = =

            # 2-3.인덱스 이름으로 행 접근 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
# loc를 사용하여 라벨로 행에 접근합니다.
# 인덱스 이름를 사용해서 행에 접근하는 방식.
데이터프레임.loc['기린']
데이터프레임.loc[5.2]

# iloc를 사용하여 인덱스를 기반으로 행에 접근합니다.
# 1:4는 인덱스 번호 1부터 3까지 (4는 포함되지 않음)의 행을 선택하는 것
데이터프레임.iloc[1:4]

#= = = = = = = = = = = = = = = = = = = = = = = = = =

            # 2-4.열을 인덱스 값으로 설정 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
# '도시' 열을 DataFrame 'data5'의 인덱스로 설정합니다.
# 덮어쓰기 형식으로 처리됨, 기존의 인덱스는 사라진다.
# '도시' 열을 DataFrame '데이터프레임'의 인덱스로 설정하여 새로운 데이터프레임을 반환합니다.
# 새로운 데이터프레임은 '데이터프레임'를 변경하지 않고, 설정된 인덱스를 가지고 있습니다.
데이터프레임2 = 데이터프레임.set_index('도시')

# '도시' 열을 DataFrame '데이터프레임'의 인덱스로 설정하여 변경합니다.
# inplace=True 매개변수를 사용하여 '데이터프레임'를 직접 변경하므로, '데이터프레임'의 내용이 수정됩니다.
데이터프레임.set_index('도시', inplace=True)

#= = = = = = = = = = = = = = = = = = = = = = = = = =

                  # 2-5. 속성 추가#

#= = = = = = = = = = = = = = = = = = = = = = = = = =
# DataFrame 'data5'에 새로운 열 'car'를 추가합니다.
# 기본적으로 가장 오른쪽에 추가됨.
# 같은 이름일 경우에는 값이 덮어씌어진다. 
cars = [50, 40, 20, 30, 10]
데이터프레임['car'] = cars

# 조건에 따라 새로운 열 'high1'을 DataFrame '데이터프레임'에 추가합니다.
# car의 값보다 크거나 같으면 True를 작으면 False를 저장한다.
데이터프레임['high1'] = 데이터프레임.car >= 30

# 다른 조건에 따라 새로운 열 'high2'를 DataFrame '데이터프레임'에 추가합니다.
데이터프레임['high2'] = 데이터프레임.car >= 40

#= = = = = = = = = = = = = = = = = = = = = = = = = =

                  # 2-6. 속성 제거 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
# DataFrame 'data5'에서 'high1' 열을 삭제합니다.
# 만약 같은 값이 있을 경우에는 같은 값을 가진 값이 전부 삭제됩니다.
# 단 해당 코드는 기존의 값을 변경하지 않고 반환하는것 이기에 값이 변경되지 않는다.
데이터프레임.drop('high1', axis=1) # 열: 1, 행: 0

# DataFrame '데이터프레임'에서 'high2' 열을 삭제하고 '데이터프레임2'에 할당합니다.
# 기존의 DataFrame은 변경되지 않음 
# data5.drop('high2', axis=1,inplace=False) 와 동일
데이터프레임2 = 데이터프레임.drop('high2', axis=1) # 열: 1, 행: 0

# DataFrame 'data5'에서 'high1' 열(세로)을 삭제하고 해당 DataFrame을 변경합니다.
데이터프레임.drop('high1', axis=1, inplace=True) # 열: 1, 행: 0

# DataFrame 'data5'에서 인덱스 라벨이 '대구'인 행(가로)을 삭제합니다.
데이터프레임.drop('대구', axis=0, inplace=True) # 열: 1, 행: 0

#= = = = = = = = = = = = = = = = = = = = = = = = = =

                  # 2-7. 속성 정렬 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
[frame]================
       d  a  가  c
three  3  4  2  0
one    1  9  7  5
=======================
# 인덱스를 기준으로 오름차순으로 정렬한 결과를 출력합니다.
# 'one'이 먼저 나오고 'three'가 나중에 나옵니다.
# 열 이름 순서는 유지됩니다.
frame.sort_index()
frame.sort_index(axis=0)
# 출력결과:
       d  a  가  c
one    1	 9	7	 5
three  3  4  2  0

# 열 이름을 기준으로 오름차순으로 정렬한 결과를 출력합니다.
# 열 이름이 'a', 'c', 'd', '가' 순서로 변경됩니다.
# 행의 순서는 유지됩니다.
frame.sort_index(axis=1)
frame.sort_index(axis=1, ascending=True, inplace=True)
# 출력결과:
       a  c  d  가
three  4  0  3  2
one    9  5  1  7

# '가' 열의 값에 따라 내림차순으로 정렬한 결과를 출력합니다.
# 'one' 행이 'three' 행보다 먼저 나옵니다.
# 열 이름 순서는 유지됩니다.
frame.sort_values(by='가', ascending=False)
# 출력결과:
       d  a  가  c
one    1  9  7  5
three  3  4  2  0

[frame2]===============
   b  a  c
0  4  4  5
1  7  9  3
2  3  2  7
3  2  5  9
=======================
frame2.sort_values(by='b')
# 'b' 열을 기준으로 정렬한 결과
   b  a  c
3  2  5  9
2  3  2  7
0  4  4  5
1  7  9  3

frame2.sort_values(by='a')
# 'a' 열을 기준으로 정렬한 결과
   b  a  c
2  3  2  7
0  4  4  5
3  2  5  9
1  7  9  3

frame2.sort_values(by=['b', 'c'])
# 'b'와 'c' 열을 기준으로 정렬한 결과
   b  a  c
3  2  5  9
2  3  2  7
0  4  4  5
1  7  9  3

#= = = = = = = = = = = = = = = = = = = = = = = = = =

                  # 2-8. 속성 순위 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
데이터프레임 = DataFrame({'b':[4, 4, 4, 2], 'a':[4, 9, 2, 5], 'c': [5, 3, 7, 9]})
   b  a  c
0  4  4  5
1  4  9  3
2  4  2  7
3  2  5  9

# 데이터프레임에 rank() 메서드를 적용하여 각 요소의 순위를 매깁니다.
# 기본적으로는 오름차순으로 순위를 매기며, 동일한 값이 있을 경우 평균 순위를 부여합니다.
# 기본적으로 행 기준으로 순위를 매깁니다.
# rank(axis=0 or 1, ascending=True or False, method='first' or 'min' or 'max')
데이터프레임.rank() 
	 b	 a	 c
0	3.0	2.0	2.0
1	3.0	4.0	1.0
2	3.0	1.0	3.0
3	1.0	3.0	4.0

#= = = = = = = = = = = = = = = = = = = = = = = = = =

                 # 2-9. 속성 합/평균 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
데이터프레임 = DataFrame({'b':[4, 4, 4, 2], 'a':[4, 9, 2, 5], 'c': [5, 3, 7, 9]})
   b  a  c
0  4  4  5
1  4  9  3
2  4  2  7
3  2  5  9
# 데이터프레임의 열을 기준으로 합을 계산합니다.
데이터프레임.sum()

# 데이터프레임의 행을 기준으로 합을 계산합니다.
데이터프레임.sum(1)

# 데이터프레임의 열을 기준으로 평균을 계산합니다.
데이터프레임.mean()

# 데이터프레임의 행을 기준으로 평균을 계산합니다.
데이터프레임.mean(1)

데이터프레임2 = DataFrame({'b':[4, 4, 4, 2], 'a':[4, 9, 2, 5], 'c': [5, 3, 7, np.nan]})
	b	a	 c
0	4	4	5.0
1	4	9	3.0
2	4	2	7.0
3	2	5	NaN

# 데이터프레임2의 각 열에 대한 합을 계산합니다.
# 이때 NaN(결측값)을 포함하여 계산하며, skipna=False로 설정되어 있습니다.
# 따라서 NaN 값이 있는 열은 해당 위치의 합계가 NaN으로 반환됩니다.
# 이 매개변수를 지정하지 않거나 기본값인 skipna=True로 설정할 경우 NaN 값을 무시하고 합계를 계산합니다.
데이터프레임2.sum(skipna=False)
b    14.0
a    20.0
c     NaN

# NaN 값을 77로 변경합니다.
데이터프레임2.fillna(77)

# 데이터프레임2에서 각 행에 대해 최대값이 위치한 열의 인덱스를 반환합니다.
# idxmax(axis=1)은 행을 기준으로 각 행의 최대값이 위치한 열의 인덱스를 찾는 것을 의미합니다.
데이터프레임2.idxmax(1)
0    c
1    a
2    c
3    a

# 데이터프레임2에서 각 열에 대해 최대값이 위치한 행의 인덱스를 반환합니다.
# idxmax(axis=0)은 열을 기준으로 각 열의 최대값이 위치한 행의 인덱스를 찾는 것을 의미합니다.
데이터프레임2.idxmax(0)
b    0
a    1
c    2

# 데이터프레임2에서 idxmin() 메서드를 사용하여 각 행에서 최소값의 인덱스를 반환합니다.
# 여기서 axis=1은 행을 기준으로 동작하며, 각 행에서 최소값의 인덱스를 찾습니다.
# 반환되는 값은 각 행에서 최소값의 위치를 나타냅니다.
데이터프레임2.idxmin(1)
0    b
1    c
2    a
3    b

# 주의 : axis의 값이 sum의 axis와 반대이다.
# dropna(axis=0)은 NaN 값을 포함한 행을 제거합니다.
# 따라서 NaN 값이 있는 행이 제거된 데이터프레임이 반환됩니다.
데이터프레임2.dropna()
데이터프레임2.dropna(axis=0)
	b	a	 c
0	4	4	5.0
1	4	9	3.0
2	4	2	7.0

# 주의 : axis의 값이 sum의 axis와 반대이다.
# 데이터프레임2에서 NaN 값을 포함한 열을 제거합니다.
# axis=1은 열을 나타내며, 따라서 dropna(axis=1)은 NaN 값을 포함한 열을 제거합니다.
데이터프레임2.dropna(axis=1)
	b	a
0	4	4
1	4	9
2	4	2
3	2	5

# 데이터프레임2.dropna(axis=0 or 1, inplace=False or True,how='all')
# how='all' 전부 결측값인 열이나 행을 제거합니다.

#= = = = = = = = = = = = = = = = = = = = = = = = = =

               # 2-10. 파일 입출력 관련 #

#= = = = = = = = = = = = = = = = = = = = = = = = = =
# 시리즈를 CSV 파일로 저장합니다.
# './file2.csv'는 저장할 파일의 경로와 이름을 나타냅니다.
# header=True는 열 이름을 포함하여 저장하고, index=False는 인덱스를 저장하지 않습니다.
# encoding='utf-8'은 UTF-8 인코딩을 사용하여 파일을 저장합니다.
데이터프레임.to_csv('./file2.csv', header=True, index=False, encoding='utf-8')

# CSV 파일을 읽어서 데이터프레임으로 변환합니다.
# './file2.csv'에서 파일을 읽어오며, sep=','는 구분자로 쉼표를 사용합니다.
데이터프레임 = pd.read_csv('./file2.csv', sep=',')



