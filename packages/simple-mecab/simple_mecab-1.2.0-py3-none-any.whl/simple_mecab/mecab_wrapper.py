import re
from typing import List, Literal

import MeCab

from simple_mecab.exceptions import InvalidArgumentError
from simple_mecab.morpheme import Morpheme


class MeCabWrapper:
    """MeCabをより簡単に使えるようにするラッパークラスです。

    Features
    --------
    - MeCabの処理結果をdataclassに格納し、アクセスしやすくしています。

    - EOSや空文字('')の除去を行っています。


    Attributes
    ----------
    multiple_instance : bool
        `True` に設定すると、通常通りインスタンスを複数作成できます。

        `False` に設定すると、何度インスタンス生成を行っても同じインスタンスを使用します。

        デフォルトは `False` です。


    Dependencies
    ------------
    - コンピュータにMeCabがインストールされ、プログラムからアクセス可能である必要があります。

    - `mecab-python3` ライブラリがインストールされている必要があります。

    - 同ライブラリの中の Morpheme dataclass を使用して結果を格納します。
    """

    __none_pattern: List[str] = ['', ' ', '*']  # 該当なしのパターン

    __banned_args = (r'-O',
                     r'-F', r'--node-format',
                     r'-U', r'--unk-format',
                     r'-B', r'--bos-format',
                     r'-E', r'--eos-format',
                     r'-S', r'--eon-format',
                     r'-x', r'--unk-feature')

    def __init__(self, args: str = '',
                 dict_type: Literal['ipadic', 'unidic'] = 'ipadic') -> None:
        """
        Parameters
        ----------
        args : str, optional
            MeCabの実行時引数を入力してください。
            ただし以下の引数は入力しないでください。

            `-O{文字列}`, 出力フォーマットを指定するオプション

            デフォルトは引数なしです。

        dict_type : Literal['ipadic, 'unidic'], optional
            MeCabで使用する辞書の表示タイプを選択してください。
            - `'ipadic'` : IPA辞書のデフォルト表示タイプ
            - `'unidic'` : UniDicのデフォルト表示タイプ

            辞書の出力と表示タイプが一致していない場合、正しく結果を抽出できません。
            デフォルトは `'ipadic'` です。

        Raises
        ------
        InvalidArgumentError
            argsに禁止されている引数が存在する場合に発生します。
        """
        self.__mecab_args = args
        self.__dict_type = dict_type
        self.__latest_input = ''
        invalid_args = self.__are_contained(set(self.__banned_args), args)
        if not invalid_args:
            self.tagger = MeCab.Tagger(args)
        else:
            raise InvalidArgumentError(
                f"{', '.join(invalid_args)} がargsに指定されました。\n"
                "MeCabWrapperのargsでは以下に示す引数を使用することはできません。\n"
                f"{', '.join(self.__banned_args)}\n"
                "[ヒント] もし分かち書きをしたいのであれば、wakati_gaki関数を使用することができます。")

    def parse(self, sentence: str) -> List[Morpheme]:
        """日本語の文字列をMeCabで解析します。

        Parameters
        ----------
        sentence : str
            MeCabで解析したい日本語の文章

        Returns
        -------
        list[Morpheme]
            形態素ごとにそれぞれ Morpheme クラスに情報が格納されています。
            （アクセス例：`mecab.parse()[0].token`）
            詳細は Morpheme クラスの docstring を参照してください。
        """
        result: List[Morpheme] = []
        self.__latest_input = sentence
        parsed_string = self.tagger.parse(self.__latest_input)
        words: List[str] = parsed_string.split('\n')
        words.remove('EOS')
        words.remove('')
        for w in words:
            result.append(self.__extract(w))
        return result

    def wakati_gaki(self, sentence: str) -> str:
        """文を分かち書きして、リストに格納します。

        Parameters
        ----------
        sentence : str
            分かち書きしたい文（一文）

        Returns
        -------
        list[str]
            分かち書きされた形態素のリスト
        """
        wakati_list: List[str] = []
        for e in self.parse(sentence):
            wakati_list.append(e.token)
        return ' '.join(wakati_list)

    @property
    def latest_input(self) -> str:
        """最新の入力

        Returns
        -------
        str
            MeCabWrapperのメソッドに最後に入力された文字列を返します。
        """
        return self.__latest_input

    @property
    def dict_type(self) -> str:
        """辞書タイプ

        Returns
        -------
        str
            MeCabWrapperに指定された辞書タイプの文字列を返します。
        """
        return self.__dict_type

    @property
    def mecab_args(self) -> str:
        """MeCab引数

        Returns
        -------
        str
            MeCabWrapperに指定されたMeCabの起動時引数を文字列で返します。
        """
        return self.__mecab_args

    def __are_contained(self, query_str: set[str], target_str: str):
        query_re = '|'.join(query_str)
        return re.findall(query_re, target_str)

    def __extract(self, parsed_word: str) -> Morpheme:
        if self.__dict_type == 'ipadic':
            surface, features = parsed_word.split('\t')
            features_list = features.split(',')
            pronunciation = None
            if len(features_list) > 7:
                pronunciation = [features_list[7]]
                if len(features_list) > 8 and features_list[7] != features_list[8]:
                    pronunciation.append(features_list[8])
                pronunciation = tuple(pronunciation)
            ret = Morpheme(surface,
                           features_list[0] if len(
                               features_list) > 0 and features_list[0] not in self.__none_pattern else None,
                           features_list[1] if len(
                               features_list) > 1 and features_list[1] not in self.__none_pattern else None,
                           features_list[2] if len(
                               features_list) > 2 and features_list[2] not in self.__none_pattern else None,
                           features_list[3] if len(
                               features_list) > 3 and features_list[3] not in self.__none_pattern else None,
                           features_list[4] if len(
                               features_list) > 4 and features_list[4] not in self.__none_pattern else None,
                           features_list[5] if len(
                               features_list) > 5 and features_list[5] not in self.__none_pattern else None,
                           features_list[6] if len(
                               features_list) > 6 and features_list[6] not in self.__none_pattern else None,
                           pronunciation,
                           None)
            return ret
        elif self.__dict_type == 'unidic':
            raise NotImplementedError("UniDic辞書のパーサーは未実装です。")
        else:
            surface, feature = parsed_word.split()
            ret = Morpheme(surface, None, None, None, None,
                           None, None, None, None, feature)
            return ret
