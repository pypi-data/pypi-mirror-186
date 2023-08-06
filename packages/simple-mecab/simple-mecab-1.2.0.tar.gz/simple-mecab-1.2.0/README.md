# Python package "simple-mecab"

**MeCabをPythonから簡単に使えるようにした、[mecab](https://pypi.org/project/mecab/)パッケージのラッパーです。**

通常のMeCabよりも使える機能に制限がありますが、辞書の違いを吸収して統一されたアクセス方法で形態素情報にアクセスできます。

## インストール方法

ターミナルで `pip install simple-mecab` を実行し、パッケージをインストールします。

## 要件
- Python 3.7 以上 （`mecab`パッケージが対応しているバージョンのみ）
- 形態素解析器MeCabとUTF-8辞書がインストール済みで、プログラムからアクセス可能である
- `mecab`パッケージをインストールできる環境にあること  
  （このパッケージをインストールする際に、pipによって`mecab`パッケージが自動的にインストールされます。）  
  - コンピューターにインストールされたMeCabの対応bitとPythonのアーキテクチャが一致していること  
    （例：MeCab 32bitとPython 32bit, MeCab 64bitとPython 64bit）
  - Pythonのバージョンが`mecab`パッケージの対応バージョンであること  

## 使い方

### MeCabWrapperのインスタンスを入手する
```python
mecab = simple_mecab.MeCabWrapper(args="{MeCab Args}", dict_type='{dict_type Literal}')
```
で入手できます。

#### 引数argsについて
`args`には、通常MeCabをコマンドラインで実行する際に指定する引数を文字列としてそのまま指定できます。ただし、以下の引数は指定することができません。
- `-Owakati` → [`mecab.wakati_gaki()`関数](#日本語の文を分かち書きする)を使用してください。
- `-F`, `-U`, `-B`, `-E`, `-S`, `-x` といった出力フォーマットを指定する引数 → MeCabの出力を自動分類する性質上サポートできません。  
  未知語の推定機能の利用可否の設定は今後追加予定です。
- `-N {N}` → 今後対応予定です。

何も指定しないと、引数なし（`''`）と同義になります。


#### 引数dict_typeについて
`dict_type`には以下の文字列のいずれかを指定してください。[**`ipadic`以外はまだ実装されていません。**]
| dict_type   | 使用辞書                                             |
| :---------- | :--------------------------------------------------- |
| ipadic      | IPA辞書, mecab-ipadic-NEologd辞書 or 出力形式が同様の辞書                      |
| ~~unidic~~  | ~~UniDic辞書 or 出力形式が同様の辞書~~ (version 2.0で対応予定)              |

何も指定しないと`ipadic`が使用されます。


### 日本語の文を形態素解析する
```python
result = mecab.parse("文")
```
で、`"文"`の形態素解析結果を入手できます。

形態素解析結果は各形態素のlist形式になっていて、それぞれの要素は形態素の`Morpheme`クラスのインスタンスです。

#### Morphemeクラスの構成
`Morpheme`クラスはPythonの`dataclass`として定義されており、形態素とその属性が格納されています。

例えば変数`r`にある形態素の`Morpheme`クラスのインスタンスが格納されているとき、
```
{MeCabの項目の値} = r.{Morphemeのproperty}
```
で、属性の値を知ることができます。

サポートされている属性は以下のとおりです。
| MeCabの項目    | Morphemeのproperty | propertyのtype         | 出力例                                 | 
| -------------- | ------------------ | ---------------------- | -------------------------------------- | 
| 形態素の文字列 | token              | `str`                  | '東京', '行っ'                         | 
| 品詞           | pos0               | `str` or `None`        | '名詞', '動詞'                         | 
| 品詞細分類1    | pos1               | `str` or `None`        | '固有名詞', '自立'                     | 
| 品詞細分類2    | pos2               | `str` or `None`        | '地域', None                           | 
| 品詞細分類3    | pos3               | `str` or `None`        | '一般', None                           | 
| 活用型         | conjugation_type   | `str` or `None`        | None, '五段・カ行促音便'               | 
| 活用形         | conjugation        | `str` or `None`        | None, '連用タ接続'                     | 
| 原型           | stem_form          | `str` or `None`        | '東京', '行く'                         | 
| 発音           | pronunciation      | `tuple[str]` or `None` | ('トウキョウ', 'トーキョー'), ('イッ') | 
| <分類失敗時>   | unknown            | `str` or `None`        | None, None                             | 

`token`は常に文字列が格納されます。

それ以外の属性は、存在するときはその値の文字列、存在しない場合には`None`が格納されます。

`pronunciation`のみ、発音が1つしかない場合でもタプルが格納されるため、`r.pronunciation[0]`などでアクセスしてください。  
（IPA辞書の場合、MeCabの出力した発音2種がどちらも異なる場合にのみ、タプルの要素が2つになります。）

`unknown`にはMeCabの出力を正しく分類できなかった際に、MeCabの出力結果が文字列としてそのまま格納されます。通常は`None`です。MeCabの辞書を正しく分類するために、[`dict_type`](#引数dict_typeについて)は正しく指定してください。


### 日本語の文を分かち書きする
このパッケージではMeCab標準の`-Owakati`を用いた分かち書きを使用することができません。代わりに、
```python
wakati_result = mecab.wakati_gaki("文")
```
によって文を形態素ごとに分割できます。

`wakati_result`はそれぞれの形態素をスペースで区切った文字列になっています。


## 例外
`simple_mecab.InvalidArgumentError` : このパッケージがサポートしていない引数が`MeCabWrapper()`の`args`に指定された場合に発生します。対応しない引数を削除して再度お試しください。

## サンプル
以下ではサンプルとして "渋谷に行った。" という文を形態素解析・分かち書きした際のPythonコードと結果を示します。

[Python 3.10]
```python
import simple_mecab

target_sentence = "渋谷に行った。"

mecab: simple_mecab.MeCabWrapper = simple_mecab.MeCabWrapper(args=r"-r C:\PROGRA~2\MeCab\etc\mecabrc", dict_type='ipadic')

result: list[simple_mecab.Morpheme] = mecab.parse(target_sentence)

# 各形態素について属性を表示する
for r in result:
    print("形態素", r.token)
    print("品詞", r.pos0)
    print("品詞細分類1", r.pos1)
    print("品詞細分類2", r.pos2)
    print("品詞細分類3", r.pos3)
    print("活用型", r.conjugation_type)
    print("活用形", r.conjugation)
    print("原型", r.stem_form)
    print("発音", r.pronunciation)
    print("<分類失敗時>", r.unknown)
    print('\n')

# 文を分かち書きする
wakati_result: str = mecab.wakati_gaki(target_sentence)
print("文をスペース区切りの分かち書きにします。")
print(wakati_result)
```

[出力]
```
形態素 渋谷
品詞 名詞
品詞細分類1 固有名詞
品詞細分類2 地域
品詞細分類3 一般
活用型 None
活用形 None
原型 渋谷
発音 シブヤ
<分類失敗時> None


形態素 に
品詞 助詞
品詞細分類1 格助詞
品詞細分類2 一般
品詞細分類3 None
活用型 None
活用形 None
原型 に
発音 ニ
<分類失敗時> None


形態素 行っ
品詞 動詞
品詞細分類1 自立
品詞細分類2 None
品詞細分類3 None
活用型 五段・カ行促音便
活用形 連用タ接続
原型 行く
発音 イッ
<分類失敗時> None


形態素 た
品詞 助動詞
品詞細分類1 None
品詞細分類2 None
品詞細分類3 None
活用型 特殊・タ
活用形 基本形
原型 た
発音 タ
<分類失敗時> None


形態素 。
品詞 記号
品詞細分類1 句点
品詞細分類2 None
品詞細分類3 None
活用型 None
活用形 None
原型 。
発音 。
<分類失敗時> None


文をスペース区切りの分かち書きにします。
渋谷 に 行っ た 。
```

さらにサンプルコードを閲覧したい場合には[sample.ipynb](sample.ipynb)を参照してください。
